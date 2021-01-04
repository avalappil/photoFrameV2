#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime
import os, fnmatch
import pygame
from pygame.locals import *
import json
import serial


#path = '/home/pi/mirror'
path = '.'
picPath = path + '/wallpaper/'
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
mode = 'a'

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
    global ser
    for event in events:
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.mouse.set_visible(True)
            pygame.quit()
            sys.exit(1)

def process():
   global mode
   global fotoframe
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
          frame = pygame.image.load(fotoframe)
       except:
          print ("This is an error message!")

       imageIndexCount += 1
       #calculate the orientation
       FW = frame.get_width()
       FH = frame.get_height()
       W = pic.get_width()
       H = pic.get_height()
       print (H)
       print (W)
       if H > W:
           pic = pygame.transform.rotate(pic, rotate)
           imageOrientation = 1
           W = pic.get_width()
           H = pic.get_height()
           FW = frame.get_width()
           FH = frame.get_height()
           screen.fill((0,0,0))
       else:
           imageOrientation = 0
           screen.fill((0,0,0))
       #calculate the scaling ratios
       ws = 0
       wh = 0
       if imageOrientation == 0:
           ws=305
           wh=198
       else:
           ws=305
           wh=198

       frw = int(w)/FW
       frh = int(h)/FH    
       frame = pygame.transform.smoothscale(frame, (int(FW*frw), int(FH*frh)))
       fwidth = int(FW*frw)
       fheight = int(FH*frh)
       
       rw = int(w - ws)/W
       rh = int(h - wh)/H
       pic = pygame.transform.smoothscale(pic, (int(W*rw), int(H*rh)))
       width = int(W*rw)
       height = int(H*rh)
       
       # display the photo
       screen.blit(frame, (int((int(w)-fwidth)/2), int((int(h)-fheight)/2)))
       screen.blit(pic, (int((int(w - ws)-int(width - ws))/2), int((int(h - wh)-int(height - wh))/2)))

       if (imageOrientation == 0):
        if (mode == ''):
          ser.write(bytearray('h\n', 'UTF-8'))
       else:
        if (mode == ''):
          ser.write(bytearray('v\n', 'UTF-8'))
      
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
   screen = pygame.display.set_mode((w, h), flags, bits)
   screen.blit(tmp, (0, 0))
   pygame.key.set_mods(0)
   (w, h) = (screen.get_width(), screen.get_height())
   myfont = pygame.font.SysFont("Arial", 80)
   myfontSmall = pygame.font.SysFont("Arial", 50)

   #serial setup
   if (mode == ''):
      ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, xonxoff = False, rtscts = False, dsrdtr = False)
      path = '/home/pi/mirror'
   else:
      path = '.'
   picPath = path + '/wallpaper/'
   readImages()
   process()