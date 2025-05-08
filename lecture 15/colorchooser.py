from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor

def ok ():       
    # colorchooser.askcolor(title='arham')
    ans=askcolor(title='arham')
    win.config(bg=ans[1])


win=Tk()

bt=Button(win,text='ok',command=ok)
bt.place(x=10,y=10,height=30,width=40)

lab=Label(win,text='')
lab.place(x=10,y=40)







win.mainloop()
