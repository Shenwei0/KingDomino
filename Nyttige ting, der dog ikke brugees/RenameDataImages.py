import os
import glob

path = '/Users/mortenstephansen/Documents/GitHub/KingDomino/DataSet/wheat/'

images = glob.glob(f'{path}*.jpg')



name = 1
for image in images:
    os.rename(image, f'{path}{name:03d}.jpg')
    name += 1