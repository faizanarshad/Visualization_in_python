# conver an image into Black and White

#import the labrary
from cv2 import imshow, resize
from cv2 import imwrite
import cv2 as cv
from cv2 import cvtColor

# original image 

img = cv.imread("resourses/img2.jpeg")
#original image convert into the gray image

gray = cvtColor(img, cv.COLOR_BGR2GRAY)
# write the image into the resourses folder

imwrite('resourses/imagee_gray.jpeg',gray)

# gray image convert into the  binary image 

(thresh,binaryimg) = cv.threshold(gray,127,255,cv.THRESH_BINARY)
# change the size of the image 

binaryimg = resize(binaryimg,(500,500))
#write the image in the resourses folder
imwrite('resourses/binary.jpeg',binaryimg)
