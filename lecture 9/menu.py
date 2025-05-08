from tkinter import *

def new():
    print("arham")

win=Tk()

main_menu=Menu(win)
win.config(menu=main_menu)


f_menu=Menu(main_menu,tearoff=False)
f_menu.add_command(label="New File",command=new)
f_menu.add_command(label="Open File")
f_menu.add_command(label="Save File")
f_menu.add_command(label="Save as File")
main_menu.add_cascade(label='File',menu=f_menu)

f_menu1=Menu(main_menu,tearoff=False)
f_menu1.add_command(label="New File")
f_menu1.add_command(label="Open File")
f_menu1.add_command(label="Save File")
f_menu1.add_command(label="Save as File")
main_menu.add_cascade(label='menu',menu=f_menu1)










win.mainloop()