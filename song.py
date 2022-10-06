import sys
import regex
from datetime import datetime
from pathlib import Path
from console import Clear
import os
from pytube import YouTube
#from builtins import str


Fails = 0
Completed = 0 
def Download(song, author, songName):
          try:
                    Video = song
                    down = "downloads"
                    downPath = Path(down)
                    if downPath.is_dir() == False:
                                        os.mkdir(downPath)

                    authorDir = Path(down+author)
                    if authorDir.is_dir() == False:
                                        os.mkdir(authorDir+"-Songs")

                    path = os.path.join(down, author)
                    #path = authorDir
                    yt = YouTube(Video)
                    print(yt.title)
                    yt.streams.filter()
                    print("Downloading "+songName+" From: "+author)
                    vtag = yt.streams.filter(only_audio=True).get_audio_only().itag
                    stream  = yt.streams.get_by_itag(vtag)
                    file = stream.download(output_path=path, filename=".mp3", filename_prefix=regex.sub(r'[^\w]', ' ',yt.title ),
                    skip_existing=False, timeout=10000, max_retries=10)
                    global Completed
                    Completed = Completed +1
                    PrintStatus('\033[92m')
                    print("File Location: "+file+" Downloaded Completed!!!")


          except:
                    global Fails
                    Fails = Fails + 1
                    now = datetime.now()
                    time = now.strftime("%H:%M:%S")
                    file1t = open("data/error"+time+".log","w")
                    file1t.writelines(song)
                    file1t.close()
                    PrintStatus('\033[91m')
                    
                    
                    
                    
def PrintStatus(color):
          print(color+"Completed: "+str(Completed)+" Fails: "+str(Fails))
          
          