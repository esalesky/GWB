#Girls Who Build
#Raspberry Pi Camera
#by Kristen Railey 04/17/16

#Picamera python resource: https://www.raspberrypi.org/documentation/usage/camera/python/README.md
import picamera #Import picamera library 
import RPi.GPIO as GPIO #Import general input/outputs on Raspberry pi
import time
from time import sleep
import pygame

GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Set up button input on pin 17
#Button is a pull-up resistor https://learn.sparkfun.com/tutorials/pull-up-resistors

WIDTH=1280
HEIGHT=1024
camera=picamera.PiCamera()

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))


camera.start_preview()
sleep(0.5)
#camera.preview_fullscreen


count=1

while True: #Checking if button has been pressed
    button_unpressed=GPIO.input(17) #Normally the button is unpressed
    
#    camera.start_preview()
  #  sleep(0.1)
    camera.capture('image.gif',format='gif',resize=(WIDTH,HEIGHT))
    pygame.display.update()
 #   camera.stop_preview()
    img=pygame.image.load('image.gif')
    screen.blit(img,(0,0))
    if button_unpressed==False:
        print ('Button Pressed')
    #    sleep(0.2)
        #Camera settings
        camera.sharpness = 0
        camera.contrast = 0
        camera.brightness = 50
        camera.saturation = 0
        camera.ISO = 0
        camera.video_stabilization = False
        camera.exposure_compensation = 0
        camera.exposure_mode = 'auto'
        camera.meter_mode = 'average'
        camera.awb_mode = 'auto'
        camera.image_effect = 'none'
        camera.color_effects = None
        camera.rotation = 0
        camera.hflip = False
        camera.vflip = False
        camera.crop = (0.0, 0.0, 1.0, 1.0)

        #Save picture
        camera.capture('image'+repr(count)+'.jpg')
   #     pygame.display.update()
        count+=1
    

