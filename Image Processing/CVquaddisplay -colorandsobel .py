#Quad video for real time image processing 
#program tested with Rasspberry PI 3B+.v2 NoIR camera
#sets up 3 windows -trackbar windows and video quad display showing camera settings, color filter and sobel edge detection  
# trackbar alss sets up blob detection see Satya Mallick https://www.learnopencv.com/tag/blob-detector/
#record video by setting file name, videowriter format and enable 'out.write(combined)' and 'write video' commands

#trackbars also feature blob detection

#requires opencv2 and picamera and scipy
#ESC to quit


import os
from scipy.signal import convolve2d as conv2
from scipy import ndimage
from skimage import color, data, restoration
from skimage.filters import sobel
import matplotlib.pyplot as plt

import time
import numpy as np
import cv2
import picamera
import picamera.array
from fractions import Fraction

def nothing(x):
    pass

#set camera control values
ISO_number = [100,200,320,400,500,640,800]
exposure_number = ['auto','off','night', 'nightpreview', 'backlight','spotlight', 'sports','snow','beach','verylong','fixedfps','antishake','fireworks']
effect_number = ['none','negative','solarize', 'colorswap','washedout','colorbalance','cartoon','sketch', 'denoise','emboss', 'oilpaint','hatch','gpen','pastel','watercolor','film','blur']


font=cv2.FONT_HERSHEY_SIMPLEX
#set up Windows

cv2.namedWindow("Public Lab")
blankimg= np.zeros((400,544,3),np.uint8)
cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)
cv2.namedWindow("Trackbars1", cv2.WINDOW_NORMAL)

# set up trackbars

cv2.createTrackbar ('Exposure Comp',"Trackbars",25,50,nothing)
cv2.createTrackbar ('Red Gain',"Trackbars",10,80,nothing)
cv2.createTrackbar ('Blue Gain',"Trackbars",14,80,nothing)
cv2.createTrackbar ('Frame Rate',"Trackbars",45,60,nothing)
cv2.createTrackbar ('Contrast',"Trackbars",100,200,nothing)
cv2.createTrackbar  ('Brightness',"Trackbars",50,100,nothing)
cv2.createTrackbar  ('Saturation',"Trackbars",100,200,nothing)
cv2.createTrackbar  ('Sharpness',"Trackbars",100,200,nothing)
cv2.createTrackbar  ('Exposure',"Trackbars",0,11,nothing)
cv2.createTrackbar  ('Effects',"Trackbars",0,16,nothing)
 
cv2.createTrackbar('Hstart','Trackbars',80,255,nothing)
cv2.createTrackbar('Hend','Trackbars',156,255,nothing)

cv2.createTrackbar('Sstart','Trackbars',80,255,nothing)
cv2.createTrackbar('Send','Trackbars',166,255,nothing)

cv2.createTrackbar('Vstart','Trackbars',50,255,nothing)
cv2.createTrackbar('Vend','Trackbars',144,255,nothing)

cv2.createTrackbar('MinArea','Trackbars1',200,4000,nothing)
cv2.createTrackbar('Circularity', 'Trackbars1',1,10,nothing)
cv2.createTrackbar('Convexity', 'Trackbars1',50,100,nothing)

cv2.createTrackbar('minThreshold', 'Trackbars1',10,200, nothing)
cv2.createTrackbar('maxThreshold', 'Trackbars1',200,2000, nothing)
cv2.createTrackbar('InertiaRatio', 'Trackbars1',50,100,nothing)

# SET UP colorspace values
Bstart,Gstart,Rstart = 0,0,0
Bend,Gend,Rend = 255,255,255

lower_range = np.array([Bstart,Gstart,Rstart], dtype=np.uint8)
upper_range = np.array([Bend,Gend,Rend], dtype=np.uint8)


#########################


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 1500
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01







# Create a VideoCapture object/used for video recording
cap = cv2.VideoCapture(0)

#Set video frame height 

height= 400
width=544
frame_width = 544
#frame_height = int(cap.get(4))
frame_height= 400

# Define the codec and create VideoWriter object.  Three choices available are avi,mpeg4 or h264

#The output is stored in 'outpy.avi' file.
#out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

#twice height and width

#set video writer MPEG4 =XVID
out = cv2.VideoWriter('/home/pi/Desktop/microscopequad1.mp4',cv2.VideoWriter_fourcc('X','V','I','D'), 10, (1088,800),1)
#set video writer (MJPG=avi) option
#out = cv2.VideoWriter('/home/pi/Desktop/NDVItestwithtrackbar.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1088,800),1)
#set video writer H264 option
#out = cv2.VideoWriter('/home/pi/Desktop/output.h264',cv2.VideoWriter_fourcc('H','2','6','4'), 10, (1088,800),1)

#def functions

def label(image, text):
    """
    Labels the given image with the given text
    """
    return cv2.putText(image, text, (0, 50), font, 2, (255,255,255),4)


