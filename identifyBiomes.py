import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from KingDominoFunctions import findTiles, readImage, showImage
from MakeDataBasedOnImages import extractTileFeatures

def KNN(observation, training, ground_truth, k = 3):
    '''The function utilises the sklearn library to approximate which biome an observe tile classifies as.
        The data from the observation and the training set, should be normalized before use to get the best result\n
    
        Parameters: \n

        observation: An np array containing the features 

        training: The training data

        ground_truth: result for each sample in the training set

        return: The approximated ground_truth
    
    '''
    # Making a classifier
    classifier = KNeighborsClassifier(k,weights='uniform', algorithm='brute')

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
    



def main():

    # pop biome names from csv file, to give them numbers instead of string names
    data = pd.read_csv('./data.csv')


    # Pop the names and convert to numpy in order to use them as ground_truth
    biome_names = data.pop('Biome')
    biome_names = biome_names.to_numpy()

    # normalize data and convert to numpy
    data_normalized_features = normalize_dataFrame(data).to_numpy()


    # Read an image
    img = readImage('Cropped and perspective corrected boards/24-52-20t-train.jpg')

    # Split it into tiles
    imgTiles = findTiles(img)

    # Extract features from the wanted tile
    tile_feature = extractTileFeatures(imgTiles[11])

    # Normalize tile features
    tile_feature_normalized = normalize_test_data(tile_feature, data)


    # Predict which biome is needed
    print(KNN(tile_feature_normalized, data_normalized_features, biome_names))



if __name__ == "__main__":
    main()



