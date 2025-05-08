from tkinter import *
from tkinter import messagebox

def ok():

    b=messagebox.askyesno("arham","dont give up")
    if b==True:
        print("arham")
    else:
        pass    
    # b=messagebox.askquestion("arham","dont be give up")

win=Tk()

bt=Button(win,text="ok",command=ok)
bt.place(x=20,y=20,height=30,width=50)







win.mainloop()