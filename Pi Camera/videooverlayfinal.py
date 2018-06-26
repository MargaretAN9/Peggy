'''
-calibration overlay program
-loads file, request user input and then creates transparent grid video overlay 
-user input is two mouse clicks and integer input (number of ruler divisions)
-requires picamera, opencv, matplotlib
-press q to exit from video

'''
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np
import os








#set parameters 
#set filename/resolution
#resolution size 4:3 options: (1920,1088),(1640,1232),(640,480)
# note (3280,2464) provides 'out of resources' 
SIZE = (640,480)

# provide calibration file /Output file address

calimagefilename = "/home/pi/Desktop/microscope1.jpg"
FILEOUT = '/home/pi/Desktop/testimage1.jpg'


# display parameters 

font = cv2.FONT_HERSHEY_SIMPLEX

opacity = .5  # sets grid transparency (.1 most transparent, 1 =no transparency) 


# losd cslibration file



try:
     img=cv2.imread(calimagefilename, 1)
except:
     print ('faild to load %s' % imagefilename)
     quit()

usage='left click to draw a circle.\nright click to draw a rectangle.\n'
usage='left click to draw a circle.\ndraw line by two left clicks along straight edge.\nright click to draw a rectangle.\n'
usage=usage+'press any key to exit.'
print(usage)

a=np.array([0,0])


# request mouse clicks

windowName="mouse"
cv2.namedWindow(windowName)


global dist
dist=0

def onMouse(event, x, y, flags, param):
     """
        Mouse event callback function.
        left click -> draw circle
        right click -> draw rectangle
     """ 
     
     global a
     global dist 
     
     if event == cv2.EVENT_MOUSEMOVE:return 
 
     if event == cv2.EVENT_LBUTTONDOWN:
         center=(x,y)
         point1 = center
         radius=10
         color=(255,255,0)
         cv2.circle(img,center,radius,color)
         a=np.vstack([a,np.hstack([x,y])])
         b=a[1:,:]
         
                
         if len(b) >=2:
             element = b[-2]
             elemenet2 = b[-1]
             
             cv2.line(img,(element[0],element[1]),(elemenet2[0],elemenet2[1]),(255,0,0),5)
             
             dist = cv2.norm(element,elemenet2)
            
        #  right click for square marker (this could be used if you wanted to select region of interest)
     if event == cv2.EVENT_RBUTTONDOWN:
         rect_start=(x-10,y-10)
         rect_end=(x+10,y+10)
         color=(100,255,100)
         cv2.rectangle(img,rect_start,rect_end,color)

     cv2.imshow(windowName,img)
     

#setMouseCallback(...)
#    setMouseCallback(windowName, onMouse [, param]) -> None
cv2.setMouseCallback(windowName,onMouse)



cv2.imshow(windowName,img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

print ("pixel distance=", dist)



#look at ruler and count divisions , typical value is 50
num = int(input ("enter number of divisions and press enter"))
print ("prepare for new measurement/ video turn on/press q to quit ") 

"""
#begin video capture
# initialize the camera and grab a reference to the raw camera capture
# press q to quit 

"""
camera = PiCamera()
camera.resolution = (SIZE)
camera.framerate = 5
rawCapture = PiRGBArray(camera, size=(SIZE))
                                    

 
# allow the camera to warmup
time.sleep(0.1)
 
# set scale using pixel distance form caibration picture
scale = dist/(num/10)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array 


	# show the frame/create overlay
	
	overlay = image.copy()
	start = 0
	while start < 640:
		cv2.line(overlay, (0, int(start)), (640, int(start)), (255, 255, 0), 1)
		cv2.line(overlay, (int(start),0), (int(start),640), (255, 255, 0), 1)		
		start += scale     

		
        # blend with the original:
	
	cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)

	# SET Text/manual input

	#cv2.putText(image,'Grid Scale = 100 microns',(225,470), font, .5, (255,255,255), 1, cv2.LINE_AA)
	#cv2.putText(image,'4X Objective',(510, 470), font, .5, (200,255,255), 1, cv2.LINE_AA)
	cv2.putText(image,'Public Lab Overlay Test',(5,470), font, .5, (255,255,255), 1, cv2.LINE_AA)	
	cv2.imshow("Frame", image)
	
	key = cv2.waitKey(1) & 0xFF
	
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break


cv2.imwrite(FILEOUT,image)

cv2.destroyAllWindows() 

camera.close()
cv2.waitKey(0)








