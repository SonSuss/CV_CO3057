import os

import cv2
import numpy as np
import PIL

CURRENT_PATH = os.getcwd()
IMGS_FOLDER_PATH = os.path.join(CURRENT_PATH, 'imgs')

img_path= os.path.join(IMGS_FOLDER_PATH,'1.png')
img = cv2.imread(img_path)

"""Using opencv to convert images"""
rbg_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_rgb = cv2.cvtColor(rbg_gray, cv2.COLOR_GRAY2BGR)

# cv2.imshow('just2ofus',img)
cv2.imshow('just2ofus_gray',rbg_gray)
print(rbg_gray.shape) # shape (736, 736)
cv2.imshow('just2ofus_bgr',gray_rgb)
# print(gray_rgb.shape) # shape (736, 736, 3)




cv2.waitKey(0)
cv2.destroyAllWindows()
