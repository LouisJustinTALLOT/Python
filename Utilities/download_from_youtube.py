"""
Small utility script to download YouTube playlists and videos
By @LouisJustinTALLOT

Usage:
    If you have only a few playlists or videos to download, you can simply
    run the script with the playlist URLs as arguments, separated by spaces.

    python download_from_youtube.py <playlist_url> <video_url> ...


    In order to download more playlists, you can write all the playlist
    and videos URLs to a (some) file(s), and then call the script with the
    name of the file(s) as arguments (you can even mix in youtube urls):

    python download_from_youtube.py urls.txt [urls_2.txt ...] [youtube playlist urls ...] [youtube videos urls]

Example:
    python download_from_youtube.py urls.txt

    python download_from_youtube.py https://www.youtube.com/playlist?list=PLzPiaCaGenuqyZEkfAgUF_CNnNroKKKV7 https://www.youtube.com/playlist?list=PL18D36145BE009EDC
"""

__author__ = "Louis-Justin TALLOT"

# by @LouisJustinTALLOT (https://github.com/LouisJustinTALLOT)

import sys
from typing import List, Tuple

from multiprocessing import Value, Process

from pytube import Playlist, YouTube
from pytube.helpers import safe_filename
from pytube.exceptions import PytubeError

PLAYLIST = "PLAYLIST"
VIDEO = "VIDEO"
ERROR = "ERROR"

def chunk(l, n):
    """Yield n number of sequential chunks from l.
    
    From https://stackoverflow.com/a/54802737/14451421
    """
    l = list(l)
    d, r = divmod(len(l), n)
    for i in range(n):
        si = (d+1)*(i if i < r else r) + d*(0 if i < r else i - r)
        yield l[si:si+(d+1 if i < r else d)]

def is_video_or_playlist(url: str) -> str:
    """Checks if the given url corresponds to a playlist or a video

    Args:
        url (str): The url to check

    Returns:
        str: "VIDEO" if the url is a video, "PLAYLIST" if it is a playlist, "ERROR" otherwise
    """
    if "playlist" in url:
        return PLAYLIST
    if "watch" in url:
        return VIDEO
    return ERROR


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


def download_playlist(args_tuple: Tuple[List[str], str]):
    """Downloads the audio of the videos from a given YouTube playlist
    or from a list of videos

    Args:
        args_tuple Tuple[List[str], str]: Tuple(list of video URLs, playlist title)
    """
    video_urls, title = args_tuple
    nb_videos = len(video_urls)

    if nb_videos == 0:
        return
    
    nb_processes = min(8, nb_videos)

    shared_counter = Value('i', 0)

    split_args_list = chunk(
        zip(
                video_urls,
                (title for _ in range(nb_videos)),
                (shared_counter for _ in range(nb_videos)),
                (nb_videos for _ in range(nb_videos)),
            ),
        nb_processes
    )

    processes_list = [Process(target=download_playlist_chunk, args=(args,)) for args in split_args_list]

    print(f"Starting download of playlist {title}...", end="\r")

    for process in processes_list:
        process.start()

    for process in processes_list:
        process.join()

    print("Playlist " + title + " downloaded !" + " "*20)


def download_all_playlists(playlist_urls_list: List[str]):
    """Downloads the audio from all the playlists passed as arguments

    Args:
        playlist_urls_list (List[str]): A list of Youtube playlist URLs
    """
    playlist_list = [Playlist(url) for url in playlist_urls_list]

    for pl in playlist_list:
        download_playlist((pl.video_urls, pl.title))


def download_all_individual_videos(videos_url_list: List[str]):
    download_playlist((videos_url_list, "Individual videos"))


def separate_videos_and_playlists(urls_list: List[str]) -> Tuple[List[str], List[str]]:
    """Separates the list of playlist URLs into a list of playlist URLs and a list of video URLs

    Args:
        playlist_urls_list (List[str]): The list of playlist URLs to separate

    Returns:
        Tuple[List[str], List[str]]: The list of playlist URLs and the list of video URLs
    """
    videos_url_list: List[str] = []
    playlist_urls_list: List[str] = []

    for url in urls_list:
        if is_video_or_playlist(url) == VIDEO:
            videos_url_list.append(url)
        elif is_video_or_playlist(url) == PLAYLIST:
            playlist_urls_list.append(url)
        else:
            print(f"Unknown url {url}")

    return playlist_urls_list, videos_url_list

def build_all_urls_list(input_args: List[str]):
    """Create the list of all the playlist URLs to download
    from the URLs and the text files passed as arguments

    Args:
        input_args (List[str]): The list of arguments passed to the script

    Returns:
        List[str]: the list of all the playlist URLs to download
    """
    playlist_urls_list: List[str] = []
    videos_urls_list: List[str] = []

    if "-h" in input_args[0] or "-help" in input_args[0]:
        print(__doc__)
        sys.exit(0)

    # we can pass directly urls or a file containing urls
    for string in input_args:
        if ".txt" in string or ".md" in string or "youtube" not in string:
            try:
                with open(string, "r") as file:
                    separated = separate_videos_and_playlists(file.read().split())
            except FileNotFoundError: # it was not a file
                pass
            else:
                playlist_urls_list.extend(separated[0])
                videos_urls_list.extend(separated[1])
        else:
            separated = separate_videos_and_playlists([string])
            playlist_urls_list.extend(separated[0])
            videos_urls_list.extend(separated[1])

    return playlist_urls_list, videos_urls_list


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

    playlist_urls_list, videos_urls_list = build_all_urls_list(input_args)

    download_all_playlists(playlist_urls_list)
    download_all_individual_videos(videos_urls_list)

    print(f"All playlists downloaded !")


if __name__ == '__main__':
    main()