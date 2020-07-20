import numpy as np
import cv2

def draw(event, x, y, flags, param):
    # Left Button Click
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=img,
                   center=(x, y),
                   radius=100,
                   color=(75,131,251),
                   thickness=-1)
    # Right Button Click
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(
            img=img,
            pt1=(x,y),
            pt2=(x+100,y+100),
            color=(0,155,251),
            thickness=-1
        )
# Connect function to the callback
cv2.namedWindow(winname="Drawing")

# CallBack
cv2.setMouseCallback("Drawing",draw)

# Show the image
img = np.zeros((512,512,3),np.int8)

while True :
  cv2.imshow("Drawing",img)
  if(cv2.waitKey(5) & 0xFF == ord('q')):
    break

cv2.destroyAllWindows()