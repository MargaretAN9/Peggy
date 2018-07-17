# Process HDR pictures
# files and exp data from takeHDRpictures.py
#plots crf function
# creates HDR and tonemapped images:Robertson,Debevek,fusion_mertens
# see:https://docs.opencv.org/3.1.0/d2/df0/tutorial_py_hdr.html




import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping

# Loading exposure images into a list
img_fn = ["/home/pi/Desktop/img01.jpg", "/home/pi/Desktop/img02.jpg", "/home/pi/Desktop/img03.jpg", "/home/pi/Desktop/img04.jpg"]

filename="expfile.npy"

img_list = [cv2.imread(fn) for fn in img_fn]
exposure_times=np.load(filename)

#exposure_times = np.array([0.1, 1.0, 4.0, 8.0], dtype=np.float32)
print (exposure_times)


# Merge exposures to HDR image
merge_debvec = cv2.createMergeDebevec()
hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy())
merge_robertson = cv2.createMergeRobertson()
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy())

dimensions=hdr_debvec.shape
print (dimensions)

# Tonemap HDR image
tonemap1 = cv2.createTonemapDurand(gamma=2.2)
res_debvec = tonemap1.process(hdr_debvec.copy())
tonemap2 = cv2.createTonemapDurand(gamma=1.3)
res_robertson = tonemap2.process(hdr_robertson.copy())
print ("step2")


# Exposure fusion using Mertens
merge_mertens = cv2.createMergeMertens()
res_mertens = merge_mertens.process(img_list)



print ("step3")


# Convert datatype to 8-bit and save
res_debvec_8bit = np.clip(res_debvec*255, 0, 255).astype('uint8')
res_robertson_8bit = np.clip(res_robertson*255, 0, 255).astype('uint8')
res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')

cv2.imwrite("/home/pi/Desktop/ldr_debvec.jpg", res_debvec_8bit)
cv2.imwrite("/home/pi/Desktop/ldr_robertson.jpg", res_robertson_8bit)
cv2.imwrite("/home/pi/Desktop/fusion_mertens.jpg", res_mertens_8bit)

cv2.imwrite("/home/pi/Desktop/hdr_debvec.jpg", hdr_debvec)
cv2.imwrite("/home/pi/Desktop/hdr_robertson.jpg", hdr_robertson)



cal_debvec = cv2.createCalibrateDebevec()
crf_debvec = cal_debvec.process(img_list, times=exposure_times)
hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy(), response=crf_debvec.copy())
cal_robertson = cv2.createCalibrateRobertson()
crf_robertson = cal_robertson.process(img_list, times=exposure_times)
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy(), response=crf_robertson.copy())

# Obtain Camera Response Function (CRF)
gr = crf_debvec [:,:,0]
gb = crf_debvec [:,:,1]
gg = crf_debvec[:,:,2]



plt.figure(figsize=(10,10))
plt.ylim((0,14))
plt.xlim((0,256))


plt.plot(range(256),gr, color = "red" ,linestyle = "-")

plt.plot(range(256),gg, color = "green" ,linestyle = "-")
plt.plot(range(256),gb, color = "blue" ,linestyle = "-")

plt.ylabel('Calibrated Intensity')
plt.xlabel('Measured Intensity')

plt.show()




calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(img_list, exposure_times)

dimensions=responseDebevec.shape
print (dimensions)


cv2.imwrite("/home/pi/Desktop/hdr_debvec.jpg", hdr_debvec)
cv2.imwrite("/home/pi/Desktop/hdr_robertson.jpg", hdr_robertson)



