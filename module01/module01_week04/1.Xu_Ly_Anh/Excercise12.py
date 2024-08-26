import gdown
gdown.download('https://drive.google.com/uc?id=1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB', 'dog_1.jpg', quiet=False)
import matplotlib.image as mpimg
import numpy as np
import cv2

def v_mean(vector):
    max_rgb = np.max(vector)
    min_rgb = np.min(vector)
    return np.mean([max_rgb, min_rgb])

img = mpimg.imread('dog_1.jpg')
gray_img_01 = np.apply_along_axis(v_mean, axis = 2, arr = img) 
print(gray_img_01[0 , 0])
result = cv2.imwrite('gray_dog_1.jpg', gray_img_01)
