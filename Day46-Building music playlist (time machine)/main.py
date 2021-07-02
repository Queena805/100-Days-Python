from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL= "https://www.billboard.com/charts/hot-100/"

ClientID = "ebc7a963bd9f4862bc38cb615180e986"
ClientSecret = "ffb9f165dc9f4d5b9502a51d5b55991d"
Redirect_URL = "https://example.com"



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=Redirect_URL,
        client_id=ClientID,
        client_secret=ClientSecret,
        show_dialog=True,
        cache_path="token.txt"
        )
)

user_id = sp.current_user()["id"]
date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")


response = requests.get(URL + date)
music_web_page = response.text
soup = BeautifulSoup(music_web_page, "html.parser")
# print(soup.prettify())


song_list = []
for song in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary"):
    song_list.append(song.text)
# print(song_names.text)
# playlist = date+'_playlist.txt'
#
# with open(f"{playlist}",mode="w") as file:
#     for song in song_list:
#         file.write(f"{song}\n")
year = date.split("-")[0]
song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False,)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)


