import cv2
import csv
import glob
import os
import numpy as np
from KingDominoFunctions import findTiles

# Functions 
def listdir_nohidden(path=os.getcwd()):
    '''The function lists everything in a folder except for hidden files \n

        Parameters: \n

        path: The path from which the files should be listed
    '''
    return glob.glob(os.path.join(path, '*'))


def extractData3ChannelsMean(image):
    '''The function takes an image with 3 channels and returns the mean of each channel seperately \n

    Input: An image with 3 channels
    '''
    # Calculate the mean for each channel and return them
    c1 = np.mean(image[:,:,0])
    c2 = np.mean(image[:,:,1])
    c3 = np.mean(image[:,:,2])

    return c1, c2, c3


def makeCSVFile(features, header):
    '''The function makes a training data set, with the features from the input \n
    
    Parameters: \n

    features: An array containing the feature values for each row

    header: An array containing the header names for the columns

    '''
    # Write the inputs into a file, and safe it as 'data.csv'
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(features)


def extractTrainingFeatures(path_to_biomes):
    '''The function extracts every training tile, extracts their features, and returns the result from all the tiles \n

        Parameters: \n

        path_to_biomes: The path to the folders with biome tiles

        return: array with data (could be safed in a csv file)
    '''
    # Create array for data
    biomes_data_rows = []    
    
    # Array with different folder names, to use when going through each training tile
    biome_paths = ['forest', 'grass', 'mine', 'start_blue',
                     'start_red', 'start_yellow', 'start_green',
                      'start_castle', 'swamp', 'water', 'wheat']
    
    # For every biome, find the values of the features
    for biomes in biome_paths:

            # Array with every photo in the current biome folder
            train_photos = listdir_nohidden(f'{path_to_biomes}{biomes}')

            for image in train_photos:
                
                img = cv2.imread(image)
                
                # find features

                features = extractTileFeatures(img, biomes)

                # Append to dataset array
                biomes_data_rows.append(features)
                
    return biomes_data_rows


def extractTileFeatures(imageTile, biome = 0):
    # Do different feature extractions

    # Find hue and saturation
    imgHSV = cv2.cvtColor(imageTile, cv2.COLOR_BGR2HSV)
    Hm, Sm, _ = extractData3ChannelsMean(imgHSV)

    # Find YCrCb features
    imgYCrCb = cv2.cvtColor(imageTile, cv2.COLOR_BGR2YCrCb)
    _, Crm, Cbm = extractData3ChannelsMean(imgYCrCb)


    # R G and B means after equalization of brigthness
    imgEQU = cv2.equalizeHist(imgHSV[:,:,2])
    imgHSV_equalized = imgHSV
    imgHSV_equalized[:,:,2] = imgEQU

    # Convert back to RGB and take mean of RGB channels
    imgRGB = cv2.cvtColor(imgHSV_equalized, cv2.COLOR_HSV2RGB)
    Rm, Gm, Bm = extractData3ChannelsMean(imgRGB)

    # Count indicidual colors in the hue scale
    blue_pixels = 0
    yellow_pixels = 0
    red_pixels = 0
    green_pixels = 0
    brown_pixels = 0
    black_pixels = 0

    for y in range(imageTile.shape[0]):
        for x in range(imageTile.shape[1]):
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

            if (35 > imageTile[y,x,0] and imageTile[y,x,1] < 35 and imageTile[y,x,2] < 35):
                black_pixels += 1



    

    # Return array with features
    if biome == 0:
        return [Hm, Sm, Rm, Gm, Bm, Crm, Cbm, blue_pixels, green_pixels, red_pixels, yellow_pixels, brown_pixels, black_pixels]
    else:
        return [Hm, Sm, Rm, Gm, Bm, Crm, Cbm, blue_pixels, green_pixels, red_pixels, yellow_pixels, brown_pixels, black_pixels, biome]




def main():
    folder_path = '/Users/mortenstephansen/Documents/GitHub/KingDomino/DataSet/'
    header = ['Hue mean', 'Saturation mean', 'Red mean', 'Green mean', 'Blue mean', 'R from luminance mean', 'B from luminance mean', 'Blue pixels', 'Green_pixels', 'Red pixels', 'Yellow pixels', 'Brown pixels', 'Black pixels', 'Biome']

    data_rows = extractTrainingFeatures(folder_path)
                


    makeCSVFile(data_rows, header)

if __name__ == "__main__":
    main()