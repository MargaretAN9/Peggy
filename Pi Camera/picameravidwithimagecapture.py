#test camera program -tested with Raspberrty Pi camera v2.1
#program provides xx sec alignment preview and records jpg image 
# application: align spectrometer or focus microscope 
# annotates with filename and datetime

from picamera import PiCamera,Color
from time import sleep
import datetime as dt

#set filename/resolution/video time (sec)
#resolution size 4:3 options: (3280,2464),(1920,1080),(1640,1232),(640,480)


filename = '/home/pi/Desktop/testimage1.jpg'
SIZE = (3280,2464)
vidtime = 40

camera = PiCamera()

camera.start_preview(alpha=255)

#camera.annotate_background = picamera.Color('black')
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = filename + "     " + dt.datetime.now().strftime ('%Y-%m-%d %H:%M:%S')


#camera.start_preview()
sleep(vidtime)
 

camera.resolution = (SIZE)

camera.capture(filename)

camera.stop_preview()


