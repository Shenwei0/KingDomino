import cv2
import numpy as np

####################################################################
# Function declarations


def readImage(image, TYPE = 1):
    returnImage = cv2.imread(image,TYPE)
    return returnImage


def showImage(image, name="Window"):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def findTiles(image):
    tiles = [image[x:x+100,y:y+100] for x in range(0,image.shape[0],100) for y in range(0,image.shape[1],100)]
    return tiles


def 



#####################################################################
# Variable initiation



img = readImage("Cropped and perspective corrected boards/4-42.jpg")

imgSplit = findTiles(img)
