import cv2
import pandas as pd
import numpy as np

def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

def get_color_name(r, g, b):
    minimum = 10000
    for i in range(len(col_name)):
        d = abs(r - int(col_name.loc[i, 'r'])) + abs(r - int(col_name.loc[i, 'g'])) + abs(r - int(col_name.loc[i, 'b']))
        if d <= minimum :
            minimum = d
            cname = col_name.loc[i, 'color_name']
    return cname

img_path = 'img/colorpic.jpg'
img = cv2.imread(img_path)

col_name = ['color', 'color_name', 'hex', 'r', 'g', 'b']
color = pd.read_csv('data/colors.csv', names=col_name, header=None)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)