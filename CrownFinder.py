import cv2
import numpy as np

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






# Load billede
path = '13-45-9t-train.jpg'
img = cv2.imread(f'./Cropped and perspective corrected boards/{path}')
img_temp = cv2.imread('Crowns/Crown2LEFT.PNG', 0)

# Grayscale billedet
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
w, h = img_temp.shape[::-1]

# blur grayed image

img_gray_blur = cv2.GaussianBlur(img_gray, (7,7), 0)

# Find templates
img_result = cv2.matchTemplate(img_gray_blur, img_temp, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
locations = np.where( img_result >= threshold)
for pt in zip(*locations[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# åben billede
openImage(img, path)