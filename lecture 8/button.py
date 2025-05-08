from tkinter import *
root=Tk()
root.config(bg='yellow')
def arham():
    lb.config(text='python')
bge=PhotoImage(file="n.png")
bt=Button(root,text='On',image=bge,compound='left',font=('arial 20 bold'),fg='black',bg='red',relief='flat',command=arham) 
bt.place(x=10,y=100)

lb=Label(root,text='hello',font=(30))
lb.place(x=200,y=100)


root.mainloop()