import cv2
cap = cv2.VideoCapture(0) # 0 for default camera, other IDs in case of other cameras plugged
cap.set(3, 640) # ID 3 is used to set width
cap.set(4, 480) # ID 4 is used to set height
cap.set(10, 100)  # ID 10 to set brightness

while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
