import matplotlib.image as mplimg
import cv2
import numpy as np

def v_mean(vector):
    return vector.mean()

img = mplimg.imread('dog_1.jpg')
gray_img = np.apply_along_axis(v_mean, axis = 2, arr = img)
print(gray_img[0][0])
result = cv2.imwrite('gray_dog_2.jpg',gray_img)
