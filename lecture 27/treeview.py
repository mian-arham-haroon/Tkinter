from tkinter import *
from tkinter import ttk


list_data=[("a","a","agmai.com"),("b","b","bgmai.com"),("f","f","fgmai.com"),]
 
win=Tk()

col=("arham","haron","aleena")
tree=ttk.Treeview(win,columns=col,show='headings')

tree.heading("arham",text="aa")
tree.heading("haron",text="ee")
tree.heading("aleena",text="vv")

for data in list_data:
    tree.insert("",END,values=data)

tree.place(x=20,y=20,height=500,width=1000 )

win.mainloop()