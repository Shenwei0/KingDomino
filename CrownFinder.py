import cv2
import numpy as np
import os
import glob
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

boxes = list()
def doTemplateMatch(image, template, threshold = 0.60, blurBool = 0):
    '''This function does template matching on an image, with a template \n
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

        # Make sure the global variable boxes is accessible
        global boxes

        # Loop over the matches' (x, y)-coordinates
        for (x, y) in zip(x_points, y_points):
            # Append the point to the list with coodinates as well as the other end-corner of the box
            boxes.append((x, y, x + W, y + H))

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

def drawMatches(image):
    '''Apply non-maxima suppression to the global boxes variable. This will create a single bounding box.
        Input: The image on which the boxes will be drawn
        Output: The input image with boxes around each crown (hopefully)
    '''
    # Make sure we can access the global variable boxes
    global boxes

    # Use non max suppression on the list of boxes to make use non are counted more than ones
    boxes = non_max_suppression(np.array(boxes))

    # Loop over the final bounding boxes
    for (x1, y1, x2, y2) in boxes:
        # Draw the bounding box on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)

def templateMatchAll():
    doTemplateMatch(img, temp_swamp)
    doTemplateMatch(img, temp_mine)
    doTemplateMatch(img, temp_water)
    doTemplateMatch(img, temp_forest)
    doTemplateMatch(img, temp_grass, 0.7)
    doTemplateMatch(img, temp_wheat)

def loadTemplates():
    # Make them all accessibler
    global temp_swamp
    global temp_wheat
    global temp_grass
    global temp_mine
    global temp_water
    global temp_forest

    # Load template images and rotate them
    temp_swamp = cv2.imread("Crowns/swamp.jpg")
    temp_wheat = cv2.imread("Crowns/wheat.jpeg")
    temp_grass = cv2.imread("Crowns/grass.jpg")
    temp_mine = cv2.imread("Crowns/mine.jpg")
    temp_water = cv2.imread("Crowns/water.jpg")
    temp_forest = cv2.imread("Crowns/forest.jpg")



""" # Load billede
path = '17-40-train.jpg'
img = cv2.imread(f'./Cropped and perspective corrected boards/{path}')

 """
 # load templates
loadTemplates()

# Find all pictures used for training
os.chdir('./Cropped and perspective corrected boards')
train_photos = glob.glob('./*reez.jpg')

print(len(train_photos))
# Loop igennem billeder
for image in range(len(train_photos)):

    # Load billede
    img = cv2.imread(train_photos[image])



    # Do templpate matching and draw boxes
    templateMatchAll()
    drawMatches(img)
    print(len(boxes))

    # Reset crowns found to prepare for next image
    boxes = list()

    # åben billede
    openImage(img, f'{train_photos[image]}')

