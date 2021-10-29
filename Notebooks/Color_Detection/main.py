import cv2
import pandas as pd
import numpy as np

clicked = False
r = g = b = xpos = ypos = 0

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
    for i in range(len(color)):
        d = abs(r - int(color.loc[i, 'r'])) + abs(g - int(color.loc[i, 'g'])) + abs(b - int(color.loc[i, 'b']))
        if d <= minimum :
            minimum = d
            cname = color.loc[i, 'color_name']
    return cname

img_path = 'img/colorpic.jpg'
img = cv2.imread(img_path)

col_name = ['color', 'color_name', 'hex', 'r', 'g', 'b']
color = pd.read_csv('data/colors.csv', names=col_name, header=None)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while(1):
    cv2.imshow('image', img)
    if(clicked):
        cv2.rectangle(img, (20, 20), (750, 60), (b,g,r), -1)

        text = get_color_name(r, g, b) + ' R = ' + str(r) + ' G = ' + str(g) + ' B = ' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        
        if r+g+b >= 600 :
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        
        clicked = False
    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()