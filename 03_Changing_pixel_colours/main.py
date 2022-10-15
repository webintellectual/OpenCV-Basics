import cv2
import numpy as np
img = cv2.imread("_Photos/cat.jpg")

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0, 255)]

cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()