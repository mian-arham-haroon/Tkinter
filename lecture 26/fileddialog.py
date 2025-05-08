from tkinter import *
from tkinter import ttk

win=Tk()

pb=ttk.Progressbar(win,orient='horizontal',length=100,mode='indeterminate')
pb.place(x=0,y=0,height=100,width=200)

bt=Button(win,text="ok",command=pb.start(1))
bt.place(x=20,y=120,height=40,width=80)

bt1=Button(win,text="ok",command=pb.stop)
bt1.place(x=120,y=120,height=40,width=80)




win.mainloop()