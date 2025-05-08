from tkinter import *
from tkinter import ttk
def ok ():
    lb.config(text=str(var.get()))


root=Tk()
var=IntVar()
sb=Spinbox(root,command=ok,from_=0,to=10,textvariable=var,wrap=True,font=(30))
sb.place(x=10,y=10,height=30,width=90)

lb=Label(root,text='',font=(30))
lb.place(x=10,y=60)


















root.mainloop()