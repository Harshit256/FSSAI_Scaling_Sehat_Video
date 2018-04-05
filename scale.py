#!/usr/bin/python3


from video_player import * #make sure video_player.py file is also on the same folder
from gpiozero import Button
from time import sleep
import pygame
import sys
import time

pygame.init()
pygame.mouse.set_visible(False)
infoObject = pygame.display.Info()
screen=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.NOFRAME)
print(str(infoObject.current_w) + " - " + str(infoObject.current_h));

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)


BASE_DIR = '/home/pi/Desktop/FSSAI_Scaling/'
#FILENAME_PRESSED =  'Video Portrait_5secs_Pressed.mp4'
FILENAME_PRESSED =  'Staring_1_1.mp4'
#FILENAME_PRESSED =  'Actual.mp4'


play_path_video_is_pressed = ''.join([BASE_DIR, FILENAME_PRESSED])

headphone_switch = 5
turnoff_switch = 2
exit_switch = 13
is_lifted_playing = False
first_time = True
is_pressed_playing = False

headphone_button = Button(headphone_switch)
turnoff_button = Button(turnoff_switch)
exit_button = Button(exit_switch)
play_pressed = Player(play_path_video_is_pressed)
play_pressed.play()
try:
  while True:
      pass
except KeyboardInterrupt:
	print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
	if play_pressed.status() == 'playing':
		print('play_lifted Video is running, terminating now!')
		play_pressed.stop()
		#load_image().stop()
		#play_pressed.kill()
	else:
		print('no Video running, exiting now')
	
	headphone_button.close()
	turnoff_button.close()
	exit_button.close()
	
	pygame.quit()
	
	pi_
