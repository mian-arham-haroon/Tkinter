from tkinter import *

def value_change(var):
    var=value.get()
    lb.config(text=var)



root=Tk()

opt_list=["c#","C++","python","java"]
value=StringVar()
value.set("arham")
op=OptionMenu(root,value,*opt_list,command=value_change)
op.pack()

lb=Label(root,text='')
lb.pack()



























root.mainloop()