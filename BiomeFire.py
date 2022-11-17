import cv2
import numpy as np

# This file will implement the grassfire method to seperate biomes from each other and calculate scores based

# Make function for searching
def biomeBurner(tile_biomes):

    def search4(y, x):
        
        if (y+1 > 4 or burn_queue.count((y+1,x)) > 0):
            pass
        else:
            if (burn_biomes[y+1,x] == current_biome):
                burn_queue.append((y+1,x))
        
        if (x-1 < 0 or burn_queue.count((y,x-1)) > 0):
            pass
        else:
            if (burn_biomes[y,x-1] == current_biome):
                burn_queue.append((y,x-1))

        if (y-1 < 0 or burn_queue.count((y-1,x)) > 0):
            pass
        else:
            if (burn_biomes[y-1,x] == current_biome):
                burn_queue.append((y-1,x))
        
        if (x+1 > 4 or burn_queue.count((y,x+1)) > 0):
            pass
        else:
            if (burn_biomes[y,x+1] == current_biome):
                burn_queue.append((y,x+1))


    # make a copy of the biome array parameter
    burn_biomes = tile_biomes.copy()

    # Burn queue
    burn_queue = []

    # Counter for connected biomes
    connected_biomes = 1

    # Dictionary for coordinates
    connected_biomes_coordinates = {}

    # For each biome tile, burn surrounding tiles with same biome type
    for y in range(5):
        for x in range(5):
            # Variable for first biome
            current_biome = burn_biomes[y, x]

            # Make array with coordinates for this blob
            coordinates = []

            if current_biome == 0:
                pass

            else:
                # Burn the current tile
                burn_biomes[y, x] = 0
                # Append to array
                coordinates.append((y, x))

                # Check surroundring tiles
                search4(y,x)

                # While burn_queue is not empty continue
                while (len(burn_queue) > 0):

                    # Pop the lastest in queue
                    pixel_to_burn = burn_queue.pop()
                    
                    # Burn the lastest in queue
                    burn_biomes[pixel_to_burn[0], pixel_to_burn[1]] = 0
                    coordinates.append((pixel_to_burn[0], pixel_to_burn[1]))

                    #check surrounding tiles
                    search4(pixel_to_burn[0], pixel_to_burn[1])
                connected_biomes_coordinates[connected_biomes] = coordinates
                connected_biomes += 1
    return connected_biomes_coordinates



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
    test_array = np.zeros((5, 5))
    test_array[0, :] = [6, 6, 2, 1,1]
    test_array[1, :] = [6, 5, 5, 2, 2]
    test_array[2, :] = [6, 6, 5, 5,6]
    test_array[3, :] = [5, 0, 1, 1, 6]
    test_array[4, :] = [5, 2, 2, 2, 6]


    # implement grassfire function
    biomes_dict = biomeBurner(test_array)

    print(len(biomes_dict))


if __name__ == "__main__":
    main()
