import tkinter
from PIL import Image, ImageTk
import random

class RollDice():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('400x400')
        self.root.title('Roll the Dice')

        self.dice = [
            'img\dice1.png',
            'img\dice2.png',
            'img\dice3.png',
            'img\dice4.png',
            'img\dice5.png',
            'img\dice6.png'
        ]

    def rolling_dice(self):
        """
        Roll new dice
        """
        self.DiceImage = ImageTk.PhotoImage(Image.open(random.choice(self.dice)))
        self.ImageDice.configure(image=self.DiceImage)
        self.ImageDice.image = self.DiceImage

    def play(self):
        """
        Make GUI
        """
        self.DiceImage = ImageTk.PhotoImage(Image.open(random.choice(self.dice)))
        self.ImageDice = tkinter.Label(self.root, image=self.DiceImage)
        self.ImageDice.image = self.DiceImage

        self.button = tkinter.Button(self.root, text="Roll the dice", fg="blue", command=self.rolling_dice)
        
        self.ImageDice.pack(expand=True)
        self.button.pack()
        
        self.root.mainloop()



if __name__ == "__main__":
    roll_dice = RollDice()
    roll_dice.play()