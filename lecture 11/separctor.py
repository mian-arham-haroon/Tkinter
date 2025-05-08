from tkinter import *
from tkinter import ttk

# def value_change(var):
#     var=value.get()
#     lb.config(text=var)



root=Tk()

# opt_list=["c#","C++","python","java"]
# value=StringVar()
# value.set("arham")
# op=OptionMenu(root,value,*opt_list,command=value_change)
# op.pack()


lb1=Label(root,text='value')
lb1.pack(side='left')

s=ttk.Separator(root,orient=VERTICAL)
s.pack(fill=Y,side='left')       
# s=ttk.Separator(root,orient=HORIZONTAL)
# s.pack(fill=X)       

lb=Label(root,text='ccc')
lb.pack(side='left')



























root.mainloop()