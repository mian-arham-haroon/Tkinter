from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askretrycancel

def ok ():
    # ans=messagebox.askretrycancel('arham','keep continously hard')
    ans=askretrycancel(title='arham',message='keep continously hard')
    if ans==True:
        # print('arham')
        ok()
    else:
        lab.config(text='arham')
        # pass    
    # pass


win=Tk()

bt=Button(win,text='ok',command=ok)
bt.place(x=10,y=10,height=30,width=40)

lab=Label(win,text='')
lab.place(x=10,y=40)







win.mainloop()
