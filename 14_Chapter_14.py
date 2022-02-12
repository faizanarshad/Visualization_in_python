# How to Draw lines and shapes in python

#import library in the file

import cv2 as cv
from cv2 import FONT_HERSHEY_DUPLEX
import numpy as np

# Draw a canvas

img = np.zeros((600,600))
img1 = np.ones((600,600))


#Print size of the canvas
print("image the size of the canvs",img.shape)
#print(img)

colored_img = np.zeros((600,600,3),np.uint8)# color Channel addition

colored_img[:] = 255,0,255  #color key will change the color of canvas

colored_img[150:230,100:500] = 255,168,10

#adding lines

cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0) ,3 )# Crossed Line

cv.line(colored_img,(100,100),(300,300),(255,255,0),3 ) #Part line
#adding rectangles
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),3) # Draw 

cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),cv.FILLED)    # Filled
#adding Circle

cv.circle(colored_img,(300,300),50,(255,100,0),cv.FILLED)
#adding text
cv.putText(colored_img,"Python ka Chilla on Codanics Youtube Channel",(200,500),cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),1)

#cv.imshow("Black",img)
#cv.imshow("White",img1)
cv.imshow("colored_img",colored_img)

cv.waitKey(0)
cv.destroyAllWindows()
