# Please add database inorder to run this projects.
# Code for MySQL
"""
CREATE DATABASE dbLibrary;
USE dbLibrary;

CREATE TABLE tblBooks(
    bid VARCHAR(20) PRIMARY KEY, 
    title VARCHAR(30), 
    author VARCHAR(30), 
    status VARCHAR(30)
);

CREATE TABLE tblBooksIssued(
    bid VARCHAR(20) PRIMARY KEY, 
    issuedto VARCHAR(30)
);
"""

from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from addbook import *
from deletebook import *
from viewbook import *
from issuebook import *

db_pass = ""
db_user = "root"
db_host = "localhost"
db = "dbLibrary"

con = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db)

cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25
# Adding a background image
background_image = Image.open("img/lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same :
    newImageSizeHeight = int(imageSizeHeight * n)
else :
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image = img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Local Library", bg="black", fg="white", font=("Courier", 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

