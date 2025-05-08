from tkinter import *
from tkinter import ttk

def ok (event):       
    print('arham')
def end (event):       
    print('consequency')


win=Tk()

bt=Button(win,text=('ok'))
bt.bind('<Leave>',ok)
bt.bind('<Leave>',end,add='+')
bt.unbind('<Leave>')
bt.place(x=20,y=20,height=100,width=100)


win.mainloop()
