print('''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█''')
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import pytube as pt
from youtubesearchpython import VideosSearch

cId= 'a5f0636145e34e9abc809ba8b438cf6f'
cSecret = '139231d3247047209de6b9fa0898f4b3'

client_credentials_manager = SpotifyClientCredentials(client_id=cId, client_secret=cSecret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlistlink = input('Enter spotify playlist link: ')
playlist_URI = playlistlink.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

tracks = []
for track in sp.playlist_tracks(playlist_URI)["items"]:
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    tracks.append(track_name + ' ' + artist_name)

links=[]
for i in tracks:
    videosSearch = VideosSearch(i) 
    if len(videosSearch.result()['result']) < 1:
        pass
    links.append(videosSearch.result()['result'][0]['link'])

print(f'Total tracks: {len(links)}')

for link in links:
    yt = pt.YouTube(link)
    t = yt.streams.filter(only_audio=True)
    a = t[0].download()
    os.rename(a, a.replace('.mp4','.mp3'))
    print(f'{links.index(link)}: Downloaded')