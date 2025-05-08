from tkinter import *

win=Tk()

win.title("arham")
win.attributes('-alpha',0.9)
# win.geometry(f'{win.winfo_screenheight}x{win.winfo_screenwidth}')
# win.iconbitmap('n.ico')
win.config(bg='yellow')
# lab=Label(win,text="arham",font=("arial 20 bold"),bg="green",fg="black")
# # lab.pack(padx=100,pady=100,ipadx=20,ipady=20,fill='both',expand=True)
# lab.grid(row=0,column=0,padx=20,pady=20)
# lab1.grid(row=0,column=1,padx=20,pady=20,columnspan=2)
lab1=Label(win,text="aqqqrham",font=("arial 20 bold"),bg="green",fg="black")
lab1.place(x=200,y=200,height=100,width=200)
lab1=Label(win,text="aham",font=("arial 20 bold"),bg="green",fg="black")
# lab1.place(relx=0.4,rely=0.4,relwidth=0.)
lab1.place(x=200,y=320)




















win.mainloop()