def disp_multiple(im1=None, im2=None, im3=None, im4=None):

 #   height, width = im1.shape
 #note u may need to convert to RGB or GRAY depending on pprocessing

    combined = np.zeros((2 * height, 2 * width, 3), dtype=np.uint8)
    
  #    combined[0:height, 0:width, :] = cv2.cvtColor(im1, cv2.COLOR_GRAY2RGB)
 #   combined[height:, width:, :] = im1
    combined[0:height, 0:width, :] = im1
#    combined[height:, 0:width, :] = cv2.cvtColor(im2, cv2.COLOR_GRAY2RGB)
    combined[height:, 0:width, :] = im2
    combined[0:height:, width:, :] = im3
   #   combined[0:height, width:, :] =cv2.cvtColor(im3, cv2.COLOR_GRAY2RGB) 
 #   combined[height:, width:, :] = im4
    combined[height:, width:, :] =cv2.cvtColor(im4, cv2.COLOR_GRAY2RGB)

    return combined

def contrast_stretch(im):
    """
    Performs a simple contrast stretch of the given image, from 5-95%.
    """
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out


#begin camera collection

def run():
    with picamera.PiCamera() as camera:

        # Set the camera parameters
        x = 400
 #       camera.resolution = (int(640), x)
        camera.resolution = (544, x) 
        # Various optional camera settings below:
        camera.iso=400
        camera.framerate = 30
        camera.awb_mode = 'off'
        camera.exposure_mode = "off"
  #      camera.framerate = Fraction (1,6)
     #red/blue camera ratios from 0 to 8

        
 #       camera.awb_gains = (Red_gain,Blue_gain)

        # Need to sleep to give the camera time to get set up properly
        time.sleep(1)

        with picamera.array.PiRGBArray(camera) as stream:
            # Loop constantly
            while True:
                # Grab data from the camera, in colour format
                # NOTE: This comes in BGR rather than RGB, which is important
                # for later!
                camera.capture(stream, format='bgr', use_video_port=True)
                image = stream.array

                image1=image

                image2=image

                # Get the individual colour components of the image
 #               b, g, r = cv2.split(image)


                f = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

#placeholder for gaussian filter deblur (tested but not used)


#                blurred_f = ndimage.gaussian_filter(f, 3)
     
 #               filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)

 #               alpha = 10
 #               sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)

 
#                image1= contrast_stretch(image1)
 #               image1 = image1.astype(np.uint8)

# sobel filter need to convert using (ex.astype(float) and np.uint8
                ex=ndimage.sobel(f,axis=0,mode='constant')
                ey=ndimage.sobel(f,axis=1,mode='constant')
                edges = np.hypot(ex.astype(float),ey.astype(float))
                edges = edges.astype(np.uint8)



#color analysis 




                image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2HSV)

     
                Hstart = cv2.getTrackbarPos('Hstart', 'Trackbars')
                Hend = cv2.getTrackbarPos('Hend', 'Trackbars')

                Sstart = cv2.getTrackbarPos('Sstart', 'Trackbars')
                Send = cv2.getTrackbarPos('Send', 'Trackbars')
        
                Vstart = cv2.getTrackbarPos('Vstart', 'Trackbars')
                Vend = cv2.getTrackbarPos('Vend', 'Trackbars')

                lower_range = np.array([Hstart,Sstart,Vstart], dtype=np.uint8)
                upper_range = np.array([Hend,Send,Vend], dtype=np.uint8)

                

                mask = cv2.inRange(image, lower_range, upper_range)

                result = cv2.bitwise_and(image,image,mask = mask)
 


#Blob  detection 

  
                blob = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                

               

                # Setup SimpleBlobDetector parameters.
                params = cv2.SimpleBlobDetector_Params()
 
                # Change thresholds
                params.minThreshold = cv2.getTrackbarPos('minThreshold', 'Trackbars1');
                params.maxThreshold = cv2.getTrackbarPos('maxThreshold', 'Trackbars1');
 
# Filter by Area.
                params.filterByArea = True
                params.minArea = cv2.getTrackbarPos('MinArea', 'Trackbars1')
 
# Filter by Circularity
                params.filterByCircularity = True
                params.minCircularity = cv2.getTrackbarPos('Circularity', 'Trackbars1')/10
 
# Filter by Convexity
                params.filterByConvexity = True
                params.minConvexity = cv2.getTrackbarPos('Convexity', 'Trackbars1')/100
 
# Filter by Inertia
                params.filterByInertia = True
                params.minInertiaRatio = cv2.getTrackbarPos('InertiaRatio', 'Trackbars1')/100


                detector = cv2.SimpleBlobDetector_create(params)



