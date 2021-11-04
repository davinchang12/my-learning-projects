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
root.mainloop()

