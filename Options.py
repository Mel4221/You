from shelve import Shelf
from traceback import print_tb
from unittest import result
from VideoDownloader import DownloadVideo
from console import Clear
import shutil
import os 
from FileReader import *
from SongDownloader import DownloadSong
from Searcher import FindSong

def FirstOptions():
          
          print("\n\n")
          print(" Please Type the option's Number then press Enter \n\n")
          print(" 1. Find Video Information")
          print(" 2. Download Song")
          print(" 3. Download Video")
          print(" 4. More Options...")
          print(" 5. Exit")

def Selector():
          #Clear()
          FirstOptions()
          
          option = input()
          if option == "1":
                    print("\n")
                    print("Please type the name of the video")
                    songName = input()
                    results = FindSong(songName)
                    print("The link for the video is :\n")
                    print(results)
                    return
          
          if option == "2":
                    print("\n")
                    print(" 1. with the name of the song")
                    print(" 2. with a list.txt of songs")
                    print(" 3. with a link")
                    print(" 4. with a list of links")
                    option = input()
                    if option == "1":
                              print("Please Type the name of the song")
                              name = input()
                              video = FindSong(name)
                              DownloadSong(video,"","")
                              return
                    if option == "2":
                              print("Drop or Drag the list.txt on the console please")
                              list = input()
                              Read(list)
                              return
                    if option == "3":
                              print("Paste the link on the console")
                              link = input()
                              DownloadSong(link,"","")
                    if option == "4":
                              print("Drop or Drag the list.txt on the console please")
                              links = input()
                              ReadLinks(links)
                              return
            
                    return
          
          """
          print(" 1. Find Video information ")
          print(" 2. Dowanload Songs Using a list.txt file")
          print(" 3. Check The list File")
          print(" 4. Download Song With a list of links")
          print(" 5. Download Song With a Single link")
          print(" 6. Download Video With a link")
          print(" 7. Download Video By the name")
          print(" 8. Download List of Videos")
          print(" 9. Delete All Downloads")
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
                    return
          if option == '3':
                    print("Type the name of the list or file.txt location if nothing it will be read list.txt as default")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.ReadCompleteFile(read)
                    else:
                              FileReader.ReadCompleteFile(read)
                    return
          if option == "4":
                    print("Type the name of the list or file.txt location if nothing it will be read list.txt as default")
                    read=input()
                    if read=="":
                              read = "list"
                              FileReader.ReadLinks(read)
                    
                    else:
                              FileReader.ReadLinks(read)
                    return
          if option == "5":
                    print("Paste the link from the video and  Press Enter")
                    link = input()
                    DownloadSong(link,"","")
                    return
                    
          if option == "6":
                    print("Paste the link from the video and  Press Enter")
                    link = input()
                    print("Which Resolution? , if you don't know just hit Enter")
                    resolution = input()
                    DownloadVideo(link,resolution)
                    return
                    
          if option =="7":
                    print("Type the name of the  video")
                    video = input()
                    print("Which Resolution? , if you don't know just hit Enter")
                    quality = input()
                    results = FindSong(video)
                    DownloadVideo(results,"")
                    return
                    
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
                              print("All Downloads have been Deleted  Deleted")
                              Selector()
                    else:
                              print("Deletion Was Cancelled")
                              Selector()
                    return
                    
          else:
                    Selector()
                    
                    
                    """