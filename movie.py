from moviepy.editor import *
import pygame
import  os, sys
import shutil
from PIL import Image
import mplayer
import time


def resize(path, size):
    
    temp_path = os.path.join("files", "temp")
    
    if os.path.isdir(temp_path):
        shutil.rmtree( temp_path )
    
    os.mkdir(temp_path)
    
    for item in os.listdir(path):
           
            file = os.path.join(path, item)
            
            im = Image.open(file)
            f, e = os.path.splitext(file)
           
            imResize = im.resize(size, Image.ANTIALIAS)
            

            imResize.save(os.path.join(temp_path, os.path.split(f)[1] + 'resized.jpg'), 'JPEG', quality=90)
    return temp_path



def display_images(path, fps):

    sequence = ImageSequenceClip(path, fps)
    sequence.preview(fullscreen=True)
    shutil.rmtree( path )   # clean up
    pygame.quit()




def display_videos(path):     

     player = mplayer.Player()

     for file in os.listdir(path):
           video_file = os.path.join(path, file)
           player.loadfile(video_file)
           player.fullscreen = True
           t1 = time.time()
           while  not player.length: 
                 pass
           t2 = time.time()

           time.sleep(int(player.length + t2 - t1) )  



if __name__ == '__main__':


    pygame.display.set_caption('Video player')

    size = tuple(map(int,os.popen('xrandr | grep "*"').readline().strip().split()[0].split('x') ))

    print(size)
    images_path = os.path.join("files", "images")
    videos_path = os.path.join("files", "videos")

    temp_path = resize(images_path, size)

    pygame.display.set_mode(size)

    display_images(temp_path, fps=1)


    display_videos(videos_path)







