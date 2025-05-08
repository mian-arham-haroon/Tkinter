from tkinter import *

win=Tk()

win.title("arham")
win.attributes('-alpha',0.9)
# win.geometry(f'{win.winfo_screenheight}x{win.winfo_screenwidth}')
# win.iconbitmap('n.ico')
win.config(bg='yellow')
# var=StringVar(win,value='arham')
# var=StringVar(win,value='pyhon',name='2')
# var=IntVar(win,value=22,name='3')
# var=BooleanVar(win,value=0,name='3')
var=DoubleVar(win,value=100000.000001,name='3')
# var.set('arham')
print(var.get())















win.mainloop()