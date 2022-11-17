import cv2
import numpy as np
import glob
import os

# This file takes a (500,500) image as input and makes 25 tiles out of it


def findTiles(image):
    '''The function converts an image of 500 x 500 pixels to 25 different tiles \n

        img: np.array containing the (500,500) image \n

        return: A np.array containing the 25 tiles

        The function will work even if the image isn't an (500,500), however the output will not be as expected

    '''
    tiles = []
    for y in range(0, image.shape[0], 100):
        for x in range(0, image.shape[1], 100):
            tiles.append(image[y:y+100, x:x+100])
    return tiles

def listdir_nohidden(path=os.getcwd()):
    '''The function lists everything in a folder except for hidden files \n

        Parameters: \n

        path: The path from which the files should be listed
    '''
    return glob.glob(os.path.join(path, '*'))

def main():

    path = '/Users/mortenstephansen/Documents/GitHub/KingDomino/Cropped and perspective corrected boards/'

    name = 0
    for image in glob.glob(f'{path}*train.jpg'):
        img = cv2.imread(image)


        imgTiles = findTiles(img)
        for i in range(len(imgTiles)):
            cv2.imwrite(f'DataSet/{name}.jpg', imgTiles[i])
            name += 1





if __name__ == "__main__":
    main()