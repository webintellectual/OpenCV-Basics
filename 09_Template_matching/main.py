import cv2
import numpy as np
img = cv2.imread("09_Template_matching/input.jpg", 0)
template = cv2.imread("09_Template_matching/template.PNG", 0)
h, w = template.shape
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, # different methods for template matching
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, 
    method) # returns location np array having value as degree of match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(
    result) # returns the maximum and minimum values (as well as their positions) in a given array.
    # we locate the highest value (or lower, depending of the type of matching method) 
    # in the result matrix, using the function minMaxLoc()
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: # these methods use min_val of result matrix
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0]+h,location[1]+w) # origin is at top left corner in images
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow("Match", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()