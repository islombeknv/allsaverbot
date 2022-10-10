import requests
from pytube import YouTube
import wget
import uuid


def dowload_video(url, ql):
    yt = YouTube(url)
    media_id = uuid.uuid4().fields[-1]
    yt.streams.filter().get_by_itag(ql).download("media", f"{media_id}.mp4")
    return f"{media_id}.mp4"


def dowload_audio(url):
    yt = YouTube(url)
    audio_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
    return f"{audio_id}.mp3"


def likedownload(url):
    return requests.get(f'https://foydaliapi.uz/like.php?url={url}').json()[0]['url']


def pinterest(data):
    url = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"
    querystring = {"url": f"{data}"}

    headers = {
        "X-RapidAPI-Key": "2b4cda67a6msh04211a14f7e237dp1186f2jsn457190f43909",
        "X-RapidAPI-Host": "pinterest-video-and-image-downloader.p.rapidapi.com"
    }

    return requests.request("GET", url, headers=headers, params=querystring).json()

