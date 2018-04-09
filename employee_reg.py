import tkinter
import sqlite3
rootE=None
var=None


def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=lb.get(tkinter.ACTIVE)
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    conn = sqlite3.connect("MDBA.db")
    conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    rootE=tkinter.Tk()
    rootE.title("Employee registration")
    rootE.geometry('400x400')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="EMPLOYEE REGISTRATION",fg='grey',font="Arial 10 bold")
    H.place(x=50,y=20)
    l1=tkinter.Label(rootE,text="EMPLOYEE ID")
    l1.place(x="50",y="50")
    t1=tkinter.Entry(rootE)
    t1.place(x='170',y='50')
    l2 = tkinter.Label(rootE, text="EMPLOYEE NAME")
    l2.place(x=50,y=80)
    t2 = tkinter.Entry(rootE)
    t2.place(x='170', y='80')
    l3 = tkinter.Label(rootE, text="SEX")
    l3.place(x=50,y=110)
    r1 = tkinter.Radiobutton(rootE, text="MALE", variable=var, value="Male")
    r1.place(x=80, y=110)
    r2 = tkinter.Radiobutton(rootE, text="FEMALE", variable=var, value="Female")
    r2.place(x=150, y=110)
    l4 = tkinter.Label(rootE, text="AGE")
    l4.place(x=50,y=140)
    t3=tkinter.Entry(rootE)
    t3.place(x=80,y=140)
    l5 = tkinter.Label(rootE, text="EMPLOYEE TYPE")
    l5.place(x=50,y=170)
    scrollbar = tkinter.Scrollbar(rootE, width=2)
    scrollbar.place(x=260, y=140)
    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1, width=15,yscrollcommand = scrollbar.set)
    lb.insert(tkinter.END, "DOCTOR")
    lb.insert(tkinter.END, "NURSE")
    lb.insert(tkinter.END, "RECEPTIONIST")
    lb.place(x=150, y=170)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)
    l6=tkinter.Label(rootE,text="SALARY")
    l6.place(x=50,y=200)
    t4=tkinter.Entry(rootE)
    t4.place(x=110,y=200)
    l7 = tkinter.Label(rootE, text="EXPERIENCE")
    l7.place(x=50,y=230)
    t5 = tkinter.Entry(rootE)
    t5.place(x=140,y=230)
    l8 = tkinter.Label(rootE, text="MOBILE NO")
    l8.place(x=50,y=260)
    t6 = tkinter.Entry(rootE)
    t6.place(x=140,y=260)
    l9 = tkinter.Label(rootE, text="EMAIL")
    l9.place(x=50,y=290)
    t7=tkinter.Entry(rootE)
    t7.place(x=90,y=290)
    b1=tkinter.Button(rootE,text="SAVE",command=inp)
    b1.place(x=60,y=320)
    b2=tkinter.Button(rootE,text="DELETE EMPLOYEE",command=delo)
    b2.place(x=110,y=320)
    b3=tkinter.Button(rootE,text="EXIT",command=ex)
    b3.place(x=230,y=320)
    rootE.mainloop()

def delling():
    global d1,de
    de=str(d1.get())
    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?", (de,))
        dme = tkinter.Label(rootDE, text="EMPLOYEE DELETED FROM DATABASE", fg="green")
        dme.place(x=20, y=100)
        conn.commit()
    else:
        error = tkinter.Label(rootDE, text="EMPLOYEE DOESN'T EXIST", fg="Red")
        error.place(x=20, y=100)

rootDE=None
def delo():
    global rootDE,d1
    rootDE=tkinter.Tk()
    rootDE.geometry("250x250")
    rootDE.title("EMPLOYEE DELETION")
    h1=tkinter.Label(rootDE,text="ENTER EMPLOYEE ID TO DELETE :")
    h1.place(x=20,y=10)
    d1=tkinter.Entry(rootDE)
    d1.place(x=20,y=40)
    B1=tkinter.Button(rootDE,text="DELETE",command=delling)
    B1.place(x=20,y=70)
    rootDE.mainloop()


