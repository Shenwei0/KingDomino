#6. Use Python and OpenCV to load and display neon-text.png
import math

import cv2
import numpy as np

img = cv2.imread("Cropped and perspective corrected boards/4-42.jpg")
cv2.imshow("image", img)
# 6.1. Use template matching to make an image which shows the positions of the three hearts, similar to the one below
# Hint: Use a combination of the functions matchTemplate, normalize, and threshold
crownup_template = cv2.imread("Crowns/Crown2UP.PNG")
#crowndown_template = cv2.imread("Images\Crown2DOWN.PNG")
#crownleft_template = cv2.imread("Images\Crown2LEFT.PNG")

output_template = cv2.matchTemplate(img, crownup_template, cv2.TM_SQDIFF_NORMED)
# Show the correlation image as an intermediate step.
# (the white dots showing the positions are very small, but there are three of them).
cv2.imshow("output template", output_template)

output_normalized = ((output_template / np.max(output_template)) * 255).astype(np.uint8)  # Normalize and convert to uint8

output_thresh = 255 - output_normalized  # Invert image as matchTemplate stores matches as low numbers
for row in output_thresh:  # Threshold the image
    row[row < 245] = 0
cv2.imshow("output_thresh", output_thresh)

cv2.waitKey(0)
