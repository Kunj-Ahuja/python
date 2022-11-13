from pytube import YouTube

url = 'https://youtu.be/rNQpWlpeBxU'

yt = YouTube(url)
yt.streams.order_by('resolution').desc()
yt = yt.streams[0].download()
