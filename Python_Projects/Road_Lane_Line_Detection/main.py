import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import matplotlib.image as mpimg
from moviepy.editor import VideoFileClip
import math

def interested_region(img, vertices):
    """
    Return ROI

    Applying frame masking and find region of interest
    """
    if(len(img.shape) > 2): # Check if image is grayscale or not
        mask_color_ignore = (255,) * img.shape[2]
    else:
        mask_color_ignore = 255

    cv2.fillPoly(np.zeros_like(img), vertices, mask_color_ignore)
    return cv2.bitwise_and(img, np.zeros_like(img)) # return merged img of roi

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    Return Line

    Applying Hough Transform
    """
    # Convert pixels to line
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    lines_drawn(line_img, lines)
    return line_img

def lines_drawn(img, lines, color=[255, 0, 0], thickness=6):
    """
    Create two lines in each frame
    """
    pass

def weighted_img(img, initial_img, alpha=0.8, beta=1., lamb=0.):
    """
    Return weighted image
    """
    pass

def process_image(image):
    """
    Return processed each frame of video to detect lane
    """
    pass


