import moviepy.editor as mp
import regex
from pathlib import Path
import os
from console import Clear
from pytube import YouTube
from FileReader import * 


def DownloadVideo(videoLink,videoQuality):
          Clear()
          print("Downloading Video: "+videoLink)
          

          #videoQuality = "1080p"
          yt = YouTube(videoLink)
          if videoQuality=="":
                    videoQuality = "720p"
          else: 
                    videoQuality = videoQuality+"p"
          print("Downloading... "+yt.title) 
          filter = yt.streams.filter(resolution=videoQuality).first().download(output_path="downloads/video/", filename=yt.title+".mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
          
          print("The Video has been downloaded Sucessfully")          
          print(filter)
          #<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
          #().download(output_path="downloads/video/", filename="video", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
          