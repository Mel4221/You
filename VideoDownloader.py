import moviepy.editor as mp
import regex
from pathlib import Path
import os
from console import Clear
from pytube import YouTube
from FileReader import * 
from Searcher import FindSong

Attemps = 0 

def DownloadVideo(videoLink,videoQuality):
          global Attemps
          #Clear()
          print("Downloading Video: "+videoLink)
          
    #videoQuality = "1080p"
          yt = YouTube(videoLink)
          if videoQuality=="":
                    videoQuality = "720p"
          else: 
                    videoQuality = videoQuality+"p"
          print("Downloading... "+yt.title+" Attemp: "+str(Attemps)) 
          #filter = yt.streams.filter(resolution=videoQuality)#.first().download(output_path="downloads/videos/", filename=yt.title+".mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
          try:
                    if videoQuality == "1080p":
                              
                              filter = yt.streams.filter(resolution=videoQuality).get_highest_resolution().download(output_path="downloads/videos/", filename=yt.title+".mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
                    
                    else:
                              filter = yt.streams.filter(resolution=videoQuality).first().download(output_path="downloads/videos/", filename=yt.title+".mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
          
          #.get_lowest_resolution().download(output_path="downloads/videos/", filename="video.mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
          
          
          
                    print("The Video has been downloaded Sucessfully "+yt.title)          
                    print("File Location: "+filter)
          except:
                    #global Attemps
                    Attemps = Attemps +1
                    if Attemps == 1:
                              print("Attempting again due to an error...")
                              DownloadVideo(videoLink,videoQuality)
                              return
                    if Attemps == 2:
                              print("Download Quality Set to Default '720p' Due to TOO MANY ATTEMPS")
                              print("Please try a lower Video Quality if the video keeps Attempting...")
                              DownloadVideo(videoLink,"")
                              return
                    if Attemps == 3:
                              print("Download Quality Set to Default '480p' Due to TOO MANY ATTEMPS")
                              print("Please try a lower Video Quality if the video keeps Attempting...")
                              DownloadVideo(videoLink,"480")
                              return
                    if Attemps == 4:
                              print("Download Quality Set to Default '360p' Due to TOO MANY ATTEMPS")
                              print("Please try a lower Video Quality if the video keeps Attempting...")
                              DownloadVideo(videoLink,"360")
                              return
                    if Attemps == 5:
                              print("Download Quality Set to Default '144p' Due to TOO MANY ATTEMPS")
                              print("Please try a lower Video Quality if the video keeps Attempting...")
                              DownloadVideo(videoLink,"144")
                              return
          return 
   
                    
          #<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
          #().download(output_path="downloads/video/", filename="video", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
 