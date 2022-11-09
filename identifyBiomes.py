import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from KingDominoFunctions import identifyTile, readImage, showImage

def KNN(observation, training, ground_truth):
    classifier = KNeighborsClassifier(1,weights='uniform', algorithm='brute')

    classifier.fit(training, ground_truth)

    obs = normalize_dataFrame(observation).to_numpy()

    prediction = classifier.predict(obs)

    return prediction[0]


def normalize_dataFrame(dataFrame):
    return (dataFrame-dataFrame.mean())/dataFrame.std()
    


# pop biome names from csv file, to give them numbers instead of string names
data = pd.read_csv('./data.csv')

# Pop the names and convert to numpy in order to use them as classifiers
biome_names = data.pop('Biome')
biome_names = biome_names.to_numpy()

# convert features from csv to nupmy array
data_features = data.to_numpy()

# normalize data
data_normalized_features = normalize_dataFrame(data).to_numpy()



#Make classifier


readImage()

KNN(,data_normalized_features, biome_names)

# Define classifier






