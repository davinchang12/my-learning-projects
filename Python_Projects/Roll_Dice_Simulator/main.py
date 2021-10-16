import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

dice = [
    'img\dice1.png',
    'img\dice2.png',
    'img\dice3.png',
    'img\dice4.png',
    'img\dice5.png',
    'img\dice6.png'
]

DiceImage = ImageTk.PhotoImage(Image.open(r'img\dice6.png'))
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack(expand=True)

root.mainloop()