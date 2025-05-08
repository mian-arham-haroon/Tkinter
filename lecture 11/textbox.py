from tkinter import *

def ok():
    varv=tb.get(1.0,END)
    lb.config(text=varv)




root=Tk()
tb=Text(root,font=('arial 18 bold'),fg='black',bg='yellow')
tb.place(x=20,y=20,height=400,width=400 )
var=StringVar()



lb=Label(root,text='',font=('arial 18 bold'))
lb.place(x=600,y=20)

bt=Button(root,text='ok',cursor='hand2',command=ok)
bt.place(x=50,y=440,height=40,width=100)







root.mainloop()