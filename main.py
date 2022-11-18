from pytube import YouTube, Playlist
import configparser, platform, os
from datetime import datetime as dt

config = configparser.ConfigParser()
config.read("config.cfg")
downloadpath = config["SAVEPATH"][platform.system()]

foldername = str(input("foldername > "))
if not os.path.exists(f"{downloadpath}/{foldername}"):
    os.mkdir(f"{downloadpath}/{foldername}")

SAVE_PATH = f"{downloadpath}/{foldername}"



URL = str(input("url > "))
match str(input("p/v > ")):
    case "p":
        is_playlist = True
        yt = Playlist(URL)
    case "v":
        is_playlist = False
        yt = YouTube(URL)
    case _:
        os.exit(1)

match str(input("v/a > ")):
    case "v":
        if is_playlist:
            for video in yt.videos:
                video_stream = video.streams.get_highest_resolution()
                video_stream.download(output_path=SAVE_PATH)
        else:
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path=SAVE_PATH)
    case "a":
        if is_playlist:
            for video in yt.videos:
                audioStream = video.streams.filter(only_audio=True).first()
                audioStream.download(output_path=SAVE_PATH)
        else:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=SAVE_PATH)