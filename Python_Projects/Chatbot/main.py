from chatbot import ChatBot
from tkinter import *
from tkinter import messagebox

"""
This is Simple Indonesia Chatbot
"""

cb = ChatBot()
def send(event=None):
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "[Anda]: " + msg + '\n\n')
        ChatLog.config(foreground="white", font=("Verdana", 12 ))
        res = cb.jawab(msg)
        ChatLog.insert(END, "[Bot]: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

def about():
    messagebox.showinfo('About','     Chatbot version 1.1')

# GUI
win = Tk()
win.title("DureanBot v1.1 ")

# Menu bar
menubar = Menu(win)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Tutup", command=win.quit)
menubar.add_cascade(label="Menu", menu=menu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Tentang", command=about)
menubar.add_cascade(label="Bantuan", menu=helpmenu)

# Widget
ChatLog = Text(win, bd=0, bg="gray33", height="10", width="60", font="Arial",)
ChatLog.config(state=DISABLED)

scrollbar = Scrollbar(win, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

SendButton = Button(win, font=("Verdana",12,'bold'), text="Kirim", width="24", height=6,
                    bd=0, bg="#191970", activebackground="#0000CD",fg='white',
                    command= send )

EntryBox = Text(win, bd=0, bg="gray33",width="29", height="5", font="Arial", fg="white")

# Grid position
scrollbar.grid(column=3, row=0, sticky='ns')
ChatLog.grid(column=0, row=0, columnspan=3, rowspan=2, sticky='nwse', padx=5, pady=5)
EntryBox.grid(column=0, row=4, sticky='nwse', padx=3, pady=3)
SendButton.grid(column=1, row=4, columnspan=1, sticky='nwse', padx=3, pady=3)

# Resizeable window apps
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)
ChatLog.columnconfigure(0, weight=2)
ChatLog.rowconfigure(0, weight=2)
scrollbar.rowconfigure(0, weight=2)
EntryBox.columnconfigure(0, weight=2)
EntryBox.rowconfigure(4, weight=2)
SendButton.columnconfigure(1, weight=3)
SendButton.rowconfigure(4, weight=3)

win.bind('<Return>', send)
win.config(menu=menubar)
win.mainloop()
