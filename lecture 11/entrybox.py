from tkinter import *

root=Tk()
def ok ():
    lb1.config(text=var.get())
var=StringVar()
lb=Label(root,text='Email',font=('arial 12 bold'))
lb.place(x=50,y=50,width=100,height=50)

ent=Entry(root,cursor='plus',show='*',justify='center',bd=2,
          textvariable=var)
ent.place(x=50,y=100,width=300,height=50)

bt=Button(root,text='ok',cursor='hand2',command=ok)
bt.place(x=50,y=160,height=20,width=50)

lb1=Label(root,text='',font=('arial 12 bold'))
lb1.place(x=50,y=190,width=100,height=50)






















root.mainloop()