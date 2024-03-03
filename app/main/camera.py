from flask import url_for
import cv2
from ultralytics import YOLO
from numpy import argmax

class VideoCamera(object):

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.is_running = True
        #Load Yolo
        
        model_url = 'D:/study/rserch-fer/model/runs/classify/train17/weights/best.pt'
        self.model = YOLO(model_url)
        # Load the Haar Cascade Classifier for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Set the desired frame size (64x64)
        self.desired_frame_size = (64, 64)
        self.detected_emotion = 'Neutral'

    def __del__(self):
        self.video.release()  

    def on_camera(self):
        # Toggle the camera's state between running and stopped
        self.is_running = True
        self.video = cv2.VideoCapture(0)  

    def off_camera(self):
        # Toggle the camera's state between running and stopped
        self.is_running = False
        self.video.release()    

    def get_detected_emotion(self):
        return self.detected_emotion     

    def get_frame(self):
        ret, frame = self.video.read()
        if not ret:
            # If there's an issue with capturing the frame, return an empty byte string
            return b''
        try:
            global emotion
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Perform face detection using the Haar Cascade Classifier
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                # Crop the detected face region
                face = frame[y:y+h, x:x+w]
                # Resize the face to the desired size (64x64) for emotion detection
                processed_face = cv2.resize(face, self.desired_frame_size)
                # Perform emotion detection using your YOLOv8 model on the cropped face
                results = self.model(processed_face)  # This will return a list of Results objects
                # Process the emotion predictions (adjust as needed)
                emotion_labels = results[0].names  # Get the class labels from the names attribute
                probs = results[0].probs.data.tolist()
                max_emotion_idx = argmax(probs)  # Assuming the first result corresponds to emotion
                predicted_emotion = emotion_labels[max_emotion_idx]
                # Display the emotion text on the frame
                cv2.putText(frame, f"Emotion: {predicted_emotion}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.detected_emotion = predicted_emotion
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return b''