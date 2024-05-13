# Moodify: Feel, Express, Listen - Your Emotions, Your Playlist.


Moodify is a Flask-based web application that seamlessly integrates facial emotion recognition (FER) with personalized music recommendations. By leveraging advanced algorithms and technologies, Moodify offers users a dynamic and immersive music listening experience tailored to their emotional states and preferences. This implementation serves as the GUI for the proposed model described in my research paper *Integrating Facial Emotion Recognition into Music Recommendation Systems*.

## Features

- **Facial Emotion Detection**: Users can interact with the application through their webcam, allowing real-time analysis of facial expressions to determine emotional states.
- **Personalized Music Recommendations**:
  - **Your Favorites Suggestions**: Offering a selection of top favorite songs aligned with the detected emotion using cosine similarity.
  - **Currently Popular Suggestions**: Based on KNN recommendations, users can explore currently popular songs tailored to their listening profiles.
  - **Discover New Suggestions**: Presenting random popular songs based on the user's listening profile across all emotions using SVD(Singular value decomposition), inviting users to explore new musical avenues.
- **Login Authentication**: Implemented to provide access to personalized recommendations and past data, ensuring security and enhancing user engagement.

## Screenshots

- **Login Page**:
  ![Login Page](https://i.imgur.com/1C3Fxgb.png)

- **Home Page**:
  ![Home Page](https://i.imgur.com/wzc3k3f.png)

- **Camera Page**:
  ![Camera Page](https://i.imgur.com/LxXQszV.png)

- **Recommendations Page**:
  ![Recommendations Page 1](https://i.imgur.com/kKUMHz1.png)

- **Recommendations After Selecting a Song**:
  ![Recommendations Page 2](https://i.imgur.com/ofyOrjU.png)