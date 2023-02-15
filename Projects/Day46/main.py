import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Scraping Billboard for the TOP 100 musics for specific date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
list_name = input("What name you want to give to your playlist?: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
song_titles = response.text
soup = BeautifulSoup(song_titles, 'html.parser')
songs = soup.select(".o-chart-results-list__item > h3#title-of-a-story")
song_names = [title.getText(strip=True) for title in songs]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
songs_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
        # print(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, public=False, name=f"{year}: {list_name}")
print(playlist['external_urls']['spotify'])

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
