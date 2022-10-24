import cv2
import numpy as np
from math import isclose


def findTiles(image):
    tiles = [image[x:x+100,y:y+100] for x in range(0,image.shape[0],100) for y in range(0,image.shape[1],100)]
    return tiles

def addBiomeText(image, biomeName):
    return cv2.putText(image, biomeName, (5,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

def addNumberText(image, biomeName):
    return cv2.putText(image, biomeName, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

def blurImage(image, kernel_size):
    return cv2.blur(image,kernel_size)



img = cv2.imread("Cropped and perspective corrected boards/3-52.jpg")

tiles = findTiles(img)
blurredTiles = [blurImage(tiles[x], (999,999)) for x in range(25)]
lineBlurred = np.concatenate(blurredTiles, axis = 1)
lineNormal = np.concatenate(tiles,axis=1)
line = np.concatenate((lineBlurred, lineNormal), axis=0)

# cv2.imshow('window',line)
cv2.waitKey(0)

