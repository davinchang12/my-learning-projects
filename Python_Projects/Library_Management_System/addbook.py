from tkinter import messagebox
from resources.app_view import *
from resources.connections import *

def addBook():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    createCanvas(root, "#FF6E40")
    
    header(root, "Add Books")
    labelFrame = textFrame(root)

    # Book ID
    text(labelFrame, "Book ID : ", 0.05, 0.2)
    book1 = entryBox(labelFrame, 0.3, 0.2)

    # Title
    text(labelFrame, "Title : ", 0.05, 0.35)
    book2 = entryBox(labelFrame, 0.3, 0.35)

    # Book Author
    text(labelFrame, "Author : ", 0.05, 0.5)
    book3 = entryBox(labelFrame, 0.3, 0.5)

    # Book Status
    text(labelFrame, "Status(Avail/Issued) : ", 0.05, 0.65)
    book4 = entryBox(labelFrame, 0.3, 0.65)

    # Submit Button
    button(root, "SUBMIT", '#d1ccc0', 'black', 0.18, 0.08, lambda: bookRegister(book1, book2, book3, book4), 0.28, 0.9)

    # Quit Button
    button(root, "QUIT", '#f7f1e3', 'black', 0.18, 0.08, root.destroy, 0.53, 0.9)

    root.mainloop()

def bookRegister(book1, book2, book3, book4):
    bid = book1.get()
    title = book2.get()
    author = book3.get()
    status = book4.get().lower()

    insertBooks = "INSERT INTO tblBooks VALUES('"+bid+"', '"+title+"', '"+author+"', '"+status+"');"

    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', 'Book added successfully')
    except:
        messagebox.showinfo('Error', "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)

    