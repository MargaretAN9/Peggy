
#The program  records a video demonstrating differnet  processing modes from a Raspberry Pi camera
#program tested on raspberry pi (strectch) with v2 camera (June 2018)
#Image is displayed at default settings  between modes for comparison.  Over 40 different settings are displayed
# see https://projects.raspberrypi.org/en/projects/getting-started-with-picamera for more info on picamera 
# video is recorded in h264 format, use omxplayer FILENAME.h264 to see  video on raspberry pi (use terminal) 
# application: program is useful to see preset processing options available with picamera
# see example demo videos at: https://www.youtube.com/watch?v=MCXqdq1Xw9A



from picamera import PiCamera
from time import sleep
from picamera import PiCamera, Color
from picamera import PiCamera, Color
import datetime as dt

# set parameters
FILENAME = '/home/pi/videodemo.h264'

camera = PiCamera()

camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
sleep(1)
camera.start_preview()

camera.start_recording(FILENAME)


camera.annotate_text = " Image displayed at default settings " 
sleep(5)


for i in range(100):
    camera.annotate_text = " Brightness : %s " % i
    camera.brightness = i
    sleep(0.1)

camera.brightness = 50
camera.annotate_text = " Image displayed at default settings "
sleep(3)


for i in range(100):
    camera.annotate_text = " Contrast: %s " % i
    camera.contrast = i
    sleep(0.1)

camera.contrast = 0
camera.annotate_text = " Image displayed at default settings "
sleep(3)


for effect in camera.AWB_MODES:
    camera.awb_mode = effect
    camera.annotate_text = " AWB Effect: %s " % effect
    sleep(5)


camera.awb_mode = 'auto'
camera.annotate_text = " Image displayed at default settings " 
sleep(3)



for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = " IMAGE Effect: %s " % effect
    sleep(5)

camera.image_effect = 'none'
camera.annotate_text = " Image displayed at default settings "
sleep(3)



for effect in camera.EXPOSURE_MODES:
    camera.exposure_mode = effect
    camera.annotate_text = " EXPOSURE MODES Effect: %s " % effect
    sleep(5)


camera.exposure_mode = 'auto'
sleep(2) 
camera.annotate_text = " Image displayed at default settings "
sleep(3)   



camera.stop_recording()    
camera.stop_preview()








