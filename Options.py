from shelve import Shelf
from traceback import print_tb
from unittest import result
from VideoDownloader import DownloadVideo
from console import Clear
import shutil
import os 
from FileReader import *
from SongDownloader import DownloadSong
from Searcher import FindSong, GetDetails

def FirstOptions():
          
          print("\n\n")
          print(" Please Type the option's Number then press Enter \n\n")
          print(" 1. Find Video Information")
          print(" 2. Download Song")
          print(" 3. Download Video")
          print(" 4. More Options...")
          print(" 5. Exit")

def Selector(option):
         
          FirstOptions()
          if option=="":
                    option = input()
        
          """
                    1-Option level
          #################################
          """
          if option == "1":
                    print("\n")
                    print("Please type the name of the video")
                    songName = input()
                    #print("The link for the video is :\n")
                    print("Video link: "+ GetDetails(songName)[0])
                    print("Video Title: "+ GetDetails(songName)[1])
                    print("Published by: "+ GetDetails(songName)[2])
                    time = int(GetDetails(songName)[3]/ 60)
                    print("Song Duration : "+str(time) +" Minutes" )
                    return
          
          """
                    2-Option level
          #################################
          """
          if option == "2":
                    print("\n")
                    print(" 1. with the name of the song")
                    print(" 2. with a list.txt of songs")
                    print(" 3. with a link")
                    print(" 4. with a list of links")
                    print(" 5. Go Back")
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
                              if list.find(".txt") <0:
                                        Clear()
                                        print("Invalid Type of file it must be a .txt file type")
                                        Selector("2")
                              else:
                                        Read(list)
                              return
                    if option == "3":
                              print("Paste the link on the console")
                              link = input()
                              DownloadSong(link,"","")
                    if option == "4":
                              print("Drop or Drag the list.txt on the console please")
                              links = input()
                              if links.find(".txt") <0:
                                        Clear()
                                        print("Invalid Type of file it must be a .txt file type")
                                        Selector("2")
                              else:
                                        ReadLinks(links)
                    if option == "5":
                              Selector("") #this just means go back to the main options
          """
                    3-Option level 
          #################################
          """    
          if option == "3":
                    print("\n")
                    print(" 1. with the name of the video")
                    print(" 2. with a link")
                    print(" 3. with a list of videos's names")
                    print(" 4. with a list of links")
                    print(" 5. Go Back")
                    option = input()
                    if option == "1":
                              print("Type the name of the  video")
                              video = input()
                              print("Which Resolution? , if you don't know just hit Enter")
                              quality = input()
                              results = FindSong(video)
                              DownloadVideo(results,quality)
                              return
                    if option == "2":
                              print("Paste the link on the console")
                              link = input()
                              
                              print("Which Resolution? , if you don't know just hit Enter")
                              quality = input()
                              DownloadVideo(link,quality) 
                    if option == "3":
                              print("Drop or Drag the list.txt on the console please")
                              list = input()
                              if list.find(".txt") <0:
                                        Clear()
                                        print("Invalid Type of file it must be a .txt file type")
                                        Selector("3")
                              else:
                                        print("Which Resolution? , if you don't know just hit Enter")
                                        quality = input()
                                        #results = FindSong(video)
                                        ReadVideoLinks(list,quality,True)
                                        #DownloadVideo(results,quality,True)
                              return
                    if option == "4":
                              print("Paste the link on the console")
                              link = input()
                              print("Which Resolution? , if you don't know just hit Enter")
                              quality = input()
                              ReadVideoLinks(link,quality,False)
                              return
                    if option == "5":
                              Selector("") #this just means go back to the main options
          """
                    4-Option level 
          #################################
          """
          if option == "4":
                    print("More Options")
                    print(" 1. Delete All Data")
                    option = input()
                    if option == "1":
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
                                        Selector("") #this just means go back to the main options
          
          """
                    5-Option level
          #################################
          """
          if option == "5":
                    return 0       
          
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