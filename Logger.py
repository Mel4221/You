from datetime import datetime
       
def LogLinks(links):
          
          file1 = open("data/Links.log", "a")  # append mode
          L = [links+"\n"]
          file1.writelines(L)
          file1.close()
          


def Log(file,matter,ext):
        
        
          file1 = open("data/"+file+ext,"a")
          L = [matter+"\n"]
          file1.writelines(L)
          file1.close()
          

