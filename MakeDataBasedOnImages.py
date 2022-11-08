import cv2
import csv
import glob
import os
import numpy as np

# Functions 

def listdir_nohidden(path=os.getcwd()):
    return glob.glob(os.path.join(path, '*'))


def extractHSVData(image):
    H = image[:,:,0]
    S = image[:,:,1]
    V = image[:,:,2]
    return H, S, V


def addDataRow(row):
    os.chdir('/Users/mortenstephansen/Documents/GitHub/KingDomino/')
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        global header
        writer.writerow(header)
        writer.writerow(row)


header = ['name', 'Hue', 'Saturation']




# For every biome, find the values of the features
for biomes in listdir_nohidden('/Users/mortenstephansen/Documents/GitHub/KingDomino/image dump'):
    
        train_photos = sorted(glob.glob(f'{biomes}/*.jpg'))
        os.chdir(biomes)
        for image in train_photos:
            img = cv2.imread(image)
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            H, S, _ = extractHSVData(imgHSV)
            row = ('test', H, S)
            addDataRow(row)


