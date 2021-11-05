from tkinter import *

def createCanvas(root, color):
    Canvas1 = Canvas(root)
    Canvas1.config(bg=color)
    Canvas1.pack(expand=True, fill=BOTH)

def header(root, textHeader):
    headingFrame = Frame(root, bg="#FFBB00", bd=5)
    headingFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame, text=textHeader, bg="black", fg="white", font=("Courier", 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

def button(root, buttonText, bgColor, fgColor, width, height, commandButton, x, y):
    btn = Button(root,text=buttonText,bg=bgColor, fg=fgColor, command=commandButton)
    btn.place(relx=x,rely=y, relwidth=width,relheight=height)

def textFrame(root):
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    return labelFrame

def text(root, textBox, x, y):
    lb = Label(root,text=textBox, bg='black', fg='white')
    lb.place(relx=x,rely=y, relheight=0.08)

def entryBox(root, x, y):
    entry = Entry(root)
    entry.place(relx=x,rely=y, relwidth=0.62, relheight=0.08)

    return entry