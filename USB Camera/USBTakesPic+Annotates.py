
#this python program collects  a picture  from a usb camera and provides a resolution scale
#tested with raspberry pi (stretch) and public lab usb camera
# program requires fswebcam which can be downloaded by using sudo apt-get install fswebcam
# see https://www.raspberrypi.org/documentation/usage/webcams/README.md for more info
# program uses matplotlib
# resolution set max resolution of the USB 2.0, PC camera from Public lab

import datetime
import time
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


filename = "/home/pi/Desktop/testimage1.jpg"



# date time display options
t = datetime.datetime.now()
                               
#DATE=$(date +"%Y-%m-%d_%H%M%S")

time.sleep(.5)

os.system('fswebcam --skip 2 -r 640x480 --no-banner --jpeg 100 filename') 
              

image = mpimg.imread("filename")
plt.imshow(image)

plt.xlabel(t)
plt.ylabel('Resolution (640x480)')


plt.title('Public Lab Test')

plt.show()
