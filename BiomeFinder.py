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

class biome:
    def __init__(self, BGRvalues, tolerance):
        self.BGRvalues = BGRvalues
        self.tolerance = tolerance

#Initialize biomes
wheat = biome([14, 150, 165], [16, 50, 35])
water = biome([125, 64, 25], [45, 35, 30])
grass = biome([20, 115, 90], [20, 50, 40])
start = biome([90, 110, 120], [25, 30, 35])



n = 0
def identifyBlurredTile(image):
    global n
    imgBmean = int(np.mean(image[:,:,0]))
    imgGmean = int(np.mean(image[:,:,1]))
    imgRmean = int(np.mean(image[:,:,2]))

    # Check if the biome is wheat
    if (isclose(imgBmean, wheat.BGRvalues[0], abs_tol = wheat.tolerance[0]) and isclose(imgGmean, wheat.BGRvalues[1], abs_tol = wheat.tolerance[1]) and isclose(imgRmean, wheat.BGRvalues[2], abs_tol = wheat.tolerance[2])):
        img = addBiomeText(image, 'Wheat')
        img = addNumberText(image, str(n))
        n += 1
    elif (isclose(imgBmean, start.BGRvalues[0], abs_tol = start.tolerance[0]) and isclose(imgGmean, start.BGRvalues[1], abs_tol = start.tolerance[1]) and isclose(imgRmean, start.BGRvalues[2], abs_tol = start.tolerance[2])):    
        img = addBiomeText(image, 'start')
        img = addNumberText(image, str(n))
        n += 1
    elif (isclose(imgBmean, water.BGRvalues[0], abs_tol = water.tolerance[0]) and isclose(imgGmean, water.BGRvalues[1], abs_tol = water.tolerance[1]) and isclose(imgRmean, water.BGRvalues[2], abs_tol = water.tolerance[2])):
        img = addBiomeText(image, 'Water')
        img = addNumberText(image, str(n))
        n += 1
    elif (isclose(imgBmean, grass.BGRvalues[0], abs_tol = grass.tolerance[0]) and isclose(imgGmean, grass.BGRvalues[1], abs_tol = grass.tolerance[1]) and isclose(imgRmean, grass.BGRvalues[2], abs_tol = grass.tolerance[2])):    
        img = addBiomeText(image, 'grass')
        img = addNumberText(image, str(n))
        n += 1
    else: 
        img = addBiomeText(image, '???')
        img = addNumberText(image, str(n))
        n += 1

    return img


def findValues(image):
    imgBmean = int(np.mean(image[:,:,0]))
    imgGmean = int(np.mean(image[:,:,1]))
    imgRmean = int(np.mean(image[:,:,2]))

    print(f'Blue: {imgBmean}, Green: {imgGmean},  Red: {imgRmean}')

img = cv2.imread("Cropped and perspective corrected boards/26-48.jpg", 1)

tiles = findTiles(img)
blurredTiles = [identifyBlurredTile(blurImage(tiles[x], (999,999))) for x in range(25)]
lineBlurred = np.concatenate(blurredTiles, axis = 1)
lineNormal = np.concatenate(tiles,axis=1)
line = np.concatenate((lineBlurred, lineNormal), axis=0)


# findValues(tiles[20])
findValues(tiles[4])
findValues(tiles[22])
findValues(tiles[23])

cv2.imshow('window',line)
cv2.waitKey(0)


