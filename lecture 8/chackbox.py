from tkinter import *
def text():
    # print(var.get())
    lb.config(text=var.get())
root=Tk()
root.config(bg='yellow')
# var=BooleanVar()
var=StringVar()
cb=Checkbutton(root,text='arham',font=('arial 20 bold'),variable=var,onvalue='python',offvalue='java',command=text)
cb.deselect()
cb.pack()
lb=Label(root,text='',font=('arial 12 bold'),)
lb.pack()
# b=Button(root,text='arham',font=('arial 20 bold'),command=text)
# b.pack()

root.mainloop()