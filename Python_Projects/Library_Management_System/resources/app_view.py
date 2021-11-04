from tkinter import *

def header(root, textHeader):
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text=textHeader, bg="black", fg="white", font=("Courier", 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

def button(root, buttonText, commandButton, x, y):
    btn1 = Button(root,text=buttonText,bg='black', fg='white', command=commandButton)
    btn1.place(relx=x,rely=y, relwidth=0.45,relheight=0.1)