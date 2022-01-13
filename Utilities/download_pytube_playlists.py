# by @LouisJustinTALLOT

import sys
from pytube import Playlist, YouTube

#"https://www.youtube.com/playlist?list=PL18D36145BE009EDC"
# https://www.youtube.com/playlist?list=PLzPiaCaGenuqyZEkfAgUF_CNnNroKKKV7

playlist = Playlist(sys.argv[1])



for video_url in playlist.video_urls:
    yt = YouTube(video_url)

    # print(list(yt.streams.filter(
    #     only_audio=True, file_extension='mp4'
    #     )))
    # print("")
    stream = yt.streams.get_by_itag(140)
    try:
        stream.download(playlist.title)
    except:
        print(yt.title)