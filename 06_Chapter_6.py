#reading a video 

#import a library 
import cv2 as cv

# load a video into the code
cap = cv.VideoCapture('resourses/video.mkv')
#cap = cv.cvtColor(cap,cv.COLOR_BGR2GRAY)
if(cap.isOpened()==False):
    print("error in reading vedio")


#reading and plying

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("video",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()