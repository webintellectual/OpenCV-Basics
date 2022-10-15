## cv2.imread(\<path>, \<mode>)
### modes:
- cv::IMREAD_UNCHANGED = -1,
- cv::IMREAD_GRAYSCALE = 0,
- cv::IMREAD_COLOR = 1,
- cv::IMREAD_ANYDEPTH = 2,
- cv::IMREAD_ANYCOLOR = 4,
- cv::IMREAD_LOAD_GDAL = 8,
- cv::IMREAD_REDUCED_GRAYSCALE_2 = 16,
- cv::IMREAD_REDUCED_COLOR_2 = 17,
- cv::IMREAD_REDUCED_GRAYSCALE_4 = 32,
- cv::IMREAD_REDUCED_COLOR_4 = 33,
- cv::IMREAD_REDUCED_GRAYSCALE_8 = 64,
- cv::IMREAD_REDUCED_COLOR_8 = 65,
- cv::IMREAD_IGNORE_ORIENTATION = 128

## cv2.rotate(\<input_array>, \<output_array>, \<rotate_code>)
### rotate codes:
- ROTATE_90_CLOCKWISE
- ROTATE_180 
    - Rotates 180 degrees clockwise
- ROTATE_90_COUNTERCLOCKWISE 

## cv2.imread(\<new file name\>, \<modified image\>)
<img src="new_img.png"/>