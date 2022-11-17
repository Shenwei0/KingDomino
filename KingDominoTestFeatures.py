import cv2
import numpy as np

img = cv2.imread('Cropped and perspective corrected boards/66-124.jpg')


def findTiles(img):
    
    tiles = [img[x:x+100,y:y+100] for x in range(0,img.shape[0],100) for y in range(0,img.shape[1],100)]
    return tiles

sliced = findTiles(img)

slide_number = 6
imgHSV = cv2.cvtColor(sliced[slide_number], cv2.COLOR_BGR2HSV)



# R G and B means after equalization of brigthness
imgEQU = cv2.equalizeHist(imgHSV[:,:,2])
imgHSV_equalized = imgHSV
imgHSV_equalized[:,:,2] = imgEQU

# Convert back to RGB and take mean of RGB channels
imgRGB = cv2.cvtColor(imgHSV_equalized, cv2.COLOR_HSV2RGB)


black_threshold = 35
blue_pixels = 0
red_pixels = 0
yellow_pixels = 0
green_pixels = 0
brown_pixels = 0
black_pixels = 0


for y in range(sliced[slide_number].shape[0]):
    for x in range(sliced[slide_number].shape[1]):
        if (95 < imgHSV[y,x,0] and imgHSV[y,x,0] < 135):
                blue_pixels += 1
        
        if (170 < imgHSV[y,x,0] or imgHSV[y,x,0] < 10):
                red_pixels += 1
        
        if (20 < imgHSV[y,x,0] and imgHSV[y,x,0] < 35):
                yellow_pixels += 1
        
        if (40 < imgHSV[y,x,0] and imgHSV[y,x,0] < 80):
                green_pixels += 1

        if (10 < imgHSV[y,x,0] and imgHSV[y,x,0] < 20):
                brown_pixels += 1

        if (black_threshold > sliced[slide_number][y,x,0] and sliced[slide_number][y,x,1] < black_threshold and sliced[slide_number][y,x,2] < black_threshold):
                black_pixels += 1
    
print(f'Blue: {blue_pixels}')
print(f'Red: {red_pixels}')
print(f'Yellow: {yellow_pixels}')
print(f'Green: {green_pixels}')
print(f'Brown: {brown_pixels}')
print(f'Black: {black_pixels}')


""" 
cv2.imshow('win', sliced[slide_number])
cv2.waitKey(0)
 """
'''
imgEQU = cv2.equalizeHist(imgHSV[:,:,2])


test =cv2.putText(sliced[2],'test', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

'''
