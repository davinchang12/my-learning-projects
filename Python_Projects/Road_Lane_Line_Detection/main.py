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
    pass

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    Return Line

    Applying Hough Transform
    """
    pass

def lines_drawing(img, lines, color=[255, 0, 0], thickness=6):
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


