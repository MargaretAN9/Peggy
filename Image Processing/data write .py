import cv2
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import numpy as np




im = mpimg.imread("/home/pi/Desktop/test.jpg")

 
if __name__ == '__main__' :
 
    # Read image
    im = mpimg.imread("/home/pi/Desktop/testimage1.jpg")
     
    # Select ROI
    r = cv2.selectROI(im)
    print  r[1]

    
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    


 
    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)
