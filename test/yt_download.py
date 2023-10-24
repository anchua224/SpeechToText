# Credits: https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/
#  
# 
# 
# For MacOS, use this command to connect python to fix requests-html error
#       $ /Applications/Python\ 3.10/Install\ Certificates.command
#
# Program takes a YouTube video link and downloads it in the highest
# resolution as an MP4 file and saves it to the same file the program is in.
# Download contains both video and audio in the highest resolution the video
# is available in.
# 
# pytube documentation: https://pytube.io/en/latest/ 
# 
# Author: Ala Chua
# Version: 0.1
# Last Modified: 10/24/23
# 
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import os
import sys

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    # youtubeObject.filename = (youtubeObject.default_filename).replace(" ", "_")
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    os.rename(os.getcwd()+"/"+youtubeObject.default_filename, os.getcwd()+"/video/"+(youtubeObject.default_filename).replace(" ", "_"))
    print("Download is completed successfully")


def get_transcripts(link):
    id = link.split('=')[1]
    srt = YouTubeTranscriptApi.get_transcript(id)
    output_path = os.getcwd()+"/captions/"+id+".txt"
    print("Writing audio transcription to "+output_path+" ...")
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in srt:
            f.write(str(item) + "\n")
    print("Transcription is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
get_transcripts(link)