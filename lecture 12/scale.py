from tkinter import *
from tkinter import ttk


def ok(p):
    p=str(var.get())
    lb.config(text=p)


root=Tk()
var=DoubleVar()
sc=Scale(root,command=ok,variable=var,from_=0,to=100,orient='horizontal')
sc.pack()
lb=Label(root,text='',font=(30))
lb.pack()

root.mainloop() 