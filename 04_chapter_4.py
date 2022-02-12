# conver an image into Black and White

#import the labrary
import cv2 as cv
from cv2 import cvtColor

# original image 

img = cv.imread("resourses/img2.jpeg")
#original image convert into the gray image

gray = cvtColor(img, cv.COLOR_BGR2GRAY)

# gray image convert into the  binary image 

(thresh,binaryimg) = cv.threshold(gray,127,255,cv.THRESH_BINARY)

# Displaay image into different images

cv.imshow('Black and White Image',binaryimg)
cv.imshow('Gray image',gray)
cv.imshow('original',img)
# Delay window
cv.waitKey(0)
cv.destroyAllWindows()