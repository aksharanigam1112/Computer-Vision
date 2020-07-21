import cv2
import numpy as np

body_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_fullbody.xml')

video = cv2.VideoCapture('video/Pedestrian.mp4')

while video.isOpened():

    ret,frame = video.read()
    bodies = body_classifier.detectMultiScale(image=frame,
                                              scaleFactor=1.2,
                                              minNeighbors=3)
    if (ret==True):
        for(x,y,w,h) in bodies :
            cv2.rectangle(img=frame,
                          pt1=(x,y),
                          pt2=(w+x,y+h),
                          color=(25,125,225),
                          thickness=5)
            cv2.imshow('Pedestrians',frame)

        if(cv2.waitKey(1)==27):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
