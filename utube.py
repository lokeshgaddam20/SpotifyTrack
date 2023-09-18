import pytube
import os
import main
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup


def get_video_url(youtube_url):
    """Downloads a list of songs from YouTube as MP3 based on the search query.

    Args:
        search_query: The search query to use to find the songs on YouTube.
    """

    # youtube_url = get_search_url(search_query)

    if youtube_url is not None:
        # Extract the video ID from the YouTube URL.
        video_id = re.findall(r"(?:v|=|&)[\w\-]+", youtube_url)[0]

        # Build the YouTube video URL.
        youtube_video_url = "https://www.youtube.com/watch?v=" + video_id

        print(youtube_video_url)
        # Download the song as MP3.
        get_path(youtube_video_url)
    else:
        print("Song could not be found on YouTube.")

def get_search_url(song_name):
    """Downloads a song from YouTube as MP3.

    Args:
        song_name: The name of the song to download.

    Returns:
        The path to the downloaded MP3 file.
    """
    encoded_search_query = urllib.parse.quote(song_name)

    # Get the YouTube URL for the song.
    youtube_url = "https://www.youtube.com/results?search_query=" + encoded_search_query
    
    print(youtube_url)
    # Make a request to the YouTube search URL.
    response = requests.get(youtube_url)

    # Parse the HTML response.
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first video result.
    video_result = soup.find("a", class_="ytd-video-renderer")
    print(video_result)

    # If the video result is not None, return the YouTube URL for the video.
    if video_result is not None:
        youtube_url = video_result["href"]
        return(youtube_url)
        # get_video_url(youtube_url)
    # Otherwise, return None.
    return "Hello"

def get_path(youtube_url):
# Download the song as MP3.
    youtube = pytube.YouTube(youtube_url)
    stream = youtube.streams.filter(only_audio=True).first()
    mp3_path = os.path.join(os.getcwd(), song_name + ".mp3")
    stream.download(mp3_path)
    print(mp3_path)
    return mp3_path

def download_songs(song_names):
    """Downloads a list of songs from YouTube as MP3.

    Args:
        song_names: A list of song names to download.
    """

    for song_name in song_names:
        get_search_url(song_name)


song_names = main.get_playlist_tracks("4p4mW2jaqtPWUOrldqOCwx")
download_songs(song_names)
