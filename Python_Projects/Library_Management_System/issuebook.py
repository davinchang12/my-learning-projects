from tkinter import messagebox
from resources.app_view import *
from resources.connections import *

def issueBook():
    root = createRoot("Library", (400, 400), "600x500")

    createCanvas(root, "#D6ED17")

    header(root, "Issue Book")
    labelFrame = textFrame(root)

    text(labelFrame, 'Book ID : ', 0.05, 0.2)
    book1 = entryBox(labelFrame, 0.3, 0.2)

    text(labelFrame, 'Issued To : ', 0.05, 0.4)
    book2 = entryBox(labelFrame, 0.3, 0.4)

    button(root, "ISSUE", '#d1ccc0', 'black', 0.18, 0.08, lambda: issue(root, book1, book2), 0.28, 0.9)
    button(root, "QUIT", '#f7f1e3', 'black', 0.18, 0.08, root.destroy, 0.53, 0.9)

    root.mainloop()

def issue(root, book1, book2):
    bid = book1.get()
    issueto = book2.get()
    
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
            
            if check == 'avail':
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
    
    addIssue = "INSERT INTO tblBooksIssued VALUES('"+ bid +"', '"+ issueto +"');"
    updateStatus = "UPDATE tblBooks SET status = 'issued' WHERE bid = '" + bid + "';"
    
    try:
        if bid in allBid and status == True:
            cur.execute(addIssue)
            con.commit()

            cur.execute(updateStatus)
            con.commit()

            messagebox.showinfo('Success', 'Book issued successfully')
        else:
            messagebox.showinfo('Message', 'Book already Issued')
            
    except:
        messagebox.showinfo('Search Error', 'The value entered is wrong, Try again')
    
    print(bid)
    print(issueto)

    allBid.clear()
    root.destroy()
