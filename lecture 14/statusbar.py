from tkinter import *
from tkinter import ttk

def ok():
    lb.config(text='go')

win=Tk()

lb=Label(win,text='ready',relief='sunken',anchor='w',)
lb.pack(fill=X,side='bottom' )


bt=Button(win,text='ok',command=ok)
bt.place(x=10,y=10,height=30,width=40)



win.mainloop()
