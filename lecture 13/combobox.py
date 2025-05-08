from tkinter import *
from tkinter import ttk

def ok ():
    p=var.get()
    lb.config(text=p)

root=Tk()
var=StringVar()
l=["c","c++","java","python"]
cb=ttk.Combobox(root,values=l,textvariable=var,state='readonly',height=20,width=40,justify='center',font=('arial 10 bold'))
cb.set('language')
cb.pack()
lb=Label(root,text='',font=('arial 10 bold'))
lb.pack()
bt=Button(root,text='ok',command=ok)
bt.pack()



root.mainloop()