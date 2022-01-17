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
from typing import List, Tuple

from multiprocessing import Value, Process

from pytube import Playlist, YouTube
from pytube.helpers import safe_filename
from pytube.exceptions import PytubeError


def chunk(l, n):
    """Yield n number of sequential chunks from l.
    
    From https://stackoverflow.com/a/54802737/14451421
    """
    l = list(l)
    d, r = divmod(len(l), n)
    for i in range(n):
        si = (d+1)*(i if i < r else r) + d*(0 if i < r else i - r)
        yield l[si:si+(d+1 if i < r else d)]


def download_video(args_tuple: Tuple[str, str, Value, int]):
    """Downloads the audio of a given YouTube video

    Args:
        args_tuple (Tuple[str, str, Value, int]): The full URL of the video to download, 
            the playlist title, the shared counter, and the number of videos in the playlist
    """
    video_url, playlist_title, counter, nb_videos = args_tuple

    try:
        yt = YouTube(video_url)
        yt.streams.get_by_itag(140).download(safe_filename(playlist_title))   
    except PytubeError as e:
        print(e, yt.title)

    with counter.get_lock():
        counter.value += 1

    print(f"Downloaded {counter.value}/{nb_videos} videos from playlist {playlist_title}", end="\r")


def download_playlist_chunk(args_list):
    for args_tuple in args_list:
        download_video(args_tuple)


def download_playlist(playlist: Playlist):
    """Downloads the audio of the videos from a given YouTube playlist

    Args:
        playlist_url (Playlist): The full URL of the playlist to download
    """

    video_urls = playlist.video_urls
    nb_videos = len(video_urls)
    nb_processes = min(8, nb_videos)

    shared_counter = Value('i', 0)

    split_args_list = chunk(
        zip(
                video_urls,
                (playlist.title for _ in range(nb_videos)),
                (shared_counter for _ in range(nb_videos)),
                (nb_videos for _ in range(nb_videos)),
            ),
        nb_processes
    )

    processes_list = [Process(target=download_playlist_chunk, args=(args,)) for args in split_args_list]

    print(f"Starting download of playlist {playlist.title}...", end="\r")

    for process in processes_list:
        process.start()

    for process in processes_list:
        process.join()

    print("Playlist " + playlist.title + " downloaded !" + " "*20)


def download_all_playlists(playlist_urls_list: List[str]):
    """Downloads the audio from all the playlists passed as arguments

    Args:
        playlist_urls_list (List[str]): A list of Youtube playlist URLs
    """
    playlist_list = [Playlist(url) for url in playlist_urls_list]

    for pl in playlist_list:
        download_playlist(pl)


def main():
    """Main function of the program, creates the CLI
    """
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

    download_all_playlists(playlist_urls_list)

    print(f"All {len(playlist_urls_list)} playlists downloaded !")


if __name__ == '__main__':
    main()
