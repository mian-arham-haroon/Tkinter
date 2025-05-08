from tkinter import *
#------------------------------------------------------------#

def ok():
    pass
#------------------------------------------------------------#
win=Tk()
win.geometry('600x700')
win.resizable(0,0)
win.config(bg='#00FFFF')
win.title('Result Entry')
win.iconbitmap('n.ico')
#------------------------------------------------------------#
school_name=Label(win,bg='lightblue',text='GC COLLAGE',font=('times new roman ',40, 'bold'))
school_name.place(x=100,y=20,height=60,width=400)

st_name=Label(win,bg='lightblue',text='Student Name',font=('times new roman ',20, 'bold'))
st_name.place(x=10,y=100,height=40,width=200)

st_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'))
st_entry.place(x=220,y=100,height=40,width=300)
#------------------------------------------------------------#
l=['Urdu','English','Science','Maths','SST']




# bt=Button(win,text='ok',cursor='boat',command=ok)
# bt.place(x=10,y=100,height=40,width=100)

#------------------------------------------------------------#
win.mainloop()