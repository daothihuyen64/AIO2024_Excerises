import numpy as np
import cv2
import matplotlib.image as mpimg


def compute_difference(imgx, imgy):
    difference = cv2.absdiff(imgx, imgy)
    difference_binary = cv2.threshold(difference, 0, 255, cv2.THRESH_BINARY) 
    return difference_binary[1]


img1 = cv2.imread('GreenBackground.png', 1)
img2 = cv2.imread('NewBackground.jpg', 1)
img3 = cv2.imread('Object.png', 1)

img1 = cv2.resize(img1, (678, 381))
img2 = cv2.resize(img2, (678, 381))
img3 = cv2.resize(img3, (678, 381))

cons = [0.07,0.72,0.21]
img1_gray = np.dot(img1,cons)
img2_gray = np.dot(img2,cons)
img3_gray = np.dot(img3,cons)
difference_13 = np.array(compute_difference(img1_gray, img3_gray))
output = np.zeros(img1.shape)
cv2.imwrite('mask_binary.png', difference_13)
h,w = difference_13.shape
print(h,w)
for i in range(h):
    for j in range(w):
        img2_3d = img2[i,j,:]
        img3_3d = img3[i,j,:]
        if(difference_13[i,j] == 0):
            output[i,j,:] = img2_3d
        else:
            output[i,j,:] = img3_3d 

cv2.imwrite('final_output.png', output)
