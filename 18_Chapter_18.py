# how to change a prospective of an image



from turtle import width
import cv2 as cv
from cv2 import imread
from cv2 import imwrite
import numpy as np

img = cv.imread("resourses/img1.jpeg")
print(img.shape)




point1 =  np.float32([[233,196],[82,471],[522,169],[715,482]])
height = 900
width = 800
height,width = 900,800
# Defineing a point

point2 = np.float32([[0,0],[800,0],[0,height],[width,height]])




matrix = cv.getPerspectiveTransform(point1,point2)
out_img = cv.warpPerspective(img,matrix,(width,height))
#out_img = cv.rectangle
cv.imshow("original",img)
cv.imshow("transformation",out_img)
imwrite('resourses/transform.png',out_img)
cv.waitKey(0)
cv.destroyAllWindows()





