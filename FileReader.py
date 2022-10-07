from wsgiref.validate import validator
from Logger import LogLinks,Log
from Searcher import FindSong
import  validators
from SongDownloader import DownloadSong,SetGoal,DownloadCount
import os

author = ""
SongsCount = 0
AuthorCount = 0


def Read(list):
    #try:
        print("Reading List")
        ReadCompleteFile(list)
      
        
        with open(list) as f:
            for line in f:
                if line.find(':') > 0:
                    global author 
                    author = line.replace(':', '')
                    print("Author: "+line)
                else:
                          if line.find(':') == 5:
                                    input("Wait Time") 
                          else:
                              songName = author.replace(':', '')+" "+line+" letra"
                              print(songName)
                              print("Finding Link...")
                              youtubeLink = FindSong(songName)
                              #Download(youtubeLink, author, line)
                              LogLinks(youtubeLink)
                              DownloadSong(youtubeLink, author, songName)
                    
                    
         
          
        return                  
   # except:
    #    print("Please try to put the list inside the list.txt file")
        #os.mkfifo("list.txt"
                 

def ReadCompleteFile(list):
  try:
        global AuthorCount
        global SongsCount
        #print("Reading List")
        #Log("LastStart","This was the last time that the application started")
        with open(list) as f:
            for line in f:
                if line.find(':') > 0:
                   
                    AuthorCount = AuthorCount+1
                    #print(line) 
                else:         
                    #print(line) 
                    SongsCount = SongsCount+1
       
            print("Songs: "+str(SongsCount)+" "+"Author: "+str(AuthorCount))
            SetGoal(SongsCount)
                   
  except:
        print("Please try to put the list inside the list.txt file")
        #os.mkfifo("list.txt")



def ReadLinks(list):
    try:
        print("Reading List")
        ReadCompleteFileLinks(list)
        
        with open(list) as f:
            for line in f:
                    
                    LogLinks(line)
                    DownloadSong(line,"","")    
          
        return                  
    except:
        print("Please try to put the list inside the list.txt file")
        #os.mkfifo("list.txt"
        
        
        
def ReadCompleteFileLinks(list):
  try:
        global AuthorCount
        global SongsCount
        #print("Reading List")
        #Log("LastStart","This was the last time that the application started")
        with open(list) as f:
            for line in f:
            
                    SongsCount = SongsCount+1
       
            print("Songs: "+str(SongsCount))
            SetGoal(SongsCount)
                   
  except:
        print("Please try to put the list inside the list.txt file")