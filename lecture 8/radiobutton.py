from tkinter import *
def ok():
    lb.config(text=var.get())
    
root=Tk()
bge=PhotoImage(file="a.png")
var=StringVar()
list_1=(("python","p"),("java","j"),("c++","c"))
for i in list_1:
    radiobutton=Radiobutton(root,text=i[0],value=i[1],variable=var,command=ok)
    # radiobutton.deselect()
    # radiobutton.pack(fill=X)
    radiobutton.pack()
lb=Label(root,text='',font=('arial 20 bold'))
lb.pack()
# bt=Button(root,text="ok",font=('arial 20 bold'),command=ok)
# bt.pack()

# radiobutton1=Radiobutton(root,text=('pnon'),value='aaa',variable=var)
# radiobutton1.deselect()
# radiobutton1.pack()



root.mainloop()