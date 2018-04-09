import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("MDBA.db")

#variables
rootB=None

def date_up():
    global b1,b2
    b1 = P_id.get()
    b2 = dd.get()
    conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "DISCHARGE DATE UPDATED")

def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("MDBA.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
    conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "BILLING DATA SAVED")

def calci():
    global b1
    conn = sqlite3.connect("MDBA.db")
    u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
    conn.commit()
    for ii in u:
        pp=tkinter.Label(rootB,text="TOTAL AMOUNT OUTSTANDING",fg='red',font='Arial 8 bold')
        pp.place(x="200", y='260')
        uu=tkinter.Label(rootB,text=ii[0])
        uu.place(x="230",y='290')

L1=None
L2=None
L3=None
L4=None

def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,dd,cost,med,med_q,price,treat_1,treat_2,cost_t,j,jj,jjj,jjjj,L2,L3,L4
    rootB=tkinter.Tk()
    rootB.geometry("450x350")
    rootB.title("BILLING SYSTEM")
    head=tkinter.Label(rootB,text="PATIENT BILL",font="Arial 16 bold italic",fg='grey')
    head.place(x=100,y=10)
    id = tkinter.Label(rootB, text="PATIENT ID")
    id.place(x=20, y=60)
    P_id = tkinter.Entry(rootB)
    P_id.place(x=100, y=60)
    dd_l = tkinter.Label(rootB, text="DATE DISCHARGED")
    dd_l.place(x=20, y=100)
    dd = tkinter.Entry(rootB)
    dd.place(x=135, y=100)
    ddp=tkinter.Button(rootB,text="UPDATE DISCHARGE DATE",command=date_up)
    ddp.place(x=270,y=100)
    treat = tkinter.Label(rootB, text="SELECT TREATMENT")
    treat.place(x=20, y=140)
    L1 = ["CONSULATION","SURGERY","LAB TEST"]
    treat_1= tkinter.Listbox(rootB, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=140,y=140)
    treat_c = tkinter.Label(rootB, text="CODE")
    treat_c.place(x=240, y=140)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB, width=6, height=1, selectmode='SINGLE', exportselection=0)
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.place(x=280, y=140)
    costl= tkinter.Label(rootB, text="COST ₹")
    costl.place(x=315, y=140)
    cost_t = tkinter.Entry(rootB,width=5)
    cost_t.place(x=350, y=140)
    med1 = tkinter.Label(rootB, text="SELECT MEDICINE")
    med1.place(x=20, y=180)
    L3 = ["NEURAL", "FANEKPLUS", "DISPRIN","DOLO+","BANDAGE","DIGENE"]
    med = tkinter.Listbox(rootB, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=140, y=180)
    med_ql = tkinter.Label(rootB, text="QUANTITY")
    med_ql.place(x=240, y=180)
    L4 = [1,2,3,4,5,6,7,8,9,10]
    med_q = tkinter.Listbox(rootB, width=4, height=1, selectmode='SINGLE', exportselection=0)
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.place(x=280, y=180)
    pricel = tkinter.Label(rootB, text="PRICE ₹")
    pricel.place(x=315, y=180)
    price = tkinter.Entry(rootB, width=5)
    price.place(x=360, y=180)
    b1=tkinter.Button(rootB,text="GENERATE BILL",command=calci)
    b1.place(x="200",y="210")
    b2 = tkinter.Button(rootB, text="UPDATE DATA", command=up)
    b2.place(x="100", y="210")
    ee=tkinter.Button(rootB,text="EXIT",command=exitt)
    ee.place(x='310',y='210')
    rootB.mainloop()
