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
    biome_paths = ['blue_start', ' blue_castle_start', 'forest_biome', 
                    'forest_house_biome', 'grass_biome', 'grass_house_biome', 
                    'green_start', 'green_castle_start', 'mine_biome', 'red_start', 'red_castle_start',
                    'swamp_biome', 'swamp_house_biome', 'water_biome', 'water_house_biome', 
                    'wheat_biome', 'wheat_house_biome', 'wood_table', 'yellow_start', 'yellow_castle_start']
    
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
    biomes_data_rows = []    # For every biome, find the values of the features

    # Do different feature extractions

    # Find hue and saturation
    imgHSV = cv2.cvtColor(imageTile, cv2.COLOR_BGR2HSV)
    H, S, _ = extractData3ChannelsMean(imgHSV)

    # Find YCrCb features
    imgYCrCb = cv2.cvtColor(imageTile, cv2.COLOR_BGR2YCrCb)

    # R G and B means equalized for brigthness
    imgEQU = cv2.equalizeHist(imgHSV[:,:,2])

    

    # Return array with features
    if (biome == 0):
        return [H,S]
    else:
        return [H, S, biome]




def main():
    folder_path = '/Users/mortenstephansen/Documents/GitHub/KingDomino/slices/'
    header = ['Hue mean', 'Saturation mean', 'Biome']

    data_rows = extractTrainingFeatures(folder_path)
                


    makeCSVFile(data_rows, header)

if __name__ == "__main__":
    main()