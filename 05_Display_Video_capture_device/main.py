import cv2

cap = cv2.VideoCapture(0)
while True:  # run a loop to iterate through frames of video
    success, img = cap.read()  # img stores a frame, success is a boolean variable
                                   # which tells weather frame is read successfully or not
    cv2.imshow("Output", img)
    if cv2.waitKey(1) == ord('q'):  # it adds a delay and look for key press 'q' to end loop. ASCII value is matched here.
        break
cap.release()
cv2.destroyAllWindows()