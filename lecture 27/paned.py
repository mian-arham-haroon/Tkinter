from tkinter import *
from tkinter import ttk

win=Tk()

pd=PanedWindow(orient='horizontal',showhandle=True,sashwidth=4,sashpad=10)
pd.pack(fill='both',expand=True)

l_B=Listbox(win)
l_B.pack(side=LEFT)
pd.add(l_B) 

r_B=Listbox(win)
r_B.pack(side=RIGHT)
pd.add(r_B) 


win.mainloop()