from tkinter import *
from tkinter import messagebox
#------------------------------------------------------------#

def ok():
    name=st_name_1.get()

    urdu=urdu_name_1.get()
    english=english_name_1.get()
    sst=sst_name_1.get()
    science=science_name_1.get()
    math=math_name_1.get()
    total=urdu+english+sst+science+math

    per=(total/500)*100

    dev=""

    if (per>60):
        dev="1st dev"
    elif (per<60)and(per>50):
        dev="2nd dev"
    elif (per<50)and(per>40):
        dev="3nd dev"         
    elif (per<40)and(per>50):
        dev="3nd dev"     
    else:
        dev="Fail"      
    messageboxx(name,total,per,dev)      
def messageboxx(*data):
    p1=f'''
    Name : {data[0]}
    Total : {data[1]}
    Persentage : {data[2]}
    Division : {data[3]}'''

    messagebox.askokcancel("Collage",f"{p1}")



#------------------------------------------------------------#
win=Tk()
win.geometry('600x650')
win.resizable(0,0)
win.config(bg='#00FFFF')
win.title('Result Entry')
win.iconbitmap('n.ico')
#------------------------------------------------------------#
school_name=Label(win,bg='lightblue',text='GC COLLAGE',font=('times new roman ',40, 'bold'))
school_name.place(x=100,y=20,height=60,width=400)

st_name_1=StringVar()

st_name=Label(win,bg='lightblue',text='Student Name',font=('times new roman ',20, 'bold'))
st_name.place(x=10,y=100,height=40,width=200)

st_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'),textvariable=st_name_1)
st_entry.place(x=220,y=100,height=40,width=300)
#------------------------------------------------------------#
subject_name=Label(win,bg='lightblue',text='Subject Nunber',font=('times new roman ',30, 'bold'))
subject_name.place(x=100,y=160,height=60,width=400)
#------------------------------------------------------------#
l=['Urdu','English','Science','Maths','SST']


urdu_name_1=DoubleVar()
urdu_name=Label(win,bg='lightblue',text='Urdu',font=('times new roman ',20, 'bold'))
urdu_name.place(x=10,y=240,height=40,width=200)
urdu_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'),textvariable=urdu_name_1)
urdu_entry.place(x=220,y=240,height=40,width=300)

english_name_1=DoubleVar()
english_name=Label(win,bg='lightblue',text='English',font=('times new roman ',20, 'bold'))
english_name.place(x=10,y=300,height=40,width=200)
english_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'),textvariable=english_name_1)
english_entry.place(x=220,y=300,height=40,width=300)

science_name_1=DoubleVar()
science_name=Label(win,bg='lightblue',text='Science',font=('times new roman ',20, 'bold'))
science_name.place(x=10,y=360,height=40,width=200)
science_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'),textvariable=science_name_1)
science_entry.place(x=220,y=360,height=40,width=300)

math_name_1=DoubleVar()
math_name=Label(win,bg='lightblue',text='Math',font=('times new roman ',20, 'bold'))
math_name.place(x=10,y=420,height=40,width=200)
math_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'),textvariable=math_name_1)
math_entry.place(x=220,y=420,height=40,width=300)

sst_name_1=DoubleVar()
sst_name=Label(win,bg='lightblue',text='SST',font=('times new roman ',20, 'bold'))
sst_name.place(x=10,y=480,height=40,width=200)
sst_entry=Entry(win,bg='lightblue',font=('times new roman ',20, 'bold'),textvariable=sst_name_1)
sst_entry.place(x=220,y=480,height=40,width=300)

bt=Button(win,text='Done',font=('times new roman ',20, 'bold'),cursor='boat',command=ok)
bt.place(x=200,y=540,height=60,width=200)

#------------------------------------------------------------#
win.mainloop()