from tkinter import *
from tkinter import ttk

def ok ():       
    pass


win=Tk()



f1=Frame(win,bg='yellow',bd=2,relief='raised')
f1.place(x=100,y=100,height=200,width=200)
bt=Button(f1,text='ok',command=ok)
bt.place(x=10,y=10,height=30,width=40)

f2=Frame(win,bg='red')
f2.place(x=600,y=600,height=200,width=200)
lab=Label(f2,text='')
lab.place(x=10,y=40)







win.mainloop()
