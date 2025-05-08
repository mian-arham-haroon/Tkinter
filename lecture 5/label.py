from tkinter import *


entry=input('enter name: ')
root=Tk()
var=StringVar()
var.set(entry)
# lb=Label(root,text='arham name\njoni\narham\naleena ',cursor='hand2',font=('arial 90 bold'),bg='red',fg='black',
#          relief='sunken',justify='center')
lb=Label(root,textvariable=var,cursor='hand2',font=('arial 90 bold'),bg='red',fg='black',
         relief='sunken',justify='center')
lb.place(x=200,y=100)
root.config(bg='green')













root.mainloop()