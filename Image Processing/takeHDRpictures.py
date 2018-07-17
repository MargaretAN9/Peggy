
#HDR collection program 
#record 4 pictures and exposure data for HDR processing
#shows all pictures to check image quality include auto exp + four exposures 




from picamera import PiCamera
from time import sleep
from fractions import Fraction
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#set parameters

font = cv2.FONT_HERSHEY_SIMPLEX
#camera = PiCamera(resolution=(1280,720 ))
#camera = PiCamera(resolution=(1280, 720),framerate=(Fraction (1,8)),sensor_mode=3)
camera = PiCamera(resolution=(1280, 720),framerate=(1),sensor_mode=3)

#set filenane to transfer exposure data

filename="expfile"

#set wait time should be min 5 sec 

waitime = 5

# xrange = how amny pictures 
xrange = 5
 
#Raspberry pi exptime is in microseconds , program desigend to accept time in sec and convert to microseconds
# enter times in sec


exposure_times = np.array([0.005, .01, .1, .3], dtype=np.float32)
np.save(filename, exposure_times)




#capture seed picture


camera.shutter_speed = 0
camera.iso = 0
sleep(waitime)
camera.capture('/home/pi/Desktop/testexposure.jpg')

    
img = cv2.imread('/home/pi/Desktop/testexposure.jpg')
#cv2.putText(img,"{0},{1}".format(x,y),(5,50), font, 2, (0,255,0), 9, cv2.LINE_AA)

img = cv2.resize(img, (0, 0), None, .25, .25)



print (exposure_times)
print (" number   exp time (sec)    exp time (microsceoned) ")

for i in range (1,xrange):
    
    sleep(waitime)
    camera.shutter_speed = int(1000000*(exposure_times[i-1]))
    print ("{0}           {1:.4}                    {2}".format(i,exposure_times[i-1],((camera.shutter_speed))))
    camera.iso = 100
   
   
    camera.capture('/home/pi/Desktop/img{0:02d}.jpg'.format(i))
    img1 = cv2.imread('/home/pi/Desktop/img{0:02d}.jpg'.format(i))
    img1 = cv2.resize(img1, (0, 0), None, .25, .25)
    img = np.concatenate((img,img1), axis=1)



cv2.imshow("img", img)



sleep(1)


cv2.waitKey(0)

cv2.destroyAllWindows()
camera.framerate = 30
sleep(.3)


camera.close()

