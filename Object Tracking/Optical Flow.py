import cv2
import numpy as np

# Parameters for SHI-TOMASI CORNER DETECTION
st_params = dict(maxCorners=30,
                 qualityLevel=0.2,
                 minDistance=2,
                 blockSize=7)

# Parameters for LUCAS-KANADE OPTICAL FLOW
lk_params = dict(winSize=(15,19),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1))

cap = cv2.VideoCapture('video/run.mp4')

# Color for optical flow
color = (0,255,0)

# Read the capture and get the first frame
ret,first_frame = cap.read()

# Convert frame to GRAY
prey_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)

# Find the strongest corner in the frame
prev = cv2.goodFeaturesToTrack(prey_gray,
                               mask=None,
                               **st_params)

# Create an image with the same dimensions as the frams
# for later drawing purposes
mask = np.zeros_like(frame)


while(cap.isOpened()):

    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Calculate the optical flow by Lucas Kanade
    next,status,error = cv2.calcOpticalFlowPyrLK(prey_gray,prev,None,**lk_params)
    #





