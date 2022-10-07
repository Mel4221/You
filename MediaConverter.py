import moviepy.editor as mp


def ConvertVideo():
          video = input()
          if str(video).find(".mp4") < 0:
                    print("Not Valid Format")
                    return 1
          mp4 = mp.VideoFileClip(video)
          mp3 = str(video).replace(".mp4",".mp3")
          print(mp3)
          mp4.audio.write_audiofile(mp3)
ConvertVideo()