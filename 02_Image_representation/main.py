import cv2
img = cv2.imread("_Photos/cat.jpg", -1)

print(img)
print(type(img))
print(img.shape)
print(img.shape[0]) # return number of rows
print(img.shape[1]) # return number of columns

print(img[257][45:400]) # Accessing values of some pixels