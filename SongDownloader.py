import moviepy.editor as mp
import regex
from pathlib import Path
import os
from pytube import YouTube
from Logger import Log
from song import Completed
""" from FileReader import * """


DownloadDir = Path("downloads")
DownloadCount = 0
Completed = 0 
Fail = 0 
Attemps = 1
def DownloadSong(song, authorName, songName):
       """   try:"""      
          
       videoLink = song #FindSong("yo soy tu gominola")
       yt = YouTube(videoLink)
       if songName == "" or authorName == "":
              print("Downloading a Direct link...")
              songName = yt.title
              authorName = "links"
              
       clearName = regex.sub(r'[^\w]', ' ',authorName)
       author = clearName.replace(" ","_")
       fileName = "temp.mp4" #regex.sub(r'[^\w]', ' ',yt.title)
       
       authorDir = Path(author)
       path = str(DownloadDir)+"/"+str(authorDir)
       pathWithFile = path+"/"+fileName
         
          
       if DownloadDir.is_dir()==False :
              print("Creatting Download Folder")
              try:
                            os.mkdir(DownloadDir)
              except:
                            print("Already Created..........................")
                        
       if authorDir.is_dir()==False :
              print("Creatting Author Folder '"+str(author)+"'")
              try:
                            os.mkdir(path)
              except:
                            print("Already Created..........................")

          #Download File
       tempFile = Path(path+"/"+fileName)
       
       if tempFile.is_file()==True:
              try:
                            os.remove(pathWithFile)
              except:
                            print("Everything Clear.............................")
       PrintStatus(authorName)
       print("Downloading Video "+songName)
       filter = yt.streams.filter(file_extension='mp4').get_lowest_resolution().download(output_path=path+"/", filename=fileName, filename_prefix="",
              skip_existing=True, timeout=10000, max_retries=10)
       
       print("Downloaded Completed!!!")
       print(filter)
       print("Converting mp4 to mp3")
          
       mp4 = mp.VideoFileClip(pathWithFile)
       
       mp3 = regex.sub(r'[^\w]', ' ',yt.title).replace(" ","_")#making the name a safe name for any system
       print(mp3)
       mp4.audio.write_audiofile(path+"/"+mp3+".mp3")
       print("Convertion Completed!!!")
       """ print("Deleting Temporal File")
              os.remove(pathWithFile)"""
       print("Completed!!!")
       global DownloadCount
       DownloadCount = DownloadCount - 1
       global Completed 
       Completed = Completed + 1 
       #os.makedirs("downloads/temp")
          
       """except:
              global Fail,Attemps
              Fail = Fail + 1 
              print("Error While downloading a song or converting it")
              Log("DownLoadError",song+"|"+authorName+"|"+songName+"|",".txt")
              if Attemps < 3:
                     Attemps = Attemps + 1
                     DownloadSong(song, authorName, songName)
              else:
                     
                     return
       """
          


def PrintStatus(authorName):
          global Fail,DownloadCount,Completed,Attemps
         
          print("Status: Completed: "+str(Completed)+" Fail: "+str(Fail)+" Missing: "+str(DownloadCount)+" Attemps: "+str(Attemps))
          print("Current Author: "+authorName)
        
def SetGoal(goal):
          global DownloadCount
          DownloadCount = goal
          
          

          
          
     