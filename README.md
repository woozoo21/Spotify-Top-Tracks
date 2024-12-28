# Spotify Top Tracks       ⇆   ◃◃   ıı   ▹▹   ↻

This project allows users to check if they are contributing to the top tracks of their favorite artist on Spotify. It compares the user's recent tracks with the top tracks of an artist and displays a message with visual effects based on the results.

## Features
- Enter your favorite artist's name.
- Check if you are listening to the artist's top tracks.
- See your recently played tracks and compare them to the artist's top tracks.
- Enjoy fun animations like confetti when contributing to an artist's top tracks.

## Technologies Used
- HTML
- CSS
- JavaScript
- Flask (Python)

## Spotify API Usage

In this project, I used the [Spotify Web API](https://developer.spotify.com/) to retrieve the top tracks and recently played tracks for a given artist. 

### How the Spotify API was integrated:
1. **Authentication**: The project uses Spotify’s OAuth 2.0 system for user authentication, which grants access to the user’s data (e.g., recently played tracks).
2. **Top Tracks**: Using the API's `artists/{id}/top-tracks` endpoint, I retrieved the top tracks of the specified artist.
3. **Recently Played Tracks**: I used the `me/player/recently-played` endpoint to fetch the user’s most recent tracks.
4. **Comparing Tracks**: The project compares the tracks the user has recently listened to with the artist's top tracks to check for common tracks and display relevant messages.

For more information, visit [Spotify Developer Portal](https://developer.spotify.com/).

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/woozoo21/Spotify-Top-Tracks.git
   ```
   
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
3. Run the application:
   ```
   python app.py
   ```
