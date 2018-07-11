
"""

Creates exposure matrix 

Raspberry camera settings: Manual Raspberry Pi cameras settings are described in https://picamera.readthedocs.io/en/release-1.13/fov.html.
Some ot the major exposure control settings for the V2 camera are listed below:
--shutter_speed - controls exposure times, max length is 10 sec. Related to frame rate
--ISO - ISO controls sensitivity of the camera (by adjusting the analog_gain and digital_gain). Values are between 0 (auto) and 1600. The actual value used when iso is explicitly set will be one of the following values (whichever is closest): 100, 200, 320, 400, 500, 640, 800.
--AWB - Auto white balance controls (red, blue) gains and ‘balances’ the color.


matrix set for exposure time vs ISO
"""



from picamera import PiCamera
from time import sleep
from fractions import Fraction
import cv2
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



#set parameters/resolution and  framerate
#note Maximum framerate is determined by the minimum exposure time (INVERSE RELATED)
camera = PiCamera(resolution=(1280, 720),framerate=(.2),sensor_mode=3)


font = cv2.FONT_HERSHEY_SIMPLEX



#set wait time should be min 5 sec 

waitime = 3




#TEST PICTURE
print ("test picture ")
sleep(waitime)
camera.capture('/home/pi/Desktop/testexposure1.jpg')

#set X AXIS /horizontal #
#camera.shutter_speed =EXPOSURE TIME/time in microseconds
xrange = 5
etime = 100000
#set Y AXIS/number of ISO values
#ISO values between 0(auto),100,200,300,400,500,600,700,800
yrange = 5

#awb gains between 0.0 and 8.0 (typical gains between 0.9 and 1.9)
print ("Manual mode") 
print("X Y Time(microsecs) ISO")

for y in range (1,yrange):

    for x in range (1,xrange):


        if x == 1:
            #capture seed picture
            camera.shutter_speed = etime*x
            camera.iso = 100*y
            sleep(waitime)
            camera.capture('/home/pi/Desktop/testexposure.jpg')

    
            img = cv2.imread('/home/pi/Desktop/testexposure.jpg')
            cv2.putText(img,"{0},{1}".format(x,y),(5,50), font, 2, (0,255,0), 9, cv2.LINE_AA)

            img = cv2.resize(img, (0, 0), None, .25, .25)
      #     print ((x),(y),"{0:10s}".format(str(camera.shutter_speed/10000000)),(camera.iso))
            print ((x),(y),"{0:15s}".format(str(round(camera.shutter_speed))),(camera.iso)) 
        else:

            
            camera.shutter_speed = etime*x
            camera.iso = 100*y
            sleep(waitime)
            camera.capture('img1.jpg')
            img1 = cv2.imread('img1.jpg')
            cv2.putText(img1,"{0},{1}".format(x,y),(5,50), font, 2, (0,255,0), 9, cv2.LINE_AA)
            img1 = cv2.resize(img1, (0, 0), None, .25, .25)
            img = np.concatenate((img, img1), axis=1)
       #    print ((x),(y),"{0:10s}".format(str(camera.shutter_speed/10000000)),(camera.iso))
            print ((x),(y),"{0:15s}".format(str(round(camera.shutter_speed))),(camera.iso))  
           

    if y==1:
        img3=img
    else:
        
         img3= np.concatenate((img3, img), axis=0)
    
#colect auto mode last row

for x in range (1,xrange):
            
    if x == 1:
        #capture seed picture
        camera.shutter_speed = 0
        camera.iso = 0
        sleep(waitime)
        camera.capture('/home/pi/Desktop/testexposure3.jpg')
        print ("AUTO MODE")
    
        img4 = cv2.imread('/home/pi/Desktop/testexposure3.jpg')
        cv2.putText(img4,"auto",(5,50), font, 2, (0,255,0), 9, cv2.LINE_AA)

        img4 = cv2.resize(img4, (0, 0), None, .25, .25)

    else:
   
        camera.shutter_speed = 0
        camera.iso = 0
        sleep(waitime)
        camera.capture('img5.jpg')
        img5 = cv2.imread('img5.jpg')
        cv2.putText(img5,"auto",(5,50), font, 2, (0,255,0), 9, cv2.LINE_AA)
        img5 = cv2.resize(img5, (0, 0), None, .25, .25)
        img4 = np.concatenate((img4, img5), axis=1)

        print ((x),(y),"{0:15s}".format(str(round(camera.shutter_speed))),(camera.iso))  
            

img3 = np.concatenate((img3, img4), axis=0)

cv2.imwrite("/home/pi/Desktop/expmatrix.jpg", img3)
sleep(.1)


cv2.imshow("img3", img3)

#shut down steps else camera may lock/freeze

cv2.waitKey()
cv2.destroyAllWindows()
camera.framerate = 30
sleep(.3)
camera.close()
