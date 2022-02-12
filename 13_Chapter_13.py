#basic functions or manuplation in open cv
import cv2 as cv
import numpy as np
# import or add a picure
img1 = cv.imread("resourses/img1.jpeg")
img = cv.imread("resourses/image1.jpg")

#resize img
resize_img = cv.resize(img,(53,53))
# Gray Img
Gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blures Image 

blurr_img = cv.GaussianBlur(img, (3,3),0)
# Black_White Image 

(thresh,binaryimg) = cv.threshold(Gray_img,127,255,cv.THRESH_BINARY)
# edge detection
edge_img = cv.Canny(img, 48,48)

#thikness of lines
mat_kernel = np.ones((3,3), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel),iterations=1)

# make a Thinner OutLine
ero_img = cv.erode(dilated_img,mat_kernel,iterations=1)


# Cropping Image we use numpy library not open cv
print("the size of the image is: ",img.shape)
cropped_img = img[0:500,150:400]

# show image on the display
cv.imshow('original_image', img)
cv.imshow('ReShape_image', resize_img)
cv.imshow('Gray_image', Gray_img)
cv.imshow('Blur_image', blurr_img)
cv.imshow('Edge', edge_img)
cv.imshow('Dilated_image', dilated_img)
cv.imshow('mat_kernal',mat_kernel)
cv.imshow('Ero_image',ero_img)
cv.imshow('Black_White Image',binaryimg)
cv.imshow("cropped_img",cropped_img)
#cv.imshow("frame",frame)
cv.waitKey(0)
cv.destroyAllWindows()