from tkinter import *


data=""

def get_data(value):
    global data
    data=data+str(value)
    var.set(data)

def equal_data():
    global data
    try:
        total=str(eval(data))
        var.set(total)
        data=""
    except:
        var.set("ERROR")    

def clear():
    global data
    data=""
    var.set("")

win=Tk()
win.title('Calculator')
win.config(bg="yellow")
win.iconbitmap('n.ico')
win.geometry('500x560')
win.resizable(0,0)

label_titel=Label(win,text='Calculator',font=('time new roman',50,'bold'),bg="yellow")
label_titel.place(x=90,y=20,height=70,width=320)

var=StringVar()
entry=Entry(win,textvariable=var,relief='sunken',bd=2,font=('time new roman',30,'bold'))
entry.place(x=20,y=110,height=60,width=460)

button_1=Button(win,text='1',font=('time new roman',30,'bold'),command=lambda:get_data(1))
button_1.place(x=20,y=190,height=70,width=115)
button_2=Button(win,text='2',font=('time new roman',30,'bold'),command=lambda:get_data(2))
button_2.place(x=135,y=190,height=70,width=115)
button_3=Button(win,text='3',font=('time new roman',30,'bold'),command=lambda:get_data(3))
button_3.place(x=250,y=190,height=70,width=115)
button_add=Button(win,text='+',font=('time new roman',30,'bold'),command=lambda:get_data('+'))
button_add.place(x=365,y=190,height=70,width=115)

button_4=Button(win,text='4',font=('time new roman',30,'bold'),command=lambda:get_data(4))
button_4.place(x=20,y=260,height=70,width=115)
button_5=Button(win,text='5',font=('time new roman',30,'bold'),command=lambda:get_data(5))
button_5.place(x=135,y=260,height=70,width=115)
button_6=Button(win,text='6',font=('time new roman',30,'bold'),command=lambda:get_data(6))
button_6.place(x=250,y=260,height=70,width=115)
button_sub=Button(win,text='-',font=('time new roman',30,'bold'),command=lambda:get_data('-'))
button_sub.place(x=365,y=260,height=70,width=115)

button_7=Button(win,text='7',font=('time new roman',30,'bold'),command=lambda:get_data(7))
button_7.place(x=20,y=330,height=70,width=115)
button_8=Button(win,text='8',font=('time new roman',30,'bold'),command=lambda:get_data(8))
button_8.place(x=135,y=330,height=70,width=115)
button_9=Button(win,text='9',font=('time new roman',30,'bold'),command=lambda:get_data(9))
button_9.place(x=250,y=330,height=70,width=115)
button_mult=Button(win,text='x',font=('time new roman',30,'bold'),command=lambda:get_data('*'))
button_mult.place(x=365,y=330,height=70,width=115)

button_dot=Button(win,text='.',font=('time new roman',30,'bold'),command=lambda:get_data('.'))
button_dot.place(x=20,y=400,height=70,width=115)
button_0=Button(win,text='0',font=('time new roman',30,'bold'),command=lambda:get_data(0))
button_0.place(x=135,y=400,height=70,width=115)
button_clear=Button(win,text='C',font=('time new roman',30,'bold'),command=clear)
button_clear.place(x=250,y=400,height=70,width=115)
button_div=Button(win,text='/',font=('time new roman',30,'bold'),command=lambda:get_data('/'))
button_div.place(x=365,y=400,height=70,width=115)
# button_equal=Button(win,text='=',font=('time new roman',30,'bold'),command=equal_data)
# button_equal.place(x=365,y=400,height=70,width=115)
button_equal=Button(win,text='=',font=('time new roman',30,'bold'),command=equal_data)
button_equal.place(x=135,y=470,height=70,width=230)


win.mainloop()