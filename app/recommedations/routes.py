import json
from app.recommedations import bp
from flask import Response, redirect, render_template, request, session, url_for
from app.main.songs import get_song
from app.static.FER_recom.cs_rec import ContentBasedRecommender
from app.static.FER_recom.knn_rec import KNNRecommender
from app.static.FER_recom.svd_rec import SVDRecommend
from ..recommedations.spotify_auth import SpotifyAPI
import requests



cs = ContentBasedRecommender()
knn = KNNRecommender()
svd = SVDRecommend()



@bp.route('/', methods=['POST','GET'])
def recommend():
    user = session.get('username')
    print(user)
    s_api = SpotifyAPI()
    token = session.get('token')
    emotion = session.get('emotion')
    songs = get_song(emotion,user)
    ids = songs['SongID'].tolist()
    ids = ','.join(ids)
    song_details = s_api.get_tracks(token, ids)
#     print(song_details)
    if request.method == 'POST':
        song_id = request.form['song_name']
        cs_songs = cs.recommender(user_id=user,recommendation={"SongID": song_id,"number_songs": 5 })
        cs_ids = []
        for x in cs_songs:
                cs_ids.append(x[3])
        cs_ids = ','.join(cs_ids)
        cs_songs_details = s_api.get_tracks(token, cs_ids)
        ibcf_songs = knn.recommender(song_id=song_id)
        ibcf_ids = []
        for x in ibcf_songs:
                ibcf_ids.append(x['song_id'])
        ibcf_ids = ','.join(ibcf_ids)
        ibcf_songs_details = s_api.get_tracks(token, ibcf_ids)
        ubcf_songs = svd.recommender(user=44, K =5)
        ubcf_ids = []
        for x in ubcf_songs:
                ubcf_ids.append(x['song_id'])
        ubcf_ids = ','.join(ubcf_ids)
        ubcf_songs_details = s_api.get_tracks(token, ubcf_ids)
        return render_template('songs.html', emotion=emotion, song_id=song_id, cs_songs=cs_songs_details, ibcf_songs=ibcf_songs_details, ubcf_songs=ubcf_songs_details)
    return render_template('songs.html', songs=song_details, emotion=emotion)
