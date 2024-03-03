# import base64, json, requests



# SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
# SPOTIFY_URL_TRACKS = 'https://api.spotify.com/v1/tracks/'

# client_id = '5f8fe92f97064745b0029b686ccf8396'
# client_secret = '9bb108de0d0847849c3cec57475aa34b'

# def get_token():
#     auth_string = "{}:{}".format(client_id, client_secret)
#     auth_bytes = auth_string.encode('utf-8')
#     encoded = str(base64.b64encode(auth_bytes),'utf-8')
#     headers = {"Content-Type" : 'application/x-www-form-urlencoded', "Authorization" : "Basic {}".format(encoded)} 

#     data = {'grant_type': "client_credentials"}

#     result = requests.post(SPOTIFY_URL_TOKEN, data=data, headers=headers)
#     json_result = json.loads(result.content)
#     token = json_result["access_token"]
#     return token

# def get_auth_header(token):
#     return{'Authorization':'Bearer '+ token}


# def get_track(token,id):
#     url = f'https://api.spotify.com/v1/tracks/?ids={id}'
#     header = get_auth_header(token)
#     result = requests.get(url,headers=header)
#     json_result = json.loads(result.content)
#     print(json_result)

# token = get_token()
# song = get_track(token,'7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')
# print(song)