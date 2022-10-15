import cv2

img = cv2.imread("_Photos/cat.jpg")
img = cv2.resize(img, (400, 400)) # resize to 400x400 px
img2=cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # reduce ratio by half
cv2.imshow("output 1", img)
cv2.imshow("output 2", img2)
cv2.waitKey(0)

cv2.imwrite('01_Image_load_display_resize_rotate/new_img.png', img)
