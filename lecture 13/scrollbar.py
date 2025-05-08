from tkinter import *
from tkinter import ttk


root=Tk()


text=Text(root,font=(30)) 
text.place(x=10,y=10,height=200,width=400)

sb=Scrollbar(root,orient='vertical',command=text.yview)
sb.place(x=420,y=10,height=200,width=10)
text["yscrollcommand"]=sb.set








root.mainloop()