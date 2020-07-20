import cv2
import matplotlib.pyplot as plt

# Read in the cascade classifiers for eyes
eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

# create a function to detect eye
def detect_eye(img):
    eye_img = img.copy()

    eye_rect = eye_cascade.detectMultiScale(image=eye_img,
                                              scaleFactor=1.2,
                                              minNeighbors=5)
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(img=eye_img,
                      pt1=(x,y),
                      pt2=(x+w,y+h),
                      color=(255,0,0),
                      thickness=2)

    return eye_img

# Reading in the image
img = cv2.imread('images/eye-face.jpeg')
img_fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Detecting the eyes
face = detect_eye(img_fix)
plt.imshow(face)
plt.show()