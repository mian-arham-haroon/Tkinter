from tkinter import *

def get_data(var):
    var=c.get()
    print(var)

win=Tk()

l=["py","c++","c","java"]
c=StringVar(value=l)
list_box=Listbox(win,listvariable=c,selectmode='extended') 
list_box.place(x=20,y=20,height=300,width=150)

list_box.bind('<<ListboxSelect>>',get_data)











win.mainloop()