# Detect blobs.
                keypoints = detector.detect(blob)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
                image_blob = cv2.drawKeypoints(blob, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 


 

                detector = cv2.SimpleBlobDetector_create(params)




#get info from Trackbars                

                Exposure_Comp=cv2.getTrackbarPos ("Exposure Comp","Trackbars")            
                Red_gain =cv2.getTrackbarPos ("Red Gain","Trackbars")  
                Blue_gain =cv2.getTrackbarPos ("Blue Gain","Trackbars")
                Frame_rate =cv2.getTrackbarPos ("Frame Rate","Trackbars")
                Contrast =cv2.getTrackbarPos ('Contrast',"Trackbars")   
                Brightness =cv2.getTrackbarPos ('Brightness',"Trackbars")
                ISO =cv2.getTrackbarPos ('ISO',"Trackbars")
                Exp=cv2.getTrackbarPos ('Exposure',"Trackbars")
                Saturation=cv2.getTrackbarPos ('Saturation',"Trackbars")
                Sharpness=cv2.getTrackbarPos ('Sharpness',"Trackbars")
                Effects=cv2.getTrackbarPos ('Effects',"Trackbars")

#scale camera settings 
 
                camera.exposure_compensation = Exposure_Comp-25                
                camera.awb_gains = (Red_gain/10,Blue_gain/10)
                camera.framerate = Frame_rate
                camera.contrast = Contrast-100
                camera.brightness = Brightness
                camera.exposure_mode = exposure_number[Exp]
                camera.saturation = Saturation-100
                camera.sharpness = Sharpness-100
                camera.image_effect = effect_number[Effects]




    
                # Label images
                label(image1, 'RGB')
  #              label(b, 'B')
  #              label(r, 'R')

#combine quad video


                # Combine ready for display
 #               combined = disp_multiple(blankimg,sharpened,result,image_blob)
                combined = disp_multiple(blankimg,result,image1,edges)


#use for recording  
 #               write video

 #put text
                cv2.putText(combined,"Exposure Compensation:",(10,25),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.exposure_compensation),(450,25),font,1,(256,256,256),2)

                cv2.putText(combined,"Blue",(10,55),font,1,(256,0,0),2)
                cv2.putText(combined,"/",(80,55),font,1,(256,256,256),2)
                cv2.putText(combined,"Red Gain:",(110,55),font,1,(0,0,256),2)
                cv2.putText(combined,str(Red_gain/10),(470,55),font,1,(0,0,256),2)
                cv2.putText(combined,"/",(450,55),font,1,(256,256,256),2)
                cv2.putText(combined,str(Blue_gain/10),(400,55),font,1,(256,0,0),2)

                cv2.putText(combined,"Frame Rate:",(10,85),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.framerate),(450,85),font,1,(256,256,256),2)

                cv2.putText(combined,"Contrast:",(10,115),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.contrast),(450,115),font,1,(256,256,256),2)

                cv2.putText(combined,"Brightness:",(10,145),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.brightness),(450,145),font,1,(256,256,256),2)

                cv2.putText(combined,"Saturation:",(10,175),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.saturation),(450,175),font,1,(256,256,256),2)

                cv2.putText(combined,"Sharpness:",(10,205),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.sharpness),(450,205),font,1,(256,256,256),2)

                cv2.putText(combined,"Exposure:",(10,235),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.exposure_mode),(355,235),font,1,(256,256,256),2)

                cv2.putText(combined,"Image Effect:",(10,265),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.image_effect),(355,265),font,1,(256,256,256),2)

                cv2.putText(combined,"ISO:",(10,295),font,1,(256,256,256),2)
                cv2.putText(combined,str(camera.iso),(355,295),font,1,(256,256,256),2)

                cv2.putText(combined,"Exposure Speed:",(10,325),font,1,(256,256,256),2)
                cv2.putText(combined,str(round(camera.exposure_speed/1000000,4)),(355,325),font,1,(256,256,256),2)
                

                cv2.putText(combined,"Analog Gain:",(10,355),font,1,(256,256,256),2)
                cv2.putText(combined,str(round(float(camera.analog_gain),2)),(355,355),font,1,(256,256,256),2)

                cv2.putText(combined,"Digital Gain:",(10,385),font,1,(256,256,256),2)
                cv2.putText(combined,str(round(float(camera.digital_gain),2)),(355,385),font,1,(256,256,256),2)

                cv2.putText(combined, "Color Filter", (10, 450), font, 2, (255,255,255),4)
  #              cv2.putText(combined, "R", (1020, 50), font, 2, (0,0,255),4)
                cv2.putText(combined, "Sobel", (580, 450), font, 2, (255,255,255),4)



# use for video recording


                out.write(combined)


                # Display
                cv2.imshow('Public Lab', combined)

                stream.truncate(0)

                #  press ESC to break 
                c = cv2.waitKey(7) % 0x100
                if c == 27:
                    break

    # cleanup or things will get messy
    cv2.destroyAllWindows()
    cap.release()
    out.release()

if __name__ == '__main__':
    run()

