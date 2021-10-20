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
    global cache
    global first_frame
    slope_l, slope_r = [], []
    lane_l, lane_r = [], []

    alpha = 0.2

    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1)
            if slope > 0.4:
                slope_r.append(slope)
                lane_r.append(line)
            elif slope < 0.4:
                slope_l.append(slope)
                lane_l.append(line)

        img.shape[0] = min(y1, y2, img.shape[0])
        
        if((len(lane_l) == 0) or len(lane_r) == 0):
            print("No lane detected")
            return 1
        
        slope_mean_l = np.mean(slope_l, axis=0)
        slope_mean_r = np.mean(slope_r, axis=0)
        mean_l = np.mean(lane_l, axis=0)
        mean_r = np.mean(lane_r, axis=0)

        if((slope_mean_l == 0) or (slope_mean_r == 0)):
            print("Dividing by zero")
            return 1
        
        x1_l = int(
            (img.shape[0] - mean_l[0][1] - (slope_mean_l * mean_l[0][0])) / slope_mean_l
        )
        x2_l = int(
            (img.shape[0] - mean_l[0][1] - (slope_mean_l * mean_l[0][0])) / slope_mean_l
        )
        x1_r = int(
            (img.shape[0] - mean_r[0][1] - (slope_mean_r * mean_r[0][0])) / slope_mean_r
        )
        x2_r = int(
            (img.shape[0] - mean_r[0][1] - (slope_mean_r * mean_r[0][0])) / slope_mean_r
        )

        if (x1_l > x1_r):
            x1_l = int((x1_l + x1_r) / 2)
            x1_r = x1_l
            y1_l = int(
                (slope_mean_l * x1_l) + mean_l[0][1] - (slope_mean_l * mean_l[0][0])
            )
            y2_l = int(
                (slope_mean_l * x2_l) + mean_l[0][1] - (slope_mean_l * mean_l[0][0])
            )
            y1_r = int(
                (slope_mean_r * x1_l) + mean_r[0][1] - (slope_mean_r * mean_r[0][0])
            )
            y2_r = int(
                (slope_mean_r * x2_l) + mean_r[0][1] - (slope_mean_r * mean_r[0][0])
            )
        else:
            y1_l = img.shape[0]
            y2_l = img.shape[0]
            y1_r = img.shape[0]
            y2_r = img.shape[0]

        present_frame = np.array([x1_l, y1_l, x2_l, y2_l, x1_r, y1_r, x2_r, y2_r], dtype=np.float32)

        if first_frame == 1:
            next_frame = present_frame
            first_frame = 0
        else:
            prev_frame = cache
            next_frame = ((1 - alpha) * prev_frame) + (alpha * present_frame)

        cv2.line(img, (int(next_frame[0]), int(next_frame[1])), (int(next_frame[2]), int(next_frame[3])), color, thickness)
        cv2.line(img, (int(next_frame[4]), int(next_frame[5])), (int(next_frame[6]), int(next_frame[7])), color, thickness)
    
        cache = next_frame

def weighted_img(img, initial_img, alpha=0.8, beta=1., lamb=0.):
    """
    Return weighted image
    """
    return cv2.addWeigthed(initial_img, alpha, img, beta, lamb)

def process_image(image):
    """
    Return processed each frame of video to detect lane
    """
    pass


