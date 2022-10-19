import cv2
import numpy as np

img = cv2.imread("Cropped and perspective corrected boards/31-67-27t.jpg")


def findTiles(img):
    height, width, _ = img.shape

    imgBredde = int(width/5)
    imgHøjde = int(height/5)

    
    tiles = [img[x:x+100,y:y+100] for x in range(0,img.shape[0],100) for y in range(0,img.shape[1],100)]
    return tiles

sliced = findTiles(img)

cv2.imshow('win', sliced[5])
cv2.waitKey(0)
#morten