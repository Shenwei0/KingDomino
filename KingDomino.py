import cv2
import numpy as np

img = cv2.imread("Cropped and perspective corrected boards/4-42.jpg")

height, width, channels = img.shape

imgBredde = int(width/5)
imgHøjde = int(height/5)

for Ysquare in range(5):
    for Xsquare in range(5):
        imgSliced = img[imgHøjde*Ysquare:imgHøjde*(Ysquare+1), imgBredde*Xsquare:imgBredde*(Xsquare+1)]
        cv2.imshow(f"Sliced{Xsquare} x {Ysquare}", imgSliced)

cv2.waitKey(0)


#morten