from tkinter import *


# entry=input('enter name: ')
root=Tk()
# var=StringVar()
# var.set(entry)
# lb=Label(root,text='arham name\njoni\narham\naleena ',cursor='hand2',font=('arial 90 bold'),bg='red',fg='black',
# #          relief='sunken',justify='center')
# lb=Label(root,textvariable=var,cursor='hand2',font=('arial 90 bold'),bg='red',fg='black',
#          relief='sunken',justify='center')
# lb=Label(root,text='arham',underline=2,cursor='hand2',font=('arial 90 bold'),bg='red',fg='black',
#          relief='sunken',justify='center')
bge=PhotoImage(file=r"C:\Users\DELL\Desktop\Tkinter\lecture 6\a.png")
# lb=Label(root,image=bge,bg='green',text='arham',compound='top',font=('arial 40 bold'),fg='black',)
lb=Label(root,image=bge,bg='green')
lb.place(x=100,y=100,height=500,width=1000)
root.config(bg='green')













root.mainloop()