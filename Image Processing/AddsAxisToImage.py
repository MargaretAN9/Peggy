
#Displaying a Matplotlib Scale Image
#Imports a file and displays labels (x,y, title} and resolution tick marks
#requires matplotlib


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Enter input file name
filein = "/home/pi/Desktop/testimage1.jpg"


image = mpimg.imread(filein)
plt.imshow(image)

#plt.axis ("off")

plt.xlabel('Horizontal')
plt.ylabel('Vertical')


plt.title('Public Lab Raspberry Pi Test')

plt.show()
