from tkinter import *
from tkcalendar import Calendar,DateEntry

def ok():
    var=calendar.get_date()
    print(var)

win=Tk()

calendar=DateEntry(win,selectmode="day",year=2020,month=12,day=23)
calendar.place(x=20,y=20)
# calendar=Calendar(win,selectmode="day",year=2020,month=12,day=23)
# calendar.place(x=20,y=20)

bt=Button(win,text="ok",command=ok)
bt.place(x=0,y=0,height=30,width=50)










win.mainloop()
