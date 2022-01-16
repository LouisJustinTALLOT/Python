"""Small script to download all videos from a YouTube playlist

    Usage:
        Simply run the script with the playlist URLs as arguments, separated by spaces.
        ```python download_pytube_playlists.py <playlist_1_url> <playlist_2_url> ...```

        Alternatively, you can write all the playlist URLs to a file, and then pipe
        the contents of a file to the script:
        ```cat playlist_urls.txt | python download_pytube_playlists.py```
        
    Example:
        python download_pytube_playlists.py https://www.youtube.com/playlist?list=PLzPiaCaGenuqyZEkfAgUF_CNnNroKKKV7 https://www.youtube.com/playlist?list=PL18D36145BE009EDC
"""

__author__ = "Louis-Justin TALLOT"

# by @LouisJustinTALLOT (https://github.com/LouisJustinTALLOT)

import sys
from pytube import Playlist, YouTube
from pytube.helpers import safe_filename

from multiprocessing import Pool


def download_playlist(playlist):
    for i, video_url in enumerate(playlist.video_urls):
        print(f"Downloading video {i+1}/{len(playlist.video_urls)} of " + playlist.title, end="")
        print("\r", end="")

        yt = YouTube(video_url)

        try:
            stream = yt.streams.get_by_itag(140)
            stream.download(safe_filename(playlist.title))
        except Exception as e:
            print(e, yt.title)


    print("Playlist " + playlist.title + " downloaded !              ")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # pipe from a list of playlist urls
        playlist_urls_list = sys.stdin.read().split()
    else:
        # passed to argv
        playlist_urls_list = sys.argv[1:]


    playlist_list = [Playlist(url) for url in playlist_urls_list]

    with Pool(4) as p:
        p.map(download_playlist, playlist_list)

    print(f"All {len(playlist_list)} playlists downloaded !")