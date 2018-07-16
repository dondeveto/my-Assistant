"""wallpaper changer """

import ctypes
import os
import random
import time





def wallpaper(moment):
    
    try:
        d = os.path.dirname(__file__)
        drive = d
        folder = "{}//wallpaper//".format(d)
        

        x = os.listdir(folder)
        img =random.choice( x )

        image_path = "{}/wallpaper/{}".format(d, img)
        
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
        return("The wallpaper has been changed")
    except:
        return("I was unable to change the wallpaper my appologies")
    
       
######  CREATES FOLDER IF NOT EXIST            
##newpath = r'C:\Program Files\arbitrary' 
##if not os.path.exists(newpath):
##    os.makedirs(newpath)



wallpaper(3)

############### GETS SCREEN SIZE
##import ctypes
##user32 = ctypes.windll.user32
##screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


#################  GETS IMAGE SIZE
##from PIL import Image
##im=Image.open(filepath)
##im.size # (width,height) tuple




       



