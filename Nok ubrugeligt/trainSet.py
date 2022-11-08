import os
import glob



# Find all pictures used for training
os.chdir('./Cropped and perspective corrected boards')
train_photos = glob.glob('./*train.jpg')

