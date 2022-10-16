import cv2
import numpy as np
img = cv2.imread("_Photos/chessboard.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert coloured image to grayscale

corners = cv2.goodFeaturesToTrack(gray, 
100, # max number of corners to detect
0.01, # quality level or degree of confidence
10 # minimum distance b/w any two corners. Helps in avoiding detection of multiple corners at same place
)
corners = np.int0(corners) # corners returned above are in float. So, converting them to integers.
print(corners.shape) # 79 rows, 1 col. Each row contains one corner point like: [pt] = [[x,y]]
for corner in corners:
    x,y = corner.ravel() # [[x,y]] -> [x,y]. It converts complex combinations of lists into single list
    cv2.circle(img, (x,y), 7, (0,0,255), -1) # drawing circle dots at corners

# Joining every two corners (Playing around)
img2 = img.copy()
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0]) # In each row we have [point] = [[x,y]]. 
                                #Extract point and convert to tuple to use in cv::circle fxn
        corner2 = tuple(corners[j][0])
        color = np.random.randint(0, 255, size=3) # return a list of three rand numbers in passed range
        # Converting numpy integers to regular python integers:
        color = map(lambda x: int(x), color) # map numpy intgers of color list to regular integers
        color = tuple(color) # converting list of three random integers to a tuple to use in cv::line function
        cv2.line(img2, corner1, corner2, color, 1)

cv2.imshow("output", img)
cv2.imshow("output 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()