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
from resources.app_view import *
from resources.connections import *

from tkinter import messagebox
from addbook import *
from deletebook import *
from viewbook import *
from issuebook import *
from returnbook import *

import PIL.Image
import PIL.ImageTk


root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25
# Adding a background image
background_image = PIL.Image.open("img/lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same :
    newImageSizeHeight = int(imageSizeHeight * n)
else :
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), PIL.Image.ANTIALIAS)
img = PIL.ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image = img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

header(root, "Local Library")
button(root, "Add book details", 'black', 'white', 0.45, 0.1, addBook, 0.28, 0.4)
button(root, "Delete book", 'black', 'white', 0.45, 0.1, deleteBook, 0.28, 0.5)
button(root, "View book list", 'black', 'white', 0.45, 0.1, viewBook, 0.28, 0.6)
button(root, "Issue book to Student", 'black','white', 0.45, 0.1, issueBook, 0.28, 0.7)
button(root, "Return book", 'black', 'white', 0.45, 0.1, returnBook, 0.28, 0.8)

root.mainloop()

