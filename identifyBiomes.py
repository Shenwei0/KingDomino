import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# pop biome names from csv file, to give them numbers instead of string names
data = pd.read_csv('data.csv')

# Pop the names and convert to numpy in order to use them as classifiers
biome_names = data.pop('Biome')
biome_names = biome_names.to_numpy()

# convert features from csv to nupmy array
data_features = data.to_numpy()

#Make classifier
classifier = KNeighborsClassifier(1,weights='uniform', algorithm='brute')

# Define classifier
classifier.fit(X=data_features,y=biome_names)






