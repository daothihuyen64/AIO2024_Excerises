import matplotlib.image as mplimg
import cv2
import numpy as np

def v_mean(vector):
    return vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07

img = mplimg.imread('dog_1.jpg')
gray_img = np.apply_along_axis(v_mean, axis = 2, arr = img)
print(gray_img[0][0])
result = cv2.imwrite('gray_dog_3.jpg',gray_img)
