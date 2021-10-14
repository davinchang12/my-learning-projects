from tkinter import *
from rps import RPS

class GUI():
    def __init__(self):
        self.rps = RPS()

        self.root = Tk()
        self.root.geometry("400x400")
        self.root.resizable(0,0)
        self.root.title("Rock, Paper, Scissors")
        self.root.config(bg="seashell3")

        self.result = StringVar()
        self.user_take = StringVar() 
    
    def header(self):
        """
        GUI : header
        """
        Label(self.root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'seashell2').pack()

    def user_choice(self):
        """
        GUI : get user choice
        """
        Label(self.root, text = 'Choose any one: rock, paper, scissors' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
        Entry(self.root, font = 'arial 15', textvariable = self.user_take , bg = 'antiquewhite2').place(x=90 , y = 130)
    
    def button(self):
        """
        GUI : set button position and command
        """
        Entry(self.root, font = 'arial 10 bold', textvariable = self.result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
        Button(self.root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = self.send_user_choice).place(x=150,y=190)
        Button(self.root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = self.reset).place(x=70,y=310)
        Button(self.root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = self.exit).place(x=230,y=310)

    def send_user_choice(self):
        """
        Get result
        """
        self.result.set(self.rps.check(self.user_take.get()))

    def run(self):
        """
        Run GUI
        """
        self.header()
        self.user_choice()
        self.button()
        self.root.mainloop()

    def reset(self):
        """
        Reset game
        """
        self.result.set("")
        self.user_take.set("") 
        self.rps.play_again()

    def exit(self):
        """
        Exit GUI
        """
        self.root.destroy()