from tkinter import*
from tkinter import Toplevel,messagebox
import time
root=Tk()
root.title('Student Management System')
root.config(bg='#F05B56')
root.geometry('1080x720+220+30')
root.iconbitmap('icon.ico')

root.resizable(False,False)
###############################################################################
DataEntryF=Frame(root,bg='#F3DFA2',relief=GROOVE,borderwidth=5)
DataEntryF.place(x=15,y=100,height=600,width=500)
#------------------------------------------------------------------------------
def add():
    addroot=Toplevel(master=DataEntryF)
    addroot.geometry('450x450+261+180')
    addroot.config(bg='#F04842')
    addroot.grab_set()
    addroot.iconbitmap('icon.ico')
    addroot.resizable(False,False)
    #-----------------------------------------------------------------------
    idlabel=Label(addroot,text="Enter ID :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    idlabel.place(x=10,y=20)
    
    Namelabel=Label(addroot,text="Enter Name :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    Namelabel.place(x=10,y=70)
    
    moblabel=Label(addroot,text="Enter Mobile :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    moblabel.place(x=10,y=120)
    
    emailabel=Label(addroot,text="Enter Email :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    emailabel.place(x=10,y=170)
    
    addresslabel=Label(addroot,text="Enter Address :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    addresslabel.place(x=10,y=220)
    
    genlabel=Label(addroot,text="Enter Gender :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    genlabel.place(x=10,y=270)
    
    doblabel=Label(addroot,text="Enter D.O.B. :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    doblabel.place(x=10,y=320)
    #------------------------------------------------------------------------------------------------------------------------------
    idvar=StringVar()
    namevar=StringVar()
    mobvar=StringVar()
    emailvar=StringVar()
    addressvar=StringVar()
    genvar=StringVar()
    dobvar=StringVar()
    
    identry=Entry(addroot,bd=3,font=('sitika',15),textvariable=idvar,width=17)
    identry.place(x=245,y=20)
    
    namentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=namevar,width=17)
    namentry.place(x=245,y=70)
    
    mobentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=mobvar,width=17)
    mobentry.place(x=245,y=120)
    
    emailentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=emailvar,width=17)
    emailentry.place(x=245,y=170)
    
    addressentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=addressvar,width=17)
    addressentry.place(x=245,y=220)
    
    genentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=genvar,width=17)
    genentry.place(x=245,y=270)
    
    dobentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=dobvar,width=17)
    dobentry.place(x=245,y=320)
    
    addroot.mainloop()
    
def search():
    pass
def delstd():
    pass
def update():
    pass
def show():
    pass
def export():
    pass
def exit():
    res=messagebox.askyesno('Notification','Do you want to exit?')
    if (res==True):
        root.destroy()


frontlabel=Label(DataEntryF,text='----------------WELCOME----------------',font=('Granger',22,'bold'),bg='#F3DFA2')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryF,text="1. Add Student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=add)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryF,text="2. Search Student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=search)
searchbtn.pack(side=TOP,expand=True)

delbtn=Button(DataEntryF,text="3. Delete Student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=delstd)
delbtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryF,text="4. Update student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=update)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(DataEntryF,text="5. Show All",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=show)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryF,text="6. Export Data",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=export)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryF,text="7. Exit",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=exit)
exitbtn.pack(side=TOP,expand=True)




ShowDataF=Frame(root,bg='#F3DFA2',relief=GROOVE,borderwidth=5)
ShowDataF.place(x=560,y=100,height=600,width=500)
#################################################################################
count=0
text=''
ss='Welcome to Student Management System'
sliderlabel=Label(root,text=ss,bg='#F3DFA2',font=('Granger',25,'bold'),width=35,relief=RIDGE,borderwidth=4)
sliderlabel.place(x=220,y=5)

def Introslider():
    global count,text
    if (count>=len(ss)):
        count=0
        text=''
        sliderlabel.config(text=text)
    else:
        text+=ss[count]
        sliderlabel.config(text=text)
        count+=1
    sliderlabel.after(250,Introslider)
    
Introslider()  
def tick():
    time_str=time.strftime("%H:%M:%S")
    date_str=time.strftime("%d/%m/%Y")   
    clock.config(text="Date: "+date_str+'\n'+'Time: '+time_str)
    clock.after(20,tick)
    
###################################################################################
clock=Label(root,bg='#F3DFA2',font=('Granger',10,'bold'),relief=GROOVE,borderwidth=4)
clock.place(x=0,y=10)
tick()
#####################################################################################
def Connectdb():
    dbroot=Toplevel()
    dbroot.geometry('450x250+805+250')
    dbroot.config(bg='#F04842')
    dbroot.grab_set()
    dbroot.iconbitmap('icon.ico')
    dbroot.resizable(False,False)
    
    #----------------------------------------
    idlabel=Label(dbroot,text="Enter Host :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    idlabel.place(x=10,y=20)
    
    userlabel=Label(dbroot,text="Enter user :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    userlabel.place(x=10,y=70)
    
    passlabel=Label(dbroot,text="Enter Password :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=18)
    passlabel.place(x=10,y=120)
    
    #---------------------------------------------------------------------------------------------------------------------
    hostval=StringVar()
    userval=StringVar()
    passval=StringVar()
    hostentry=Entry(dbroot,bd=3,font=('sitika',15),textvariable=hostval,width=16)
    hostentry.place(x=252,y=20)
    
    userentry=Entry(dbroot,bd=3,font=('sitika',15),textvariable=userval,width=16)
    userentry.place(x=252,y=70)
    
    passentry=Entry(dbroot,bd=3,font=('sitika',15),textvariable=passval,width=16)
    passentry.place(x=252,y=120)
    #-------------------------------------------------------------------------------------------------------------------------
    submit=Button(dbroot,text="Submit",font=('Granger',19,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=20,activebackground='#F3DFA2',activeforeground='#ED231D',bd=3)
    submit.place(x=110,y=180)
    dbroot.mainloop()
    
    
connect=Button(root,text='Connect to Database', bg='#F3DFA2',font=('Granger',15,'bold'),relief=GROOVE,borderwidth=4,activebackground='#F04842',activeforeground='#F3DFA2',command=Connectdb)   
connect.place(x=890,y=6)
 
root.mainloop()