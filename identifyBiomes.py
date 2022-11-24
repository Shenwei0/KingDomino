import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from KingDominoFunctions import findTiles, readImage, showImage
from MakeDataBasedOnImages import extractTileFeatures

def KNN(observation, training, ground_truth, k = 5):
    '''The function utilises the sklearn library to approximate which biome an observed tile classifies as.
        The data from the observation and the training set, should be normalized before use to get the best result\n
    
        Parameters: \n

        observation: An np array containing the features 

        training: The training data

        ground_truth: result for each sample in the training set

        return: The approximated ground_truth
    
    '''
    # Making a classifier
    classifier = KNeighborsClassifier(k,weights='distance', algorithm='brute')

    # Fitting the data to the classifier
    classifier.fit(X=training, y=ground_truth)

    # Predict which biome the observation belongs to
    prediction = classifier.predict([observation])

    # Return result
    return prediction[0]


def normalize_dataFrame(dataFrame):
    '''The function normalizes a dataFrame type input \n

    Parameters: \n

    dataFrame: An input of the type 'dataFrame'

    return: A normalized dataFrame
    
    '''
    return (dataFrame-dataFrame.mean())/dataFrame.std()


def normalize_test_data(arr, dataFrame):
    '''The function normalizes an np array according to a dataFrame \n

    Parameters: \n

    arr: An np array 

    dataFrame: An input of the type 'dataFrame'

    return: A normalized np array
    
    '''
    return (arr-dataFrame.mean())/dataFrame.std()
    
def identifyBoard(tiles, path_to_data):
    '''The function guesses the biome on each tile and safes the result in a (5,5) matrix \n
    
    Parameters:
    
    tiles: A dictionary containing the different tiles

    return: An dictionary with the guessed biome names
    '''

    # Read data from the data file
    data = pd.read_csv(path_to_data)

    # Pop the names and convert to numpy in order to use them as ground_truth
    biome_names = data.pop('Biome')
    biome_names = biome_names.to_numpy()

    # normalize data and convert to numpy
    data_normalized_features = normalize_dataFrame(data).to_numpy()

    biomes = {}

    # Loop over each tile to collect feature data
    for y in range(5):
        for x in range(5):

            # Extract features from the tile
            tile_feature = extractTileFeatures(tiles[y,x])

            # Normalize tile features
            tile_feature_normalized = normalize_test_data(tile_feature, data)


            # Predict the tiles biome and safe the result in the dictionary
            biomes[y,x] = KNN(tile_feature_normalized, data_normalized_features, biome_names)

            # Print for debugging
            #print(f'Biome ({y}, {x}) should be: {biomes[y,x]}')

    return biomes

def drawBiomes(biome, img):
    '''The functions adds the biome name to each individual tile \n

        Parameters:

        biome: A dictionary containing the tile names

        img: The image onto which it should be drawn
    '''
    image = img.copy()

    # Draw the result on the tiles
    # Loop over the different tiles
    for y in range(5):
        for x in range(5):
            image = cv2.putText(image,f'{biome[y,x]}', (((x*100)+10),(y*100)+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    return image


def colorBiomes(biome_arr):
    '''The function makes a visual representation of the detected biomes
    '''
    image = np.zeros((500,500, 3), dtype=np.uint8)

    # Colors for biomes
    start_biome = [122, 122, 122]
    water = [233, 169, 23]
    grass = [92, 217, 110]
    forest = [26, 82, 34]
    mine = [0,0,0]
    wheat = [8, 192, 235]
    swamp = [30, 101, 140]

    for y in range(5):
        for x in range(5):
            if (biome_arr[y,x] == 'forest'):
                image[(y*100):(y*100)+100, x*100:(x*100)+100] = forest
            elif (biome_arr[y,x] == 'mine'):
                image[y*100:y*100+100, x*100:x*100+100] = mine
            elif (biome_arr[y,x] == 'wheat'):
                image[y*100:y*100+100, x*100:x*100+100] = wheat
            elif (biome_arr[y,x] == 'swamp'):
                image[y*100:y*100+100, x*100:x*100+100] = swamp
            elif (biome_arr[y,x] == 'water'):
                image[y*100:y*100+100, x*100:x*100+100] = water
            elif (biome_arr[y,x] == 'grass'):
                image[y*100:y*100+100, x*100:x*100+100] = grass
            else:
                image[y*100:y*100+100, x*100:x*100+100] = start_biome
    return image

def main():
    """ 
    # Read data from the data file
    data = pd.read_csv('./data.csv')


    # Pop the names and convert to numpy in order to use them as ground_truth
    biome_names = data.pop('Biome')
    biome_names = biome_names.to_numpy()

    # normalize data and convert to numpy
    data_normalized_features = normalize_dataFrame(data).to_numpy()
 """

    # Read an image
    img = readImage('Cropped and perspective corrected boards/2dreez.jpg')

    #Make a copy of the image
    imgCopy = np.copy(img)

    # Split it into tiles
    imgTiles = findTiles(img)

    # Extract features from the tiles
    biomes = identifyBoard(imgTiles, './data.csv')

    # Draw biomes on 5x5 image
    coloredBiome = colorBiomes(biomes)

    # Draw biome names on the tiles
    imgCopy = drawBiomes(biomes, imgCopy)

    # show the image
    showImage(coloredBiome)



    
""" 
     # Extract features from the tiles
    for y in range(5):
        for x in range(5):
            tile_feature = extractTileFeatures(imgTiles[y,x])

            # Normalize tile features
            tile_feature_normalized = normalize_test_data(tile_feature, data)

            # Predict which biome is needed
            print(f'Biome ({y}, {x}) should be: {KNN(tile_feature_normalized, data_normalized_features, biome_names)}')
            imgCopy = cv2.putText(imgCopy,f'{KNN(tile_feature_normalized, data_normalized_features, biome_names)}', (((x*100)+10),(y*100)+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

    showImage(imgCopy) """


if __name__ == "__main__":
    main()



