import cv2
import csv
import glob
import os
from sklearn.preprocessing import StandardScaler
import numpy as np

# Functions 
def listdir_nohidden(path=os.getcwd()):
    return glob.glob(os.path.join(path, '*'))


def extractData3Channels(image):
    c1 = np.mean(image[:,:,0])
    c2 = np.mean(image[:,:,1])
    c3 = np.mean(image[:,:,2])

    return c1, c2, c3

def findTiles(image):
    tiles = [image[x:x+100,y:y+100] for x in range(0,image.shape[0],100) for y in range(0,image.shape[1],100)]
    return tiles

def addDataRow(row):
    with open('data.csv', 'w') as file:
        global header
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(row)



# Global vars

folder_path = '/Users/mortenstephansen/Documents/GitHub/KingDomino/slices/'

biome_paths = ['blue_start', ' blue_castle_start', 'forest_biome', 
                'forest_house_biome', 'grass_biome', 'grass_house_biome', 
                'green_start', 'green_castle_start', 'mine_biome', 'red_start', 'red_castle_start',
                'swamp_biome', 'swamp_house_biome', 'water_biome', 'water_house_biome', 
                'wheat_biome', 'wheat_house_biome', 'wood_table', 'yellow_start', 'yellow_castle_start']

biomes_data_row = []

header = ['Hue mean', 'Saturation mean', 'Biome']

# For every biome, find the values of the features

for biomes in biome_paths:
    
        train_photos = listdir_nohidden(f'{folder_path}{biomes}')

        for image in train_photos:
            img = cv2.imread(image)

            # Do different feature extractions

            # Find hue and saturation
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            H, S, _ = extractData3Channels(imgHSV)

            # Find YCrCb features
            imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)




            # Append to dataset array
            biomes_data_row.append([H, S, biomes])

            


addDataRow(biomes_data_row)

# Scale dataset
""" scaler = StandardScaler()
data = scaler.fit_transform(biomes_data_row[:,:,1]) """