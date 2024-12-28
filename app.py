from flask import Flask, render_template, request, jsonify
import os
import base64
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = "user-read-recently-played"

sp_oauth = SpotifyOAuth(client_id=client_id,
                         client_secret=client_secret,
                         redirect_uri=redirect_uri,
                         scope=scope)

# Function to get Spotify client
def get_spotify_client():
    token_info = sp_oauth.get_access_token()
    if not token_info:
        return None
    token = token_info['access_token']
    sp = spotipy.Spotify(auth=token)
    return sp

# Function to search for an artist and get top tracks
def search_for_artist_and_tracks(artist_name):
    sp = get_spotify_client()
    if sp is None:
        return None

    result = sp.search(q=artist_name, type="artist", limit=1)
    if not result['artists']['items']:
        return None

    artist_id = result['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id, country='US')['tracks']
    return top_tracks

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user input and display results
@app.route('/check_tracks', methods=['POST'])
def check_tracks():
    artist_name = request.form['artist_name']
    sp = get_spotify_client()
    if not sp:
        return jsonify({'error': 'Spotify authentication failed'})

    # Get recently played tracks
    recently_played = sp.current_user_recently_played(limit=50)['items']
    top_tracks = search_for_artist_and_tracks(artist_name)

    if top_tracks is None:
        return jsonify({'error': 'Artist not found or no tracks available'})

    # Process the results
    recently_played_names = [track['track']['name'] for track in recently_played]
    top_track_names = [track['name'] for track in top_tracks]
    
    common_tracks = set(recently_played_names) & set(top_track_names)
    
    return jsonify({
        'common_tracks': list(common_tracks),
        'recent_tracks': recently_played_names,
        'top_tracks': [track['name'] for track in top_tracks]
    })

if __name__ == "__main__":
    app.run(debug=True)
