import cv2  # openCV library

img = cv2.imread("_Photos/cat.jpg")
cv2.imshow("Output", img)  # param1 is the name of output window
cv2.waitKey(0)  # imshow shows and exits instantly. waitkey adds delay to make output visible
                # param = 0 => infinite delay, Non zero param => that much milisec of delay
# press any key to exit from output window

img2 = cv2.imread("_Photos/cat.jpg", 0)
cv2.imshow("Output2", img2)  # param1 is the name of output window
cv2.waitKey(0)