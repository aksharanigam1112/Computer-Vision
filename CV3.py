import numpy as np
import cv2

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=img,
                   center=(x, y),
                   radius=70,
                   color=(35, 69, 78),
                   thickness=-1)

# Connect function to the callback
cv2.namedWindow(winname="Drawing")

# CallBack
cv2.setMouseCallback("Drawing",draw_circle)

# Show the image
img = np.zeros((512,512,3),np.int8)

while True :
  cv2.imshow("Drawing",img)
  if(cv2.waitKey(5) & 0xFF == 27):
    break

cv2.destroyAllWindows()