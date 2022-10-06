from shelve import Shelf
from traceback import print_tb
from unittest import result
from VideoDownloader import DownloadVideo
from console import Clear
import shutil
import os 
import FileReader
from SongDownloader import DownloadSong
from Searcher import FindSong

def Selector():
          #Clear()
          print("\n\n")
          print("Please Type the option's Number then press Enter \n\n")
          print(" 1. Find Video information ")
          print(" 2. Dowanload Songs Using a list.txt file")
          print(" 3. Check The list File")
          print(" 4. Download Song With a list of links")
          print(" 5. Download Song With a Single link")
          print(" 6. Download Video With a link")
          print(" 7. Download Video By the name")
          print(" 8. Delete All Downloads")
          print(" 0. To Exit")
          option = input()
          if option == '0':
                    return
          if option == "1":
                    print("Please type the name of the video")
                    songName = input()
                    results = FindSong(songName)
                    print("The link for the video is :\n")
                    print(results)
                    return
                    
          if option == "2":
                    print("Type the name of the list or file.txt location if nothing it will be read list.txt as default ")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.Read(read)
                    else:
                              FileReader.Read(read)
          if option == '3':
                    print("Type the name of the list or file.txt location if nothing it will be read list.txt as default")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.ReadCompleteFile(read)
                    else:
                              FileReader.ReadCompleteFile(read)
          if option == "4":
                    print("Type the name of the list or file.txt location if nothing it will be read list.txt as default")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.ReadLinks(read)
                    
                    else:
                              FileReader.ReadLinks(read)
          if option == "5":
                    print("Paste the link from the video and  Press Enter")
                    link = input()
                    DownloadSong(link,"","")
                    
          if option == "6":
                    print("Paste the link from the video and  Press Enter")
                    link = input()
                    print("Which Resolution? , if you don't know just hit Enter")
                    resolution = input()
                    DownloadVideo(link,resolution)
          if option =="7":
                    print("Type the name of the  video")
                    video = input()
                    print("Which Resolution? , if you don't know just hit Enter")
                    quality = input()
                    results = FindSong(video)
                    DownloadVideo(results,"")
          if option == "":
                    Clear()
                    Selector()
          if option == '8':
                    print("You will not be able to undo this are you sure???")
                    sure = input("y / n \n")
                    if sure == "y":
                             
                              shutil.rmtree("downloads", ignore_errors=False, onerror=None)
                              os.mkdir("downloads")
                              Clear()
                              print("downloads Folder Deleted")
                              Selector()
                    else:
                              print("Deletion Was Cancelled")
                              Selector()
          else:
                    Selector()