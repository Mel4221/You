from FileReader import Read,ReadCompleteFile
from Logger import Log
import sys
from pathlib import Path
import os 
from Options import Selector
from VideoDownloader import DownloadVideo

def CreateDataPath():
          path = Path("data")
          if path.is_dir()==False:
                    print("Creatting Data Folder")
                    os.mkdir("data")
def main():
          #ReadCompleteFile()
          #print("Please type the name of the list that you will be downloading from")
          #list = input()
          #Read(list)
          #Tester()
          path = Path("data")
          if path.is_dir()==False:
                    os.mkdir("data")
                    os.mkdir("data/downloads")
                    os.mkdir("data/downloads/videos/")
          args = sys.argv[1:]
          if len(args) > 0:
                    print(args)
          else:
                    #DownloadVideo("https://www.youtube.com/watch?v=Cn1YELnob5U","")
                    #CreateDataPath()
                    Selector("")
          
          Log(file="LastExit",matter="This was the last exit from the application",ext=".log")
          return 0
if __name__ == '__main__':
          main()
 
 
