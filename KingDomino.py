import cv2
import numpy as np
from identifyBiomes import identifyBoard


class board:
    def __init__(self, path_to_image, path_to_data='./data.csv'):
        self.path_to_image = path_to_image
        self.path_to_data = path_to_data
        self.image = self.__readImage()
        self.tiles = self.__splitTiles()
        self.tile_biomes = self.__identifyTiles()
        

    def showBoard(self, name="Board"):
        ''' The function displays the board using openCV \n
        
            Parameters: \n

            image: A np.array containing an image
            
            name: A string with the title of the display window (default is 'Board')
            
            '''
        cv2.imshow(name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def showTile(self, tile_YX):
        ''' The function displays a tile from the board using openCV \n
        
            Parameters: \n

            image: A np.array containing an image
            
            name: A string with the title of the display window (default is 'Tile')
            
            '''
        y, x = tile_YX

        cv2.imshow(f'Tile ({y},{x})', self.tiles[y,x])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def calculateScore(self):
        '''The function utilises the grassfire method, to segment the biome-blocks from each other in order to calculate score. \n
            This will be done for all the biomes and the score, will then be the sum of the biomes' scores. \n
            
            
            '''
        pass

    def __splitTiles(self):
        '''The function splits the board into 25 pieces and returns a dictionary with the images.
        '''

        tiles = {}

        for y in range(0, self.image.shape[0], 100):
            for x in range(0, self.image.shape[1], 100):
                tiles[y/100,x/100] = self.image[y:y+100, x:x+100]

        return tiles

    def __readImage(self):
        ''' The function reads the board using openCV \n
            
            Parameters: \n

            path: A path to the picture of the board
                
            color_bool: A boolean determining whether the image is read in color or grayscale (1 is color, 0 is grayscale)
                
            '''
        returnImage = cv2.imread(self.path_to_image)
        return returnImage

    def __identifyTiles(self):
        return identifyBoard(self.tiles, self.path_to_data)
        







def main():
    board1 = board('Cropped and perspective corrected boards/2dreez.jpg')



    print(board1.tile_biomes[4,4])





if __name__ == "__main__":
    main()