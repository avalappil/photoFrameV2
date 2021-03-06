#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime
import os, fnmatch
import pygame
from pygame.locals import *
import maestro
import time

path = '/home/pi/photoFrameV2'
#path = '.'
picPath = '/media/pi/PHOTOVIEWER/'
fotoframe = "./frame.jpg"
images = {}
maxImageCount = 0
imageIndexCount = 0
temp = 0
minTemp = 0
maxTemp = 0
tempDesc = ''
icon = ''
rotate = 90
mode = ''
prevImageOrientation = 0

def move(ac, speed, target):
    servo.setAccel(0, ac)
    servo.setSpeed(0, speed)
    servo.setTarget(0, target)

if (mode == ''):
   servo = maestro.Controller()
   prevImageOrientation = 0
   move(25, 5, 2680)
   time.sleep(60)
    
def readImages():
   listOfFiles = os.listdir(picPath) 
   pattern = "*.jpg"   
   global images
   global maxImageCount
   maxImageCount = 0
   for entry in listOfFiles:
      if fnmatch.fnmatch(entry, pattern):
          images[maxImageCount] = picPath + entry;
          maxImageCount += 1

def input(events):
    for event in events:
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.mouse.set_visible(True)
            pygame.quit()
            sys.exit(1)

def process():
   global mode
   global fotoframe
   global prevImageOrientation
   imageIndexCount = 0
   while True:
       #check for keyboard interupt
       input(pygame.event.get())
       #set background as black
       screen.fill((0,0,0))
      
       #reading the image
       if imageIndexCount >= maxImageCount:
          imageIndexCount = 0
          readImages()
       try:
          print (images)
          pic = pygame.image.load(images[imageIndexCount])
       except:
          print ("This is an error message!")

       imageIndexCount += 1
       W = pic.get_width()
       H = pic.get_height()
       print (H)
       print (W)
       if H > W:
           pic = pygame.transform.rotate(pic, rotate)
           imageOrientation = 1
           W = pic.get_width()
           H = pic.get_height()
           screen.fill((0,0,0))
       else:
           imageOrientation = 0
           screen.fill((0,0,0))
       ws = 0
       wh = 0
       
       rw = int(w - ws)/W
       rh = int(h - wh)/H
       pic = pygame.transform.smoothscale(pic, (int(W*rw), int(H*rh)))
       width = int(W*rw)
       height = int(H*rh)
       
       # display the photo
       

       if (imageOrientation == 0):
        if (mode == ''):
           if (prevImageOrientation == 1):
              pygame.display.update()
              prevImageOrientation = 0
           move(25, 5, 2680)
           time.sleep(8)
       else:
        if (mode == ''):
           if (prevImageOrientation == 0):
              pygame.display.update()
              prevImageOrientation = 1
           move(25, 5, 6350)
           time.sleep(8)
       screen.blit(pic, (int((int(w - ws)-int(width - ws))/2), int((int(h - wh)-int(height - wh))/2)))
       pygame.display.flip()
       time.sleep(5)

if __name__ == '__main__':
   pygame.init()
   modes = pygame.display.list_modes()
   print (modes)
   pygame.display.set_mode((1024, 768))
   screen = pygame.display.get_surface()
   time.sleep(2)
   screen = pygame.display.get_surface()
   tmp = screen.convert()
   (w, h) = (screen.get_width(), screen.get_height())
   flags = screen.get_flags()
   bits = screen.get_bitsize()
   screen = pygame.display.set_mode((w, h), flags ^ FULLSCREEN, bits)
   screen.blit(tmp, (0, 0))
   pygame.key.set_mods(0)
   (w, h) = (screen.get_width(), screen.get_height())
   myfont = pygame.font.SysFont("Arial", 80)
   myfontSmall = pygame.font.SysFont("Arial", 50)

   #serial setup
   if (mode == ''):
      path = '/home/pi/photoFrameV2'
   else:
      path = '.'
   picPath = '/media/pi/PHOTOVIEWER/'
   readImages()
   process()
