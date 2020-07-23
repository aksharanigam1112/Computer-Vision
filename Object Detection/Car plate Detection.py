import cv2
import matplotlib.pyplot as plt

# Read in the cascade classifiers for plate
plate_cascade = cv2.CascadeClassifier('../Haarcascades/haarcascade_russian_plate_number.xml')

# create a function to detect car plate
def detect_plate(img):
    plate_img = img.copy()

    plate_rect = plate_cascade.detectMultiScale(image=plate_img,
                                              scaleFactor=1.2,
                                              minNeighbors=1)

    for (x, y, w, h) in plate_rect:
        cv2.rectangle(img=plate_img,
                      pt1=(x,y),
                      pt2=(x+w,y+h),
                      color=(215,255,0),
                      thickness=10)

    return plate_img

# Reading in the image
img = cv2.imread('images/car-plates.jpg')
img_fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Detecting the plate
result = detect_plate(img_fix)
plt.imshow(result)
plt.show()