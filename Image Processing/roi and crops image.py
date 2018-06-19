
"""""
crops a portion of image

mouse click to draw rectangle 

press keyboard to show crop

"""""

 



import cv2
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import numpy as np

#parameters select file

FILEIN = "/home/pi/Desktop/microscope1.jpg"
                 

 
if __name__ == '__main__' :
 
    # Read image
    im = mpimg.imread(FILEIN)
     
    # Select ROI
    r = cv2.selectROI(im)
 

    
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    

 
    # Display cropped image
    cv2.imshow("Image", imCrop)
    print (r)
   
    cv2.waitKey(0)
