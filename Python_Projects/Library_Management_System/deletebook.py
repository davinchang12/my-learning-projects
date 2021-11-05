from tkinter import messagebox
from resources.app_view import *
from resources.connections import *

def deleteBook():
    root = createRoot("Library", (400, 400), "600x500")

    createCanvas(root, "#006B38")

    header(root, "Delete Book")
    labelFrame = textFrame(root)

    text(labelFrame, 'Book ID:', 0.05, 0.5)
    book1 = entryBox(labelFrame, 0.3, 0.5)

    button(root, "SUBMIT", '#d1ccc0', 'black', 0.18, 0.08, lambda: delete(root, book1), 0.28, 0.9)
    button(root, "QUIT", '#f7f1e3', 'black', 0.18, 0.08, root.destroy, 0.53, 0.9)

    root.mainloop()


def delete(root, book1):
    bid = book1.get()
    try:
        delete_tblBooks = "DELETE FROM tblBooks WHERE bid = '" + bid + "';"
        cur.execute(delete_tblBooks)
        con.commit()

        delete_tblBooksIssued = "DELETE FROM tblBooksIssued WHERE bid = '" + bid + "';"
        cur.execute(delete_tblBooksIssued)
        con.commit()

        messagebox.showinfo('Success', 'Book record deleted successfully')
    except:
        messagebox.showinfo('Please check book ID')
    

    print(bid)
    book1.delete(0, END)
    root.destroy()
