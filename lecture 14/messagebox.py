from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo,showerror,showwarning

def ok ():
    # messagebox.showerror('Error','plese dont be give up')
    # messagebox.showwarning('Error','plese dont be give up')
    # messagebox.showinfo('Error','plese dont be give up')
    # showerror(title='arham',message='arham') 
    # # showinfo(title='arham',message='arham') 
    pass
    # showwarning(title='arham',message='arham') 


win=Tk()

bt=Button(win,text='ok',command=ok)
bt.place(x=10,y=10,height=30,width=40)








win.mainloop()
