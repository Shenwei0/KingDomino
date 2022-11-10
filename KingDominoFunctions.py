import cv2
import numpy as np



####################################################################
# Function declarations





def readImage(path, color_bool = 1):
    ''' The function reads an image using openCV \n
    
        Parameters: \n

        path: A path to the picture that should be opened
        
        color_bool: A boolean determining whether the image is read in color or grayscale (1 is color, 0 is grayscale)
        
        '''
    returnImage = cv2.imread(path,color_bool)
    return returnImage


def showImage(image, name="Window"):
    ''' The function displays an image using openCV \n
    
        Parameters: \n

        image: A np.array containing an image
        
        name: A string with the title of the display window (default is 'window')
        
        '''
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


