import cv2
import numpy as np

# This file will implement the grassfire method to seperate biomes from each other and calculate scores based

# Make function for searching


def search4(y, x, burn_img, burn_queue, tiles, biome, last_searched_pixel):
    if (last_searched_pixel != [y, x]):
            if (tiles[y+1, x] == biome):
                if ((y+1, x) in burn_queue or burn_img[y+1, x] == biome):
                    pass
                else:
                    burn_queue.append((y+1, x))

            if (tiles[y, x-1] == biome):
                if ((y, x-1) in burn_queue or burn_img[y, x-1] == biome):
                    pass
                else:
                    burn_queue.append((y, x-1))

            if (tiles[y-1, x] == biome):
                if ((y-1, x) in burn_queue or burn_img[y-1, x] == biome):
                    pass
                else:
                    burn_queue.append((y-1, x))

            if (tiles[y, x+1] == biome):
                if ((y, x+1) in burn_queue or burn_img[y, x+1] == biome):
                    pass
                else:
                    burn_queue.append((y, x+1))
    last_searched_pixel = [y, x]
    return 

def biomeBurner(tile_biomes):

    # make a copy of the biome array parameter
    burn_biomes = tile_biomes


    # Burn queue
    burn_queue = []

    last_searched_pixel = []

    # For each biome tile, burn surrounding tiles with same biome type
    for y in range(5):
        for x in range(5):
            # Variable for first biome
            current_biome = tile_biomes[y,x]

            if burn_biomes[y,x] == 0:
                pass

            else:
                # Burn the different tiles
                
            
def main():
    '''The different biomes will be given a number following the convention below this \n
    
    Biomes: \n

    Start  = 0

    Grass  = 1

    Wheat  = 2

    Mine   = 3

    Swamp  = 4
    
    Forest = 5
    
    Water  = 6
    '''
    # Array containing the biomes 
    test_array = np.zeros((5,5))
    test_array[0, :] = [6,6,2,1,1]
    test_array[1, :] = [6, 5, 5, 2, 2]
    test_array[2, :] = [6,6,5,5,6]
    test_array[3, :] = [5, 0, 1, 1, 6]
    test_array[4, :] = [5, 2, 2, 2, 6]

    print(test_array)


    # implement grassfite function
    biomeBurner(test_array)



if __name__ == "__main__":
    main()