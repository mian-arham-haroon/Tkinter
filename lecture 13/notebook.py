from tkinter import *
from tkinter import ttk


root=Tk()


nb=ttk.Notebook(root)
nb.pack(fill='both',expand=TRUE)

f1=Frame(nb)
f1.pack(fill='both',expand=True)
lb1=Label(f1,text='arham')
lb1.place(x=10,y=10)
f2=Frame(nb)
f2.pack(fill='both',expand=True)
lb2=Label(f2,text='haroon')
lb2.place(x=10,y=10)
nb.add(f1,text='arham')
nb.add(f2,text='haroon')







root.mainloop()