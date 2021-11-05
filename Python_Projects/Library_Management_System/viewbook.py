from tkinter import messagebox
from resources.app_view import *
from resources.connections import *

def viewBook():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    createCanvas(root, "#12a4d9")

    header(root, "View Books")
    labelFrame = textFrame(root)

    text(labelFrame, "%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'), 0.07, 0.1)
    text(labelFrame, "----------------------------------------------------------------------------", 0.05, 0.2)

    y = 0.25
    getBooks = "SELECT * FROM tblBooks"
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            text(labelFrame, "%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]), 0.07, y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    button(root, "QUIT", '#f7f1e3', 'black', 0.18, 0.08, root.destroy, 0.4, 0.9)