'''
calibration test program 

'''

import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np
import os
 
imagefilename = "/home/pi/Desktop/test.jpg"
try:
     img=cv2.imread(imagefilename, 1)
except:
     print 'faild to load %s' % imagefilename
     quit()

usage='left click to draw a circle.\nright click to draw a rectangle.\n'
usage=usage+'press any key to exit.'
print(usage)



windowName="mouse"
cv2.namedWindow(windowName)

a=np.array([0,0])  
def onMouse(event, x, y, flags, param):
     """
        Mouse event callback function.
        left click -> draw circle
        right click -> draw rectangle
     """ 
     global a
     if event == cv2.EVENT_MOUSEMOVE:return 
 
     if event == cv2.EVENT_LBUTTONDOWN:
         center=(x,y)
         point1 = center
         radius=1
         color=(255,255,0)
         cv2.circle(img,center,radius,color)
         a=np.vstack([a,np.hstack([x,y])])
         
         
          
     if event == cv2.EVENT_RBUTTONDOWN:
         rect_start=(x-10,y-10)
         rect_end=(x+10,y+10)
         color=(100,255,100)
         cv2.rectangle(img,rect_start,rect_end,color)

     cv2.imshow(windowName,img)
     b=a[1:,:]
     print b
    
#setMouseCallback(...)
#    setMouseCallback(windowName, onMouse [, param]) -> None
cv2.setMouseCallback(windowName,onMouse)

cv2.imshow(windowName,img)
cv2.waitKey(0)
cv2.destroyAllWindows() 


