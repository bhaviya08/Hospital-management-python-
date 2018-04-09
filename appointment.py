import tkinter
import sqlite3
conn=sqlite3.connect("MDBA.db")
rootAA=None

def set():
    global e3,e1,e2,e4,e5,e6,conn
    p1=e1.get()
    p2=e2.get()
    p3=e3.get(tkinter.ACTIVE)
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    conn = sqlite3.connect("MDBA.db")
    conn.execute("Insert into appointment values(?,?,?,?,?,?)",(p1,p2,p3,p4,p5,p6,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")


def appo():
    global rootAA,L,e1,e2,e3,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("500x550")
    rootAA.title("APPOINTMENTS")
    H=tkinter.Label(rootAA,text="APOINTMENTS",fg="blue",font="Arial 10 bold")
    H.place(x=55,y=5)
    l1=tkinter.Label(rootAA,text="PATIENT ID")
    l1.place(x=20,y=30)
    e1=tkinter.Entry(rootAA)
    e1.place(x=100,y=30)
    l2 = tkinter.Label(rootAA,text="DOCTOR ID")
    l2.place(x=20,y=60)
    e2 = tkinter.Entry(rootAA)
    e2.place(x=110, y=60)
    l3 = tkinter.Label(rootAA,text="APPOINTMENT NO")
    l3.place(x=20,y=90)
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50']
    e3=tkinter.Listbox(rootAA, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=140,y=90)
    l4 = tkinter.Label(rootAA,text="APPOINTMENT TIME(HH:MM:SS)")
    l4.place(x=20,y=120)
    e4=tkinter.Entry(rootAA)
    e4.place(x=20,y=145)
    l5 = tkinter.Label(rootAA,text="APPOINTMENT DATE(YYYY-MM-DD)")
    l5.place(x=20,y=170)
    e5=tkinter.Entry(rootAA)
    e5.place(x=20,y=195)
    l6=tkinter.Label(rootAA,text="DESCRIPTION")
    l6.place(x=20,y=220)
    e6=tkinter.Text(rootAA,width=20,height=3)
    e6.place(x=20,y=240)
    scrollbar = tkinter.Scrollbar(rootAA,orient=tkinter.HORIZONTAL)
    scrollbar.place(x=235, y=90)
    e3.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=e3.yview)
    b1=tkinter.Button(rootAA,text="SET APPOINTMENT",command=set)
    b1.place(x=20,y=310)
    b2=tkinter.Button(rootAA,text="Delete Appointment",command=dela)
    b2.place(x=180,y=310)
    b4=tkinter.Button(rootAA,text="TODAYS APPOINTMENTS",command=va)
    b4.place(x=320,y=310)
    rootAA.mainloop()

def remove():
    global e7,edd
    edd=str(e7.get())
    v=list(conn.execute("select * from appointment where AP_NO=?", (edd,)))
    if (len(v)==0):
        errorD = tkinter.Label(rootAA, text="PATIENT APPOINTMENT NOT FIXED",fg="red")
        errorD.place(x=20,y=420)
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(edd,))
        disd1=tkinter.Label(rootAA,text="PATIENT APPOINTMENT DELETED",fg='green')
        disd1.place(x=20,y=420)
        conn.commit()



def dela():
    global e1,e7
    l3 = tkinter.Label(rootAA, text="ENTER APPOINTMENT NO TO DELETE")
    l3.place(x=20, y=340)
    e7=tkinter.Entry(rootAA)
    e7.place(x=20,y=360)
    b3=tkinter.Button(rootAA,text="Delete",command=remove)
    b3.place(x=50,y=380)

rootAP=None

def viewappointment():
    global e8
    ap=str(e8.get())
    vv = list(conn.execute("select * from appointment where AP_DATE=?", (ap,)))
    if (len(vv) == 0):
        errorD = tkinter.Label(rootAA, text="NO APPOINTMENT FOR TODAY", fg="red")
        errorD.place(x=20, y=420)
    else:
        s=conn.execute("Select PATIENT_ID,NAME,AP_NO,EMP_NAME,AP_DATE,AP_TIME from PATIENT NATURAL JOIN employee NATURAL JOIN appointment where AP_DATE=?",(ap,))
        for i in s:
            s1=tkinter.Label(rootAP,text=i,fg='green')
            s1.place(x=10,y=85)


def va():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("500x550")
    rootAP.title("TODAYS APPOINTMENTS")
    h1=tkinter.Label(rootAP,text="ENTER DATE TO VIEW APPOINTMENTS")
    h1.place(x=20,y=20)
    e8=tkinter.Entry(rootAP)
    e8.place(x=20,y=40)
    b5=tkinter.Button(rootAP,text="SEARCH",command=viewappointment)
    b5.place(x=30,y=65)
    rootAP.mainloop()