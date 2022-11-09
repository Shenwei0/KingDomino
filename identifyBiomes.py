import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def KNN(observations, training):
    classifier = KNeighborsClassifier(1,weights='uniform', algorithm='brute')

    classifier.fit()


def normalize_dataFrame(dataFrame):
    return (dataFrame-dataFrame.mean())/dataFrame.std()
    


# pop biome names from csv file, to give them numbers instead of string names
data = pd.read_csv('./data.csv', delim_whitespace=True)

# Pop the names and convert to numpy in order to use them as classifiers
biome_names = data.pop('Biome')
biome_names = biome_names.to_numpy()

# convert features from csv to nupmy array
data_features = data.to_numpy()

# normalize data
data_normalized_features = normalize_dataFrame(data).to_numpy()

print(data_features)

#Make classifier


# Define classifier






