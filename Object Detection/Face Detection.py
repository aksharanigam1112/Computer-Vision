import numpy as np
import cv2
import matplotlib.pyplot as plt

face_classifier = cv2.CascadeClassifier('/Haarcascades/haarcascade_frontalface_default.xml')

# Open the image
image = cv2.imread('images/eye-face.jpeg')
fix_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
plt.show()

# Detect Faces
faces = face_classifier.detectMultiScale(image,1,5)

# If no faces found
if faces is ():
    print("No Faces found")

# Face detection
def detect_face(fix_img):
    face_rects = face_classifier.detectMultiScale(fix_img)

    for(x,y,w,h) in face_rects :
        cv2.rectangle(img=fix_img,
                      pt1=(x,y),
                      pt2=(x+w,y+h),
                      color=(255,0,0),
                      thickness=10)
    return fix_img

result = detect_face(fix_img)
plt.imshow(result)
plt.show()