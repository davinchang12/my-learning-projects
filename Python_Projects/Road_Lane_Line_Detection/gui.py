import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTK
import os
import numpy as np

global last_frame1
global last_frame2
global cap1
global cap2

last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
last_frame2 = np.zeros((480, 640, 3), dtype=np.uint8)

cap1 = cv2.VideoCapture("vid/input.mp4")
cap2 = cv2.VideoCapture("vid/output.mp4")

def show_vid():
    pass

def show_vid2():
    pass


