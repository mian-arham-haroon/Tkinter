from tkinter import *
from tkinter import ttk

def ok ():       
    pass


win=Tk()

canvas_0=Canvas(win,bg='red')
canvas_0.place(x=10,y=20,height=700,width=700)
# cor=10,10,200,200
# cor=20,20,500,500
# cor=20,20,50,50,40,100
# cor1=700,0,0,700
# canvas_0.create_arc(cor,start=0,extent=180,fill='blue')
# canvas_0.create_oval(cor,fill='blue')
# canvas_0.create_polygon(cor,fill='blue')
# canvas_0.create_text(50,50,text='hello',fill='yellow',font=('arial 20 bold'))
pic=PhotoImage(file='a.png')
canvas_0.create_image(50,50,image=pic)

# canvas_0.create_line(cor,fill='blue')
# canvas_0.create_line(cor1,fill='blue')



win.mainloop()
