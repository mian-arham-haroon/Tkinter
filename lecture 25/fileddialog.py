from tkinter import *
from tkinter import filedialog

def ok():
    # var=filedialog.asksaveasfilename(title="ok",initialdir="/",filetypes=(("arham","*.txt"),("all file","*.* ")))
    # var=filedialog.asksaveasfile(title="ok",initialdir="/",filetypes=(("arham","*.txt"),("aarham","*.py"),("all file","*.* ")))
    # var.write('arham')
    var=filedialog.askdirectory(title="ok",initialdir="/",)
    print(var)
win=Tk()

bt=Button(win,text="ok",command=ok)
bt.place(x=20,y=20,height=40,width=80)





win.mainloop()