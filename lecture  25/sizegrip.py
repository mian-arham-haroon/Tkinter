from tkinter import *
from tkinter import ttk


win=Tk()
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)

sg=ttk.Sizegrip(win)
sg.grid(row=1,sticky=SE)











win.mainloop()

