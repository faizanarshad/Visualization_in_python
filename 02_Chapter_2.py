import numpy as np
import cv2 as cv


img = cv.imread('resourses/img1.jpeg')


img1 = cv.resize(img,(100,100))

cv.imshow("Pahli Image",img)
cv.imshow("Dusri image",img1)

gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


cv.waitKey(0)

cv.destroyAllWindows()