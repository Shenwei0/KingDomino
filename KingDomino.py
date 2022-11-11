import cv2
import numpy as np


class board:
    def __init__(self, path_to_image):
        self.path = path_to_image
        self.image = self.readImage(self.path)
    
    def readImage(self, path):
        ''' The function reads the board using openCV \n
        
            Parameters: \n

            path: A path to the picture of the board
            
            color_bool: A boolean determining whether the image is read in color or grayscale (1 is color, 0 is grayscale)
            
            '''
        returnImage = cv2.imread(path)
        return returnImage

    def showBoard(self, name="Window"):
        ''' The function displays an image using openCV \n
        
            Parameters: \n

            image: A np.array containing an image
            
            name: A string with the title of the display window (default is 'window')
            
            '''
        cv2.imshow(name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showBoard(self, name="Window"):
        ''' The function displays an image using openCV \n
        
            Parameters: \n

            image: A np.array containing an image
            
            name: A string with the title of the display window (default is 'window')
            
            '''
        cv2.imshow(name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()







def main():
    board1 = board('Cropped and perspective corrected boards/2dreez.jpg')

    board1.showImage()





if __name__ == "__main__":
    main()