#imports file and shows RGB quad picture
# uses matplotilib w/numpy


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm

import numpy as np

#parameters 

FILEIN = "/home/pi/Desktop/testimage1.jpg"


img = mpimg.imread(FILEIN)
                 

B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

f, axarr = plt.subplots(2, 2)
axarr[0,0].imshow(img, cmap = cm.Greys_r)
axarr[0,0].set_title("RGB")
axarr[0,0].axis('on')

axarr[0,1].imshow(B, cmap = cm.Greys_r)
axarr[0,1].set_title("Blue")
axarr[0,1].axis('on')

axarr[1,0].imshow(G, cmap = cm.Greys_r)
axarr[1,0].set_title("Green")
axarr[1,0].axis('on')

axarr[1,1].imshow(R, cmap = cm.Greys_r)
axarr[1,1].set_title("Red")
axarr[1,1].axis('on')


# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)


plt.tight_layout()

plt.show()



