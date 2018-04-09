import tkinter
import sqlite3
import tkinter.messagebox
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from RooMT import Room_all
from BILLING import BILLING
from employee_reg import emp_screen
from appointment import appo

conn=sqlite3.connect("MDBA.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("280x350")
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="MENU",font='Times 16 bold italic',fg='grey')
    button1=tkinter.Button(root1,text="1.PATIENT REGISTRATION",command=PAT,bg='light blue',fg='black')
    button2 = tkinter.Button(root1, text="2.ROOM ALLOCATION",bg='light green',fg='black',command=Room_all)
    button3 = tkinter.Button(root1, text="3.EMPLOYEE REGISTRATION",bg='light blue',fg='black',command=emp_screen)
    button4 = tkinter.Button(root1, text="4.BOOK APPOINTMENT",bg='light green',fg='black',command=appo)
    button5 = tkinter.Button(root1, text="5.PATIENT BILL",bg='light blue',fg='black',command=BILLING)
    button6 = tkinter.Button(root1, text="6.EXIT",command=ex,bg='light green',fg='black')
    m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=80,y=100)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=150)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)
    button5.pack(side=tkinter.TOP)
    button5.place(x=80,y=250)
    button6.pack(side=tkinter.TOP)
    button6.place(x=80,y=300)
    root1.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
    conn=sqlite3.connect("MDBA.db")
    conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_dob.get()
    pp6=pat_contact.get()
    pp7=pat_contactalt.get()
    pp8=pat_address.get()
    pp9=pat_CT.get()
    pp10=pat_email.get()
    conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,))
    conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(pp1,pp6,pp7,))
    tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM","DETAILS INSERTED INTO DATABASE")
    conn.commit()


#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    print("CONTACT DATABASE HEAD :921 ")

def nothing1():
    print("MADE BY BHAVIYA BATRA")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title("MEDANTA PATIENT FORM")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXO)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=nothing)
    helpmenu.add_command(label="ABOUT",command=nothing1)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="REGISTRATION FORM",font="Arial 16 bold")
    id=tkinter.Label(rootp,text="PATIENT ID")
    pat_ID=tkinter.Entry(rootp)
    name=tkinter.Label(rootp,text="PATIENT NAME")
    pat_name = tkinter.Entry(rootp)
    sex=tkinter.Label(rootp,text="SEX")
    pat_sex=tkinter.Entry(rootp)
    dob=tkinter.Label(rootp, text="DOB (YYYY-MM-DD)")
    pat_dob=tkinter.Entry(rootp)
    bg=tkinter.Label(rootp, text="BLOOD GROUP")
    pat_BG=tkinter.Entry(rootp)
    c1=tkinter.Label(rootp, text="CONTACT NUMBER")
    pat_contact=tkinter.Entry(rootp)
    c2=tkinter.Label(rootp, text="ALTERNATE CONTACT")
    pat_contactalt=tkinter.Entry(rootp)
    email=tkinter.Label(rootp, text="EMAIL")
    pat_email = tkinter.Entry(rootp)
    ct=tkinter.Label(rootp,text="CONSULTING TEAM / DOCTOR")
    pat_CT=tkinter.Entry(rootp)
    addr=tkinter.Label(rootp, text="ADDRESS")
    pat_address=tkinter.Entry(rootp)
    back=tkinter.Button(rootp,text="<< BACK",command=menu)
    SEARCH=tkinter.Button(rootp,text="  SEARCH >>  ",command=P_display)
    DELETE=tkinter.Button(rootp,text="  DELETE  ",command=D_display)
    UPDATE=tkinter.Button(rootp,text="  UPDATE  ",command=P_UPDATE)
    SUBMIT=tkinter.Button(rootp,text="  SUBMIT  ",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    c2.pack()
    pat_contactalt.pack()
    email.pack()
    pat_email.pack()
    ct.pack()
    pat_CT.pack()
    addr.pack()
    pat_address.pack()
    SUBMIT.pack()
    back.pack(side=tkinter.LEFT)
    UPDATE.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    SEARCH.pack(side=tkinter.LEFT)
    rootp.mainloop()

