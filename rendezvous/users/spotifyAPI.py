import requests

client_id = '91e3a670387a494bb34172896b2a2f93'
client_secret = 'a6c546fdaf4646afaeeba882c70999a7'

# https://accounts.spotify.com/authorize?client_id=91e3a670387a494bb34172896b2a2f93&response_type=code&redirect_uri=http://mysite.com/callback/&scope=user-read-recently-played user-read-playback-state user-top-read user-read-currently-playing user-follow-read user-read-playback-position'

def get_auth_data(code):
    url = 'https://accounts.spotify.com/api/token'
    query = {
        'grant_type': "authorization_code",
        'code': code,
        'redirect_uri': 'http://mysite.com/callback/'
    }

    auth_data = requests.post(url,
                              params=query,
                              auth=(client_id, client_secret)).json()
    # Access and Refresh Token
    return auth_data['access_token'], auth_data['refresh_token']


def get_top_artists(token, num):
    url = 'https://api.spotify.com/v1/me/top/artists'
    query = {
        'time_range': 'medium_term',
        'limit': num,
        'offset': 0
    }

    header = {
        'Authorization': 'Bearer ' + token
    }
    return requests.get(url, params=query, headers=header).json()


def refresh_access_token(token):
    url = 'https://accounts.spotify.com/api/token'
    query = {
        'grant_type': 'refresh_token',
        'refresh_token': token
    }

    return requests.post(url,
                         data=query,
                         auth=(client_id, client_secret)).json()['access_token']
