import cv2
img = cv2.imread("_Photos/cat.jpg", -1)

# print(img.shape)

slice = img[200:400, 100:400]
img[100:300, 0:300] = slice

cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()