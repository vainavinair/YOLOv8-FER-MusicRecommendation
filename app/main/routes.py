from flask_login import login_required
from app.main import bp
from flask import Response, redirect, render_template, request, session, url_for

from app.main.camera import VideoCamera
from app.main.songs import get_song
from ..recommedations.spotify_auth import SpotifyAPI


video_stream = VideoCamera()

@login_required
@bp.route('/')
def home():
    if 'username' in session:
        s_api = SpotifyAPI()
        token = s_api.get_token()
        session['token'] = token
        video_stream.off_camera()
        return render_template('camera.html')
    else:
        return redirect(url_for('users.login'))


def gen(camera):
    while True:
        frame= camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@bp.route('/video_feed')
def video_feed():
     return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@bp.route('/requests',methods=['POST','GET'])
def tasks():
    if request.method == 'POST':
        if request.form.get('start') == 'Start':
            video_stream.on_camera()
            return render_template('camera.html')
        elif request.form.get('stop') == 'Stop':
            video_stream.off_camera()
            return render_template('camera.html')
        
        elif request.form.get('capture') == 'Capture':
            video_stream.off_camera()
            emotion = video_stream.get_detected_emotion()
            session['emotion'] = emotion
            return redirect(url_for('recommendations.recommend'))
    # Add a return statement to return an empty string for the GET request
        
@bp.route('/about')
def about():
        if 'username' in session:
            return render_template('about.html')
        else:
            return redirect(url_for('users.login'))