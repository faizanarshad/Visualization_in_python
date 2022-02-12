#import libraries
import cv2 as cv
from cv2 import cvtColor

# load image
img = cv.imread('resourses/img1.jpeg')

#resize the image
img1 = cv.resize(img,(100,100))
#img1 = cv.resize(img,(800,600))

#conversion
gray_img = cvtColor(img,cv.COLOR_BGR2GRAY)
#displaycode
cv.imshow("Pahli image",img)
cv.imshow("Gray Image",gray_img)

#gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)

#delaycode
cv.waitKey(0)
cv.destroyAllWindows()