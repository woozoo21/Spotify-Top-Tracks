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

## License

### Spotify API Usage License

This project utilizes the **Spotify Web API** for fetching and displaying data related to artists' top tracks and users' recently played tracks. By using this project, you agree to comply with the **Spotify Developer Terms of Service** and the **Spotify Developer Agreement**.

- **Spotify Developer Terms of Service**: [https://developer.spotify.com/terms/](https://developer.spotify.com/terms/)
- **Spotify Developer Agreement**: [https://developer.spotify.com/legal/](https://developer.spotify.com/legal/)

#### Spotify API Authentication
This project requires the user to authenticate via Spotify's OAuth 2.0 authentication flow to access their data. The user must provide their own **Client ID** and **Client Secret** from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) in order to interact with the API.

#### Restrictions
- The use of the Spotify Web API is subject to Spotify’s [API Terms of Service](https://developer.spotify.com/terms/).
- The API is provided on an "as-is" basis, and Spotify does not guarantee availability or reliability of the API.

#### Attribution
The Spotify Web API is a third-party service provided by Spotify AB. The data provided through the API is the property of Spotify. You should always give appropriate attribution to Spotify when displaying data from their API.

By using this project, you acknowledge that you understand and agree to these terms.

