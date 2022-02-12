# converting a vedio into Gray and Black and white

#import a library 
import cv2 as cv


# load a video into the code
cap = cv.VideoCapture('resourses/video.mkv')

while (True):
    (ret,frame) =  cap.read()# read the video and convert into the frame
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert the video ito graycolor
    (thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the black
    # To Show in Player
    if ret == True:
        cv.imshow("vedio",binaryimg)
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 





cap.release()
cv.destroyAllWindows()