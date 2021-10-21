# This is only detect a image.
# You can use this for future improvements for detecting videos.

import numpy as np
import cv2

def interested_region(img, vertices):
    """
    Return ROI

    Applying frame masking and find region of interest
    """
    if(len(img.shape) > 2): # Check if image is grayscale or not
        mask_color_ignore = (255,) * img.shape[2]
    else:
        mask_color_ignore = 255

    temp = np.zeros_like(img, dtype=np.uint8)
    cv2.fillPoly(temp, vertices, mask_color_ignore)
    return cv2.bitwise_and(img, temp) # return merged img of roi

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    Return Line

    Applying Hough Transform
    """
    # Convert pixels to line
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    return lines

def display_lines(image, lines):
    """
    Return road lane line
    """
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 5)
    return image

def process_image(image):
    """
    Return processed each frame of video to detect lane
    """
    global first_frame

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

    mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(gray_image, 200, 255)
    mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
    mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)

    gauss_gray = cv2.GaussianBlur(mask_yw_image, (5, 5), 0)
    canny_edges = cv2.Canny(gauss_gray, 50, 150)

    imshape = image.shape
    
    lower_left = [imshape[1] / 9, imshape[0]]
    lower_right = [imshape[1] - imshape[1] / 9, imshape[0]]
    top_left = [imshape[1] / 2 - imshape[1] / 8, imshape[0] / 2 + imshape[0] / 10]
    top_right = [imshape[1] / 2 + imshape[1] / 8, imshape[0] / 2 + imshape[0] / 10]
    vertices = [np.array([lower_left, top_left, top_right, lower_right], dtype=np.int32)]
    roi_images = interested_region(canny_edges, vertices)

    theta = np.pi / 180

    line_image = hough_lines(roi_images, 4, theta, 30, 100, 180)
    result = display_lines(image, line_image)
    
    return result

if __name__ == "__main__":
    first_frame = 1
    image = "img/testimg.jpg"
    image = cv2.imread(image)
    result = process_image(image)

    cv2.imshow('image', result)
    cv2.waitKey()