import cv2

car_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_car.xml')

video = cv2.VideoCapture('video/Moving cars.mp4')

while video.isOpened():

    ret,frame = video.read()
    cars = car_classifier.detectMultiScale(image=frame,
                                              scaleFactor=1.4,
                                              minNeighbors=3)
    for(x,y,w,h) in cars :
            cv2.rectangle(img=frame,
                          pt1=(x,y),
                          pt2=(w+x,y+h),
                          color=(25,125,225),
                          thickness=5)
            cv2.imshow('Cars',frame)

    if(cv2.waitKey(1) & 0xFF ==27):
        break

video.release()
cv2.destroyAllWindows()
