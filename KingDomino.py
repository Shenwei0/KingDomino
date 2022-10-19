import cv2
import numpy as np

img = cv2.imread("Cropped and perspective corrected boards/31-67-27t.jpg")


def findTiles(img):
    tiles = [img[x:x+100,y:y+100] for x in range(0,img.shape[0],100) for y in range(0,img.shape[1],100)]
    return tiles

sliced = findTiles(img)

test =cv2.putText(sliced[2],'test', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

cv2.imshow('win', test)
cv2.waitKey(0)
#morten