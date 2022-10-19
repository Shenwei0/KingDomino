import cv2
import numpy as np

def openImage(image):
    img = cv2.imread(image,1)
    return img

def openImageGray(image):
    img = cv2.imread(image, 0)
    return img

def showImage(image, name="Window"):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




img = openImage("Cropped and perspective corrected boards/4-42.jpg")

showImage(img, 'Cropped Image')
