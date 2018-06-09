
#imports file and shows YUV quad picture
# uses matplotilib,numpy,opencv



import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import numpy as np
import cv2

#parameters 

FILEIN = "/home/pi/Desktop/testimage1.jpg"



img_in= mpimg.imread(FILEIN)
                 
img_out = cv2.cvtColor(img_in, cv2.COLOR_BGR2YUV)                 


Y= img_out[:,:,0]
U= img_out[:,:,1]
V= img_out[:,:,2]



f, axarr = plt.subplots(2, 2)
axarr[0,0].imshow(img_in, cmap = cm.Greys_r)
axarr[0,0].set_title("YUV")
axarr[0,0].axis('on')

axarr[0,1].imshow(Y, cmap = cm.Greys_r)
axarr[0,1].set_title("Y")
axarr[0,1].axis('on')

axarr[1,0].imshow(U, cmap = cm.Greys_r)
axarr[1,0].set_title("U")
axarr[1,0].axis('on')

axarr[1,1].imshow(V, cmap = cm.Greys_r)
axarr[1,1].set_title("V")
axarr[1,1].axis('on')


# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)


plt.tight_layout()

plt.show()



