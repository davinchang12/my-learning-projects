from tkinter import messagebox
from resources.app_view import *
from resources.connections import *

def returnBook():
    root = createRoot("Library", (400, 400), "600x500")

    createCanvas(root, "#006B38")

    header(root, "Return Book")
    labelFrame = textFrame(root)

    text(labelFrame, 'Book ID : ', 0.05, 0.5)
    book1 = entryBox(labelFrame, 0.3, 0.5)

    button(root, "RETURN", '#d1ccc0', 'black', 0.18, 0.08, lambda: returnID(root, book1), 0.28, 0.9)
    button(root, "QUIT", '#f7f1e3', 'black', 0.18, 0.08, root.destroy, 0.53, 0.9)

def returnID(root, book1):
    bid = book1.get()

    allBid = []

    getBID = "SELECT * FROM tblBooks;"
    try:
        cur.execute(getBID)
        con.commit()

        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "SELECT status FROM tblBooks WHERE bid = '" + bid + "';"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            
            if check == 'issued':
                status = True
            else:
                status = False

        else: 
            messagebox.showinfo('Error', 'Book ID not present')
            allBid.clear()
            root.destroy()
            return
    except:
        messagebox.showinfo('Error', "Can't fetch Book IDs")
        allBid.clear()
        root.destroy()
        return
    
    deleteIssue = "DELETE FROM tblBooksIssued WHERE bid = '" + bid + "';"
    updateStatus = "UPDATE tblBooks SET status = 'avail' WHERE bid = '" + bid + "';"
    
    try:
        if bid in allBid and status == True:
            cur.execute(deleteIssue)
            con.commit()

            cur.execute(updateStatus)
            con.commit()

            messagebox.showinfo('Success', 'Book returned successfully')
        else:
            messagebox.showinfo('Message', 'Please check the book ID')
            
    except:
        messagebox.showinfo('Search Error', 'The value entered is wrong, Try again')
    
    print(bid)

    allBid.clear()
    root.destroy()

    
