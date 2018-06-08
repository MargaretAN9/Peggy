# displays video and records picture from  USB camera
#tested with Public Lab USB camera on Raspberry PI (stretch)  June 2018
# use 's' key to stop video and record image 
# code originally from https://gist.github.com/snim2/255151
# uses pygame library
# potential application - focus microscope with video and then store  image by pressing 's'


import pygame
import pygame.camera
from pygame.locals import *

# set parameters

DEVICE = '/dev/video0'
SIZE = (640, 480)

FILENAME = '/home/pi/Desktop/USBtestimage1.jpg'



def camstream():
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    screen = pygame.surface.Surface(SIZE, 0, display)
    capture = True
    while capture:
        screen = camera.get_image(screen)
        display.blit(screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
            elif event.type == KEYDOWN and event.key == K_s:
                pygame.image.save(screen, FILENAME)
                camera.stop()
                pygame.quit()
                return

    camera.stop()
    pygame.quit()
    return

if __name__ == '__main__':
    camstream()
