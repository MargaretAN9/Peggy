
# Project Title:  Computer Vision enhancements for Raspberry Pi based Public Lab Science Projects

## Program Description:
The project developed  a series of modular python programs that support different Public Lab (https://publiclab.org/) imaging and spectrum measurement toolkits. The programs enable near real time OpenCV computer vision (CV) measurements of images or spectra. The CV measurements can be used to improve instrument performance (feedback that controls lighting amplitude or camera array exposure times) or assist calibration.  

Complete Google Summer of Code proposal available at :  https://publiclab.org/notes/MaggPi/03-20-2018/gsoc-proposal-computer-vision-enhancements-for-raspberry-pi-based-public-lab-science-projects

Code demonstrations  can be seen at https://publiclab.org/profile/MaggPi.

Video demos at : https://www.youtube.com/channel/UCbyyYOlNo87CXJ39h3wqXZA

## Develpopment Environment: 
All programs were tested with a Raspberry Pi 3B+ (stretch), OpenCV2, Raspberry Pi NoIR camera (or webcam) and Python 3.5 

## Program organization:
Programs are divided into the three categories (Picamera, USB and Image  Processing) that are based on different ways the image is acquired.  Multiple  software routines have been posted to accommodate different levels of experience. For example, a beginner will probably just want to capture an image, a slightly more experienced user will want to capture and annotate the image, and an experienced programmer will want to capture, annotate and process the image. (with opencv). All code is available at: https://github.com/MargaretAN9/Peggy  Code application can be seen at https://publiclab.org/profile/MaggPi.  

# Prerequisites 
Program requirements are listed on the import section of the program but here is a complete list of download instructions or install resources:

 -Picamera -  https://picamera.readthedocs.io/en/release-1.13/install.html
 -OpenCV2 https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
 -Matplotlib:   sudo apt-get build-dep python-matplotlib
 -Omxplayer (to display h264 videos of raspberry pi): sudo apt-get install omxplayer
 -SciPy :   sudo apt-get install python3-scipy
 -fswebcam: USB camera driver   -sudo apt-get install fswebcam
 -Also don’t forget  to update before downloading: sudo apt-get update and sudo apt-get dist-upgrade


###References
-picamera documentation -  Must read for anybody working with Raspberry Pi camera:
https://picamera.readthedocs.io/en/release-1.13/

-OpenCV tutorial sites-  Great online tutorials, most with step by step instructions.
-Adrian Rosebrock -  https://www.pyimagesearch.com/author/adrian/
-Satya Mallick -  https://www.learnopencv.com/about/
-Sergio Canu - https://pysource.com/

-Dr. Robert Wilson’s git hub page https://github.com/robintw/RPiNDVI has super  python coding about a host of environmental applications.  

-Katherine Scott (SimpleCV)  and Ladyada(ADAfruit) – Their videos gave me confidence I could do this stuff. 


###Software programs: 


Image Processing: Programs that process digital images in various ways

3dRGBmeshgrid.py
Creates 3d RGB plot/meshgrid.  Shows both RGB quad and meshgrids.
AddsAxisTolmage.py
Displaying a Matplotlib Scale Image.  Imports a file and displays labels (x,y, title} and resolution tick marks.  Requires matplotlib.
HSV.py
Imports file and shows HSV quad picture.  Uses matplotilib,numpy,opencv.

HSVcolortrachbar.py
Sets up trackbars to analyze image in HSV colorspace.  Shows trackbar mask, input and result.  Esc to quit #red typical H: 156-179, S:117-255, V: 98-255 #green typical H: 40-85, S:255-255, V: 19-255.  Blue typical H: 100-127, S:107-255, V: 152-255.  Yellow typical H: 15-35, S:77-255, V: 165-255
RGBquad.py
Imports file and shows RGB quad picture.  Uses matplotilib w/numpy.
YUVQuad.py
Imports file and shows YUV quad picture.  Uses matplotilib,numpy,opencv.
histogram3.py
Plot histograms #calculates grayscale/color and 2d histograms.  See https://lmcaraig.com/image-histograms-histograms-equalization-and-histograms-comparison/.
roi and crops image.py
Crops a portion of image.  Mouse click to draw rectangle.  Press keyboard to show crop.
takeHDRpictures.py
HDR collection program.  Record 4 pictures and exposure data for HDR processing.  Shows all pictures to check image quality include auto exp + four exposures.

NDVI Red/Gain optimization program
Program displays (and records) an RGB//B/NDVI(fastie)/NDVI(Jet) quad video.  Tested with a Raspberry Pi NoIR camera with blue filter. Trackbars select gain settings.  Program opens at zero gain so need to move red/lude ,gain  .5/.5 to see first images.  NDVI equations from https://github.com/robintw/RPiNDVI/blob/master/ndvi.py
Program requires loading colorbars (jetcolorbar.jpg and NDVIcolormap.jpg) posted at https://github.com/MargaretAN9/Peggy


Pi Camera: Programs that take videos or pictures with a Raspberry Pi Camera.
PiCameraEffectsShow.py
The program displays different processing modes from a Raspberry Pi camera #program tested on raspberry pi (strectch) with v2 camera (June 2018).  Image is displayed at default settings between modes for comparison. Over 40 different settings are displayed.  See https://projects.raspberrypi.org/en/projects/getting-started-with-picamera for more info on picamera.  Application: program is useful to see preset processing options available with picamera.  See example demo videos at: https://www.youtube.com/watch?v=MCXqdq1Xw9A.
PiCameraEffectsVid.py
The program records a video demonstrating different processing modes from a Raspberry Pi camera #program tested on raspberry pi (strectch) with v2 camera (June 2018).  Image is displayed at default settings between modes for comparison.  Over 40 different settings are displayed.  See https://projects.raspberrypi.org/en/projects/getting-started-with-picamera for more info on picamera.  Video is recorded in h264 format, use omxplayer FILENAME.h264 to see video on raspberry pi (use terminal).  Application: program is useful to see preset processing options available with picamera.  See example demo videos at: https://www.youtube.com/watch?v=MCXqdq1Xw9A
exposuremosaic.py
Creates exposure matrix Raspberry camera settings: Manual Raspberry Pi cameras settings are described in https://picamera.readthedocs.io/en/release-1.13/fov.html. Some at the major exposure control settings for the V2 camera are listed below: 
--shutter_speed - controls exposure times, max length is 10 sec. Related to frame rate.
--ISO - ISO controls sensitivity of the camera (by adjusting the analog_gain and digital_gain). Values are between 0 (auto) and 1600. The actual value used when iso is explicitly set will be one of the following values (whichever is closest): 100, 200, 320, 400, 500, 640, 800. 
--AWB - Auto white balance controls (red, blue) gains and ‘balances’ the color.
Matrix set for exposure time vs ISO.
picameravidwithimagecapture.py
test camera program -tested with Raspberrty Pi camera v2.1.  Program provides xx sec alignment preview and records jpg image.  Application: align spectrometer or focus microscope.  Annotates with filename and datetime.
picameravidwithimagecapturecv.py
Shows video and captures image using picmaera and opencv.  From https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/.  Press q to quit
videooverlayfinal.py
Calibration overlay program.  Loads file, request user input and then creates transparent grid video overlay.  User input is two mouse clicks and integer input (number of ruler divisions).  Requires picamera, opencv, matplotlib.  Press q to exit from video
USB Camera: Programs that take videos or pictures with a USB Camera.
USBTakesPic+Annotates.py 
Uses the connected USB Camera to take a photo and annotate said image with a resolution scale vis matplotlib.  Requires fswebcam which can be downloaded by using sudo apt-get install fswebcam
USBVidWithImageCapture.py
Displays video and records picture from USB camera #tested with Public Lab USB camera on Raspberry PI (stretch) June 2018. Use 's' key to stop video and record image.  Code originally from https://gist.github.com/snim2/255151.  Uses pygame library.  Potential application - focus microscope with video and then store image by pressing 's'
