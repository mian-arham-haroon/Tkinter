from tkinter import *
from tkinter import filedialog

def ok ():
    # var=filedialog.askopenfilenames(initialdir='/',filetypes=(("txtfile","*.txt"),("all file","*.*")),title="arham")
    var=filedialog.askopenfile(initialdir='/',filetypes=(("txtfile","*.txt"),("all file","*.*")),title="arham")
    rd=var.read()
    print(rd)

win=Tk()

bt=Button(win,text='OK',command=ok)
bt.place(x=20,y=20,height=50,width=100)







win.mainloop()

