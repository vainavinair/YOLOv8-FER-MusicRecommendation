import base64
import json
import requests
from app.config import Config

SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
SPOTIFY_URL_TRACKS = 'https://api.spotify.com/v1/tracks/'

client_id = Config.CLIENT_ID
client_secret = Config.CLIENT_SECRET_KEY

class SpotifyAPI:
    def get_token(self):
        auth_string = "{}:{}".format(client_id, client_secret)
        auth_bytes = auth_string.encode('utf-8')
        encoded = str(base64.b64encode(auth_bytes), 'utf-8')
        headers = {"Content-Type": 'application/x-www-form-urlencoded', "Authorization": "Basic {}".format(encoded)}

        data = {'grant_type': "client_credentials"}

        result = requests.post(SPOTIFY_URL_TOKEN, data=data, headers=headers)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(self, token):
        return {'Authorization': 'Bearer ' + token}

    def get_tracks(self, token, ids):
        
        url = f'https://api.spotify.com/v1/tracks/?ids={ids}'
        header = self.get_auth_header(token)
        result = requests.get(url, headers=header)
        data = json.loads(result.content)
        # return json_result
        song_images = [track['album']['images'][0]['url'] for track in data['tracks']]
        song_name = [track['name']for track in data['tracks']]
        song_ids = [track['id']for track in data['tracks']]
        artist_names = []
        for track in data['tracks']:
            artists = [artist['name'] for artist in track.get('artists', [])]
            if not artists:
                    artists = ['Unknown']
            artist_names.append(artists)
        songs_details = {
            'images': song_images,
            'names': song_name,
            'id': song_ids,
            'artists' : artist_names
            }
        return songs_details
