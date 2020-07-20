import numpy as np
import cv2

# True when mouse button is down
# False when mouse button is up
drawing = False
ex=-1
ey=-1

def draw_rectangle(event,x,y,flags,param):

    global ex,ey,drawing
    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        ex,ey = x,y

    elif event == cv2.EVENT_MOUSEMOVE :
        if drawing == True :
            cv2.rectangle(img=img,
                          pt1=(ex,ey),
                          pt2=(x,y),
                          color=(255,0,255),
                          thickness=-1)

    elif event == cv2.EVENT_LBUTTONUP :
        drawing = False
        cv2.rectangle(img=img,
                      pt1=(ex,ey),
                      pt2=(x,y),
                      color=(255,0,255),
                      thickness=-1)

img = np.zeros((1024,1024,3),np.int8)

cv2.namedWindow(winname="Drawing")

cv2.setMouseCallback("Drawing",draw_rectangle)

while True :

    cv2.imshow("Drawing",img)
    if(cv2.waitKey(5) & 0xFF == 27):
        break

cv2.destroyAllWindows()