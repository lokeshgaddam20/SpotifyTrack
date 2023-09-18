from dotenv import load_dotenv
import pytube
import os
import main
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup
import json



load_dotenv()


def get_search_url(song_name):
    """Downloads a song from YouTube as MP3.

    Args:
        song_name: The name of the song to download.

    Returns:
        The path to the downloaded MP3 file.
    """
    encoded_search_query = urllib.parse.quote(song_name)
    api_key = os.getenv('API_KEY')
    # api_key = "AIzaSyD7pnkRJVnng6rl8aljtSv2HhnlH6ujWag"
    
    youtube_url = f"https://www.googleapis.com/youtube/v3/search/?key={api_key}&type=video&part=snippet&maxResults=1&q={encoded_search_query} "

    
    response = requests.get(youtube_url)
    video_ids = list()

    video_items = json.loads(response.content)['items']
    
    for i in range(0,len(video_items)): 
        video_ids.append(video_items[i]['id']['videoId'])
        youtube_url = f"https://www.youtube.com/watch?v={video_ids[i]}"
        get_path(youtube_url,song_name)
  

def get_path(youtube_url,song_name):
# Download the song as MP3.
    youtube = pytube.YouTube(youtube_url)
    stream = youtube.streams.filter(only_audio=True).first()
    mp3_path = os.path.join(f'{os.getcwd()}/tracks', song_name)
    stream.download(mp3_path)
    print(mp3_path)

def download_songs(song_names):
    """Downloads a list of songs from YouTube as MP3.

    Args:
        song_names: A list of song names to download.
    """
    get_search_url(song_name)




# # Get the YouTube URL for the song.
    # youtube_url = "https://www.youtube.com/results?search_query=" + encoded_search_query
    
    # print(youtube_url)
    # # Make a request to the YouTube search URL.
    
    # # Parse the HTML response.
    # soup = BeautifulSoup(response.content, "html.parser")
    # # Find the first video result.
    # video_result = soup.find("div", class_="ytd-video-renderer yt-img-shadow")
    
      # # If the video result is not None, return the YouTube URL for the video.
    # if video_result is not None:
    #     youtube_url = video_result["href"]
    #     return(youtube_url)
    #     # get_video_url(youtube_url)
    # # Otherwise, return None.
    # return "Hello"
    
    
    
# def get_video_url(youtube_url):
#     """Downloads a list of songs from YouTube as MP3 based on the search query.

#     Args:
#         search_query: The search query to use to find the songs on YouTube.
#     """

#     # youtube_url = get_search_url(search_query)

#     if youtube_url is not None:
#         # Extract the video ID from the YouTube URL.
#         video_id = re.findall(r"(?:v|=|&)[\w\-]+", youtube_url)[0]

#         # Build the YouTube video URL.
#         youtube_video_url = "https://www.youtube.com/watch?v=" + video_id

#         print(youtube_video_url)
#         # Download the song as MP3.
#         get_path(youtube_video_url)
#     else:
#         print("Song could not be found on YouTube.")