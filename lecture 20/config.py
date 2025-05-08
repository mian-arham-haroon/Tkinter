from tkinter import *

def ok():
    lb.config(text='ok')
    bt.config(bg='#00ffff')

win=Tk()
win.config(bg='#00FFFF')
lb=Label(win,anchor='e',text='Arham',relief='sunken',font=('arial ',20, 'bold roman overstrike'))
# lb.place(x=10,y=10,height=100,width=100)
lb.place(x=10,y=10)
bt=Button(win,text='ok',cursor='boat',command=ok)
bt.place(x=10,y=70,height=40,width=100)








win.mainloop()