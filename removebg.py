import cv2
import numpy as np


def removebg():
    # load image
    img = cv2.imread('input.jpg')

    # convert to graky
    # Convert image to image gray
    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Applying thresholding technique
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    
    # Using cv2.split() to split channels 
    # of coloured image
    b, g, r = cv2.split(img)
    
    # Making list of Red, Green, Blue
    # Channels and alpha
    rgba = [b, g, r, alpha]
    
    # Using cv2.merge() to merge rgba
    # into a coloured/multi-channeled image
    dst = cv2.merge(rgba, 4)
  

    # save resulting masked image
    cv2.imwrite('input2.jpg', dst)