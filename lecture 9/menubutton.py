from tkinter import *
root=Tk()
# bge=PhotoImage(file="a.png")
# lb=Label(root,image=bge)
# lb.place(x=100,y=100)

def python():
    lb.config(text='file menu')

menu_button=Menubutton(root,text='File')
menu_button.menu=Menu(menu_button,tearoff=0)
menu_button["menu"]=menu_button.menu

menu_button.menu.add_checkbutton(label='file',command=python)
menu_button.menu.add_checkbutton(label='file name')
menu_button.menu.add_checkbutton(label='file path')
menu_button.pack()

lb=Label(root,text='')
lb.pack()


root.mainloop()