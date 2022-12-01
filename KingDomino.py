import cv2
import numpy as np
import glob
from identifyBiomes import identifyBoard, drawBiomes, colorBiomes
from BiomeFire import biomeBurner
from CrownFinder import templateMatchAll, drawMatches


class board:
    def __init__(self, path_to_image, path_to_Crowns, path_to_data='./data.csv'):
        self.path_to_image = path_to_image
        self.path_to_data = path_to_data
        self.path_to_crowns = path_to_Crowns
        self.image = self.__readImage()
        self.tiles = self.__splitTiles()
        self.tile_biomes = self.__identifyTiles()
        

    def showBoard(self, with_biomes = False, with_crowns = False, name="Board"):
        ''' The function displays the board using openCV \n
        
            Parameters: \n

            image: A np.array containing an image
            
            name: A string with the title of the display window (default is 'Board')
            
            '''
        # Load the image of the board
        image = self.image.copy()
        
        # If the user wants to see biomes - draw them
        if (with_biomes == 1):
            image = drawBiomes(self.tile_biomes, image)


        # If the user wants to see crowns - draw them
        if (with_crowns == 1):
            boxes = templateMatchAll(self.image, self.path_to_crowns)
            image = drawMatches(image, boxes)

        cv2.imshow(name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showGraphic(self, name='Graphical representation of the board'):
        ''' The function displays the board as openCV sees it \n
        
            Parameters: \n
            
            name: Window name
            
        '''
        image = colorBiomes(self.tile_biomes)

        boxes = templateMatchAll(self.image, self.path_to_crowns)
        image = drawMatches(image, boxes)

        cv2.imshow(name, image)
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
        biome_array = self.__makeBiomeArray()

        biomes_dict = biomeBurner(biome_array)

        score = 0

        for connected_biome in range(len(biomes_dict)):
            crowns = 0
            for tile in range(len(biomes_dict[connected_biome+1])):
                y,x = biomes_dict[connected_biome+1][tile]
                crowns_squares = templateMatchAll(self.tiles[y,x], self.path_to_crowns)
                crowns += len(crowns_squares)
            score += crowns * len(biomes_dict[connected_biome+1])
    
        return score



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
        '''The function uses the identifyBoard function from the identifyBiomes.py file'''
        return identifyBoard(self.tiles, self.path_to_data)

    def __makeBiomeArray(self):
        '''The function uses the tile_biomes dictionary to make an array where the biome names are numbers \n
        This makes it easier to run a grassfire function on the array \n

        The biome names will get the following numbers:
             Biomes: \n

                Start  = 0

                Grass  = 1

                Wheat  = 2

                Mine   = 3

                Swamp  = 4

                Forest = 5

                Water  = 6
        '''
        biome_array = {}
        for y in range(5):
            for x in range(5):
                if (self.tile_biomes[y,x] == 'forest'):
                    biome_array[y,x] = 5
                elif(self.tile_biomes[y,x] == 'mine'):
                    biome_array[y,x] = 3
                elif(self.tile_biomes[y,x] == 'grass'):
                    biome_array[y,x] = 1
                elif(self.tile_biomes[y,x] == 'swamp'):
                    biome_array[y,x] = 4
                elif(self.tile_biomes[y,x] == 'water'):
                    biome_array[y,x] = 6
                elif(self.tile_biomes[y,x] == 'wheat'):
                    biome_array[y,x] = 2
                else:
                    biome_array[y,x] = 0
        return biome_array




def main():

    board1 = board('/Users/mortenstephansen/Documents/GitHub/KingDomino/Cropped and perspective corrected boards/66-124-test.jpg', '/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns')

    board1.showBoard(0, 1)



if __name__ == "__main__":
    main()