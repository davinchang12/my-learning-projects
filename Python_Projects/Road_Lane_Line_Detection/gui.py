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
    if not cap1.isOpened():
        print("Can't open the camera")
    flag1, frame1 = cap1.read()
    frame1 = cv2.resize(frame1, (400, 500))

    if flag1 is None:
        print("Major error")
    elif flag1:
        global last_frame1
        last_frame1 = frame1.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLORBGR2RGB)
        img = Image.fromarray(pic)
        imgtk = ImageTK.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_vid)

def show_vid2():
    if not cap2.isOpened():
        print("Can't open the camera")
    flag2, frame2 = cap2.read()
    frame2 = cv2.resize(frame2, (400, 500))

    if flag2 is None:
        print("Major error")
    elif flag2:
        global last_frame2
        last_frame2 = frame2.copy()
        pic2 = cv2.cvtColor(last_frame2, cv2.COLORBGR2RGB)
        img2 = Image.fromarray(pic2)
        imgtk2 = ImageTK.PhotoImage(image=img2)
        lmain2.imgtk2 = imgtk2
        lmain2.configure(image=imgtk2)
        lmain2.after(10, show_vid)


