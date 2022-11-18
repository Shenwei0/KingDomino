import glob
import os
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

# Denne fil prøver at finde crowns vha. template matching.


#
#
# Funktioner
#
#


def openImage(image, title='Window'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def doTemplateMatch(boxes_list, image, template, threshold = 0.60, blurBool = 0):
    '''This function does template matching on an image, with a template \n
        boxes_list: A list with the coordinates for each rectangle
        Image: An input image \n
        Template: A template \n
        Threshold: The threshold for accepting a match'''
    
    # Rotate the template, to make sure the template can find all four orientations
    template = rotateTemp(template)

    # Toggle parameter to enable blur (optional, default is off)
    if blurBool:
        blurTempAll(template)

    # For every template orientation/blur, check for matches 
    for current_template in range(len(template)):

        # Run the matchTemplate on the current template
        img_result = cv2.matchTemplate(image, template[current_template], cv2.TM_CCOEFF_NORMED)

        # Save the positions for every match within the threshold
        (y_points, x_points) = np.where(img_result >= threshold)

        # Show the result for the template (For debugging)
        """ cv2.imshow(f'{current_template}', img_result)
        cv2.waitKey(0) 
        cv2.destroyWindow(f'{current_template}') """

        # Use the shape to find the width and height of the image
        W, H = template[current_template].shape[:2]

        # Loop over the matches' (x, y)-coordinates
        for (x, y) in zip(x_points, y_points):
            # Append the point to the list with coodinates as well as the other end-corner of the box
            boxes_list.append((x, y, x + W, y + H))
    return boxes_list

def rotateTemp(template):
    '''Take an input (image) and rotates it 3 times and returns the original, turned 90 degrees clockwise, 180 degress, and 90 degress counter-clockwise \n

    Input: Image
    Output: Tuple with the input picture and the 3 additional rotations

    '''
    # Rotate the input image 3 times and return the 4 images in an array
    temp_down = cv2.rotate(template, cv2.ROTATE_180)
    temp_left = cv2.rotate(template, cv2.ROTATE_90_COUNTERCLOCKWISE)
    temp_right = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
    return [template, temp_right, temp_down, temp_left]

def blurTempAll(template, ksize=5):
    '''Blur templates - This function is made for use after the 'rotateTemp' function. DO NOT USE OTHERWISE \n
    Input: array of 4 images
    Output: The array is now 8 pictures, the new four aer simply blurred versions of the others.
    '''
    template.append(cv2.GaussianBlur(template[0],(ksize,ksize), 0))
    template.append(cv2.GaussianBlur(template[1],(ksize,ksize), 0))
    template.append(cv2.GaussianBlur(template[2],(ksize,ksize), 0))
    template.append(cv2.GaussianBlur(template[3],(ksize,ksize), 0))

def drawMatches(image, boxes_list):
    '''This will create a single bounding box.
        image: The image on which the boxes will be drawn
        boxes_list: The list with the box coordinates
        Output: The input image with boxes around each crown (hopefully)
    '''

    # Loop over the final bounding boxes
    for (x1, y1, x2, y2) in boxes_list:
        # Draw the bounding box on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)

def templateMatchAll(image):
    boxes = list()
    temp_swamp, temp_wheat, temp_grass, temp_mine, temp_water, temp_forest = loadTemplates()
    boxes = doTemplateMatch(boxes, image, temp_swamp)
    boxes = doTemplateMatch(boxes, image, temp_mine)
    boxes = doTemplateMatch(boxes, image, temp_water)
    boxes = doTemplateMatch(boxes, image, temp_forest)
    boxes = doTemplateMatch(boxes, image, temp_grass, 0.7)
    boxes = doTemplateMatch(boxes, image, temp_wheat)

    # Use non max suppression on the list of boxes to make use non are counted more than ones
    boxes = non_max_suppression(np.array(boxes))

    return boxes

def loadTemplates():
    # Load template images and rotate them
    temp_swamp = cv2.imread("/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns/swamp.jpg")
    temp_wheat = cv2.imread("/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns/wheat.jpeg")
    temp_grass = cv2.imread("/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns/grass.jpg")
    temp_mine = cv2.imread("/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns/mine.jpg")
    temp_water = cv2.imread("/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns/water.jpg")
    temp_forest = cv2.imread("/Users/mortenstephansen/Documents/GitHub/KingDomino/Crowns/forest.jpg")

    # Return the images
    return temp_swamp, temp_wheat, temp_grass, temp_mine, temp_water, temp_forest


def main():
    # Find all pictures used for training
    os.chdir('./Cropped and perspective corrected boards')
    train_photos = glob.glob('./59-38.jpg')

    print(len(train_photos))
    # Loop igennem billeder
    for image in range(len(train_photos)):

        # Load billede
        img = cv2.imread(train_photos[image])



        # Do templpate matching and draw boxes
        boxes = templateMatchAll(img)
        drawMatches(img, boxes)
        print(len(boxes))


        # åben billede
        openImage(img, f'{train_photos[image]}')


if __name__ == "__main__":
    main()