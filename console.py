from os import system, name
import array as arr

def Clear():
   if name == 'nt':
      _ = system('cls')
   else:
           _ = system('clear')

          


n = 0          
def Input():

          while input() != "":          
                    val = input()
                    #text += val
                    global n
                    n = n+1
                    print(val+" "+str(n))
