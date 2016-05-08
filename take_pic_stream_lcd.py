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
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Set up button input on pin 17

WIDTH=256 #160-320
HEIGHT=160 #128-256
camera=picamera.PiCamera()

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))


camera.start_preview()
sleep(0.5)
#camera.preview_fullscreen


count=1

while True: #Checking if button has been pressed
    button_unpressed=GPIO.input(17) #Normally the button is unpressed
    button_unpressed_camera=GPIO.input(22) #Normally the button is unpressed

#    camera.start_preview()
  #  sleep(0.1)
#    stream=io.BytesIO()

    camera.capture('image.jpg')
 #   camera.stop_preview()
    img=pygame.image.load('image.jpg')
    img=pygame.transform.scale(img,(WIDTH,HEIGHT))
    screen.blit(img,(0,0))
    pygame.display.flip()

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
        text="Took a Selfie!"
        FONTSIZE=30
        font=pygame.font.Font(None,FONTSIZE)
        font_surf=font.render(text,True,pygame.Color(255,255,0))
        font_rect=font_surf.get_rect()
        font_rect.left=30
        font_rect.top=30
        screen.blit(font_surf,font_rect)
        pygame.display.update()
        count+=1
    if button_unpressed_camera==False:
        pygame.quit()

