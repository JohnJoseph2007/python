import cv2
import numpy as np

# Why we need 4cc: to save the output in a video file (.avi)
fourcc = cv2.VideoWriter_fourcc(*"XVID") # To set up 4cc (video codec)
output = cv2.VideoWriter("output.avi", fourcc, 24, (640, 480)) # To create an output file
start = cv2.VideoCapture(0) # To start the camera
bg = 0
for i in range(60):
    label, data = start.read() # Label stores the name of the image, data stores the value.
bg = np.flip(data, 1) # To flip on y (1) axis.
while(start.isOpened()):
    ret, vid = start.read() # Ret is another variable for label while vid is for data. line 10
    if not ret:
        break
    vid = np.flip(vid, 1)
    hsv = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV) # Used to convert RGB (BGR) to HSV format

    # A mask is a binary image that consists of zero and non zero values.
    # If a mask is applied to another binary or grayscale image, all the pixels which are zero inside the mask are set to zero in the output.

    lowerRed = np.array([0, 120, 50])
    upperRed = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lowerRed, upperRed) # Returns array of values, 0 in positions where HSV is inside the range of LowerRed and UpperRed.
    lowerRed = np.array([170, 120, 70])
    upperRed = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lowerRed, upperRed)
    mask1 = mask1+mask2

    # Kindly open the image before entering the chamber of secrets
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Selecting only the part that does not have mask 1 and saving it in mask 2
    mask2 = cv2.bitwise_not(mask1)
       
    # Keeping only the part of the image without the red colour.
    x = cv2.bitwise_and(vid, vid, mask=mask2)
    
    # Keeping only the part that has the red colour.
    x1 = cv2.bitwise_and(bg, bg, mask=mask1)

    # Final output by merging x and c1:
    final = cv2.addWeighted(x, 1, x1, 1, 0) # Helps in alpha blending of the image
    output.write(final)
    cv2.imshow("CLOAK", final)

start.release()
