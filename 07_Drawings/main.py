import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640) # ID 3 is used to set width
cap.set(4, 480) # ID 4 is used to set height
while True:
    sucess, frame = cap.read()
    frame = cv2.flip(frame, 1) # To flip the image
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Focus code here:
    img = cv2.line(frame,
    (0,0), # coordinate of one end
    (width,height), # coordinate of other end
    (255,0,0), # color
    10 # thickness
    )
    img = cv2.line(img, # tu put this line over the previous line, take previous generated image as source
    (0,height), (width,0), (0,255,0), 10)
    img = cv2.rectangle(img, 
    (100, 100), # top left coordinate
    (200,200), # bottom right coordinate
    (128,128,128), # colour
    5 # thickness, -1 to fill the rectangle
    )
    img = cv2.circle(img,
    (300,300), # center
    60, # radius
    (0,0,255), # colour
    -1 # to fill (thickness)
    )
    # text:
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Akshay is awesome!",
    (150, height-15), # 	Bottom-left corner of the text string in the image.
    font,
    1.5, # font scale
    (47, 99, 0), # colour
    2, # thickness
    cv2.LINE_AA # line type
    )

    cv2.imshow("Output", img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()