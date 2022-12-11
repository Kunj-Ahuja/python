from pytube import YouTube

url = 'https://youtu.be/qxIBWL05RoA'

yt = YouTube(url)
yt.streams.order_by('resolution').asc()
yt = yt.streams[0].download()
