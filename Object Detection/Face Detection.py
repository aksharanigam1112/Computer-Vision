import cv2
import matplotlib.pyplot as plt

# Read in the cascade classifiers for face
face_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

# create a function to detect face
def detect_face(img):
    face_img = img.copy()

    face_rect = face_cascade.detectMultiScale(image=face_img,
                                              scaleFactor=1.2,
                                              minNeighbors=15)

    for (x, y, w, h) in face_rect:
        cv2.rectangle(img=face_img,
                      pt1=(x,y),
                      pt2=(x+w,y+h),
                      color=(255,0,0),
                      thickness=2)

    return face_img

# Reading in the image
img = cv2.imread('images/eye-face.jpeg')
img_fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Detecting the face
face = detect_face(img_fix)
plt.imshow(face)
plt.show()