from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

#get titles from Bilboard100

#playlist_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
playlist_date = "2023-06-14"
URL = f"https://www.billboard.com/charts/hot-100/{playlist_date}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")

songs_titles = soup.select("li.o-chart-results-list__item > h3#title-of-a-story.c-title")

titles_list = [title.getText().strip() for title in songs_titles]

#Spotify
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://open.spotify.com/",
    scope=scope,
    show_dialog=True,
))

user_id = sp.current_user()["id"]

song_uris = []
for title in titles_list:
    results = sp.search(q=title, type="track")
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{playlist_date} Billboard 100", public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)