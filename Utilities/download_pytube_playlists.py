"""Small script to download all videos from a YouTube playlist
By @LouisJustinTALLOT

Usage:
    If you have only a few playlists to download, you can simply
    run the script with the playlist URLs as arguments, separated by spaces.
    ```python download_pytube_playlists.py <playlist_1_url> <playlist_2_url> ...```

    In order to download more playlists, you can write all the playlist URLs
    to a (some) file(s), and then call the script with the name of the file(s)
    as arguments (you can even mix in youtube urls):
    ```python download_pytube_playlists.py playlist_urls.txt [playlist_urls_2.txt ...] [youtube playlist urls ...]```

Example:
    python download_pytube_playlists.py https://www.youtube.com/playlist?list=PLzPiaCaGenuqyZEkfAgUF_CNnNroKKKV7 https://www.youtube.com/playlist?list=PL18D36145BE009EDC
"""

__author__ = "Louis-Justin TALLOT"

# by @LouisJustinTALLOT (https://github.com/LouisJustinTALLOT)

import sys
from pytube import Playlist, YouTube
from pytube.helpers import safe_filename
from pytube.exceptions import PytubeError

from multiprocessing import Pool


def download_video(tuple_video_url_playlist_title):
    try:
        video_url, playlist_title = tuple_video_url_playlist_title
        yt = YouTube(video_url)
        yt.streams.get_by_itag(140).download(safe_filename(playlist_title))
    except PytubeError as e:
        print(e, yt.title)

def download_playlist(playlist):
    with Pool(processes=8) as pool:
        pool.map(download_video, zip(playlist.video_urls, [playlist.title]*len(playlist.video_urls)))

    print("Playlist " + playlist.title + " downloaded !              ")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # print the help
        print(__doc__)
        sys.exit()
    else:
        # passed to argv
        input_args = sys.argv[1:]

    playlist_urls_list = []
    # we can pass directly urls or a file containing urls
    for string in input_args:
        if ".txt" in string or ".md" in string or "youtube" not in string:
            try:
                with open(string, "r") as file:
                    playlist_urls_list.extend(file.read().split())
            except FileNotFoundError: # it was not a file
                pass
        else:
            playlist_urls_list.append(string)

    playlist_list = [Playlist(url) for url in playlist_urls_list]

    for playlist in playlist_list:
        download_playlist(playlist)

    print(f"All {len(playlist_list)} playlists downloaded !")