import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("MDBA.db")

P_id=None
rootR=None

##ROOM BUTTON
def room_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    conn = sqlite3.connect("MDBA.db")
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    conn.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(r1,r3, r2, r4, r5, r6,))
    tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "ROOM ALLOCATED")
    conn.commit()
    conn.close()

def update_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    p = list(conn.execute("Select * from ROOM where PATIENT_ID=?", (r1,)))
    if len(p) != 0:
        conn.execute('UPDATE ROOM SET ROOM_NO=?,ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r3, r2, r4, r5, r6,r1,))
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "ROOM DETAILS UPDATED")
        conn.commit()
    else:
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")
##ROOT FOR DISPLAY ROOM INFO
rootRD=None

##EXIT FOR ROOM_PAGE
def EXITT():
    global rootR
    rootR.destroy()

##FUNCTION FOR ROOM DISPLAY BUTTON
def ROOMD_button():
    global r1,lr1,dis1,lr2,dis2,c1,ii,conn,c1,P_iid
    conn = sqlite3.connect("MDBA.db")
    c1=conn.cursor()
    r1=P_iid.get()
    p=list(c1.execute('select * from  ROOM  where PATIENT_ID=?',(r1,)))
    if (len(p)==0):
        tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
    else:
        t=c1.execute('SELECT NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(r1,));
        for ii in t:
            lr0=tkinter.Label(rootRD,text="PATIENT NAME",fg='blue')
            dis0=tkinter.Label(rootRD,text=ii[0])
            lr0.place(x=50,y=120)
            dis0.place(x=50,y=140)
            lr1=tkinter.Label(rootRD,text="ROOM NO",fg='blue')
            dis1=tkinter.Label(rootRD,text=ii[1])
            lr1.place(x=50,y=170)
            dis1.place(x=50,y=190)
            lr2=tkinter.Label(rootRD,text="ROOM TYPE",fg='blue')
            dis2=tkinter.Label(rootRD,text=ii[2])
            lr2.place(x=50,y=220)
            dis2.place(x=50,y=240)

def exittt():
    rootRD.destroy()

def roomDD():
    global rootRD,ra1,ss,P_iid
    rootRD=tkinter.Tk()
    rootRD.geometry("280x280")
    rootRD.title("ROOM INFO")
    ra1=tkinter.Label(rootRD,text="ENTER PATIENT ID")
    ra1.place(x=20,y=20)
    P_iid=tkinter.Entry(rootRD)
    ss=tkinter.Button(rootRD,text="SEARCH",command=ROOMD_button)
    ra1.place(x=50, y=20)
    P_iid.place(x=50, y=50)
    ss.place(x=70,y=80)
    e=tkinter.Button(rootRD,text="EXIT",command=exittt)
    e.place(x=150,y=80)
    rootRD.mainloop()

def exitt():
    rootR.destroy()

L=None
L1=None
def Room_all():
    global rootR,r_head,P_id,id,room_tl,L,i,room_t,room_nol,room_no,L1,j,ratel,rate,da_l,da ,dd_l,dd,Submit,Update,cr
    rootR=tkinter.Tk()
    rootR.title("ROOM ALLOCATION")
    rootR.geometry("400x400")
    r_head=tkinter.Label(rootR,text="ROOM ALLOCATION",font='Times 13 bold',fg="dark grey")
    r_head.place(x=75,y=10)
    id=tkinter.Label(rootR,text="PATIENT ID")
    id.place(x=30,y=60)
    P_id=tkinter.Entry(rootR)
    P_id.place(x=100,y=60)
    room_tl=tkinter.Label(rootR,text="ROOM TYPE")
    room_tl.place(x=30, y=100)
    L=['SINGLE ROOM: Rs 4500','TWIN SHARING : Rs2500','TRIPLE SHARING: Rs2000']
    room_t= tkinter.Listbox(rootR, width=22, height=3, selectmode='SINGLE', exportselection=0)
    for i in L:
        room_t.insert(tkinter.END,i)
    room_t.place(x=105,y=100)
    room_nol=tkinter.Label(rootR,text="ROOM NUMBER")
    room_nol.place(x=30,y=180)
    L1=['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']
    room_no = tkinter.Listbox(rootR, width=8, height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        room_no.insert(tkinter.END,j)
    room_no.place(x=135,y=180)
    ratel=tkinter.Label(rootR, text="ROOM CHARGES")
    ratel.place(x=30, y=220)
    rate=tkinter.Entry(rootR)
    rate.place(x=130, y=220)
    da_l = tkinter.Label(rootR, text="DATE ADMITTED")
    da_l.place(x=30,y=260)
    da=tkinter.Entry(rootR)
    da.place(x=140,y=260)
    dd_l = tkinter.Label(rootR, text="DATE DISCHARGED(0)")
    dd_l.place(x=30, y=300)
    dd =tkinter.Entry(rootR)
    dd.place(x=155, y=300)
    Submit=tkinter.Button(rootR,text="SUBMIT",command=room_button)
    Submit.place(x=30,y=340)
    Update=tkinter.Button(rootR,text="UPDATE",command=update_button)
    Update.place(x=130,y=340)
    cr=tkinter.Button(rootR,text='ROOM DETAILS',command=roomDD)
    cr.place(x=220,y=340)
    ee=tkinter.Button(rootR,text="EXIT",command=exitt)
    ee.place(x=330,y=340)
    rootR.mainloop()
