from tkinter import *
from tkinter import ttk

def ok ():       
    pass


win=Tk()

canvas_0=Canvas(win,bg='red')
canvas_0.place(x=10,y=20,height=700,width=700)
cor=10,10,200,200
canvas_0.create_line(cor,fill='blue')



win.mainloop()
