from pickle import TRUE
import cv2
from math import isclose
import numpy as np
from sqlalchemy import false, true


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


def blurImage(image, kernel_size):
    return cv2.blur(image,kernel_size)

def identifyTile(image):
    wheatBiomeBGR = [16, 155, 186]
    wheatBiomePM = [15, 25, 20]
    imgBmean = int(np.mean(image[:,:,0]))
    imgGmean = int(np.mean(image[:,:,1]))
    imgRmean = int(np.mean(image[:,:,2]))

    # Check if the biome is wheat
    if (isclose(imgBmean, wheatBiomeBGR[0], abs_tol = wheatBiomePM[0]) and isclose(imgGmean, wheatBiomeBGR[1], abs_tol = wheatBiomePM[1]) and isclose(imgRmean, wheatBiomeBGR[2], abs_tol = wheatBiomePM[2])):
        test = cv2.putText(image,'wheat', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    else: 
        test =cv2.putText(image,'Not', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

    return test



#####################################################################
# Variable initiation


# Read the image
img = readImage("Cropped and perspective corrected boards/57-64.jpg")


# Make an array with the individual tiles in the image
imgSplit = findTiles(img)

# Blur the individual tiles to prepare for biome detection
""" blurredImg1 = blurImage(imgSplit[12], (999,999))
print(blurredImg1)
 """

blurredImg = [identifyTile(blurImage(imgSplit[x], (999,999))) for x in range(25)]
showImage(np.concatenate(blurredImg,axis=1))
