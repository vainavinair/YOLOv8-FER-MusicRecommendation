import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = b'\xd1\x84Q\xe2\xc5\x16\xbe\xeb\xc7\xd7\xdc/\t\xb9F\xf6#d\xf5\xe21B\xa2'
    STATIC_URL_PATH = '/static'
    CLIENT_ID = '5f8fe92f97064745b0029b686ccf8396'
    CLIENT_SECRET_KEY = '9bb108de0d0847849c3cec57475aa34b'