import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640) # ID 3 is used to set width
cap.set(4, 480) # ID 4 is used to set height
cap.set(10, 100)  # ID 10 to set brightness

while True:
    success, frame = cap.read()
    width = int(cap.get(3)) # cap.get is used to retrieve properties , ID 3 is used to retrieve width
    height = int(cap.get(4))
    

    # creating blank canvas using np array
    image = np.zeros(frame.shape, np.uint8) # param2 is data type of image

    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame # top left corner
    image[:height//2, width//2:] = smaller_frame # top right corner
    image[height//2:, :width//2] = smaller_frame # bottom left corner
    image[height//2:, width//2:] = smaller_frame # bottom right corner
    cv2.imshow("Output", image)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()