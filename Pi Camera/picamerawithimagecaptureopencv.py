# shows video and captures image using picmaera and opencv
# from https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/ 
#  
# press q to quit 

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#set filename/resolution
#resolution size 4:3 options: (1920,1088),(1640,1232),(640,480)
# note (3280,2464) provides 'out of resources' 

SIZE = (1640,1232)
FILEOUT = '/home/pi/Desktop/testimage1.jpg'
#cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (SIZE)
camera.framerate = 5
rawCapture = PiRGBArray(camera, size=(SIZE))
                                    
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	#resize to fit screen 
	resized = cv2.resize(image,None,fx=.7,fy=.7,interpolation = cv2.INTER_CUBIC)
        # show the frame
	cv2.imshow("window",resized)
	key = cv2.waitKey(1) & 0xFF 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.imwrite(FILEOUT,image)
camera.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
