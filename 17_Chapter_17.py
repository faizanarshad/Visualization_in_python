#joining two images 


import cv2 as cv
import numpy as np

img = cv.imread("resourses/img1.jpeg")

# stacking same Image

# 1-horizantal stack
hor_img = np.hstack((img,img))

ver_stack = np.vstack((img,img))


#cv.imshow("horizantal_image",hor_img)
cv.imshow("horizantal_image",ver_stack)

#you can only stack images with same shape (width,height.color channel)
# we can not resize the stack image (function)
# same number of channels np function
(600,500,3)

#you have to define a function to stack multiple images of different sizes and tunes

cv.waitKey(0)
cv.destroyAllWindows()