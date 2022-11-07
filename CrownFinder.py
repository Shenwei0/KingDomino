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


""" img_rgb = cv.imread('mario.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('mario_coin.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)
 """


def openImage(image, title='Window'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

boxes = list()
def doTemplateMatch(image, template, threshold = 0.60, blurBool = 0):
    '''This function does template matching on a grayscaled image, with a greyscaled template \n
        Image: An input image \n
        Template: A template \n
        Threshold: The threshold for accepting a match'''
    
    template = rotateTemp(template)
    if blurBool:
        blurTempAll(template)

    for current_template in range(len(template)):
        img_result = cv2.matchTemplate(image, template[current_template], cv2.TM_CCOEFF_NORMED)
        (y_points, x_points) = np.where(img_result >= threshold)
        """ cv2.imshow(f'{current_template}', img_result)
        cv2.waitKey(0)
        cv2.destroyWindow(f'{current_template}') """
        W, H = template[current_template].shape[:2]
        global boxes
        # loop over the starting (x, y)-coordinates again
        for (x, y) in zip(x_points, y_points):
            # update our list of rectangles
            boxes.append((x, y, x + W, y + H))

def rotateTemp(template):
    temp_down = cv2.rotate(template, cv2.ROTATE_180)
    temp_left = cv2.rotate(template, cv2.ROTATE_90_COUNTERCLOCKWISE)
    temp_right = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
    return [template, temp_right, temp_down, temp_left]

def blurTempAll(template, ksize=5):
    template.append(cv2.GaussianBlur(template[0],(ksize,ksize), 0))
    template.append(cv2.GaussianBlur(template[1],(ksize,ksize), 0))
    template.append(cv2.GaussianBlur(template[2],(ksize,ksize), 0))
    template.append(cv2.GaussianBlur(template[3],(ksize,ksize), 0))



def drawMatches(image):
    # apply non-maxima suppression to the rectangles
    # this will create a single bounding box
    global boxes
    boxes = non_max_suppression(np.array(boxes))
    # loop over the final bounding boxes
    for (x1, y1, x2, y2) in boxes:
        # draw the bounding box on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)


""" # Load billede
path = '17-40-train.jpg'
img = cv2.imread(f'./Cropped and perspective corrected boards/{path}')

 """
# Load template images and rotate them
temp_swamp = cv2.imread("Crowns/swamp.jpg")
temp_wheat = cv2.imread("Crowns/wheat.jpeg")
temp_grass = cv2.imread("Crowns/grass.jpg")
temp_mine = cv2.imread("Crowns/mine.jpg")
temp_water = cv2.imread("Crowns/water.jpg")
temp_forest = cv2.imread("Crowns/forest.jpg")

# Find all pictures used for training
os.chdir('./Cropped and perspective corrected boards')
train_photos = glob.glob('./*train.jpg')

print(len(train_photos))
# Loop igennem billeder
for i in range(len(train_photos)):

    # Load billede
    img = cv2.imread(train_photos[i])

    # Do templpate matching and draw boxes
    doTemplateMatch(img, temp_swamp)
    doTemplateMatch(img, temp_mine)
    doTemplateMatch(img, temp_water)
    doTemplateMatch(img, temp_forest)
    doTemplateMatch(img, temp_grass, 0.7)
    doTemplateMatch(img, temp_wheat)
    drawMatches(img)
    print(len(boxes))
    boxes = list()

    # åben billede
    openImage(img, f'{train_photos[i]}')

