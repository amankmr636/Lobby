from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import random

class Appointment:

    def __init__(self,root):
        self.root=root
        self.root.title("Appointment System")
        self.root.geometry("1040x600+10+10")

        self.var10= StringVar()
        self.var11 = StringVar()
        self.var12 = StringVar()
        self.var13 = StringVar()
        self.var14 = StringVar()
        self.varsearch = StringVar()
        self.remarks=StringVar()

        self.var1=StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6 = StringVar()
        self.var7=StringVar()
        self.var8=StringVar()
        self.var9 = StringVar()

        self.varaid=StringVar()


        z=random.randint(1000,9999)
        self.varaid.set(z)

        tim = datetime.datetime.now().date()
        self.ti = str(tim)


        self.vardate = StringVar()

        TitleLabel=Label(self.root,bd=20,relief=RIDGE,text="Book Your Appointment",fg="orange",bg="white",font=("times new roman",50,"bold"))
        TitleLabel.pack(side=TOP,fill=X)

        #============================Data Frame==========================================================

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=120,width=1280,height=370)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Day Schedule")
        DataFrameLeft.place(x=0,y=5,width=780,height=330)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                   text="Appointments")
        DataFrameRight.place(x=790, y=5, width=440, height=300)

        #=================================Button Frame=======================================================

        ButtonFrame =Frame(self.root,bd=10,relief=RIDGE)
        ButtonFrame.place(x=0,y=490,width=1280,height=60)

        #=================================Detail Frame=======================================================

        DetailFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailFrame.place(x=0, y=550, width=1280, height=120)

        #=====================================Data Frame Left====================================================

        Date=Label(DataFrameLeft,text="Date",padx=2,pady=6, font=("times new roman", 12, "bold"),fg="blue")
        Date.grid(row=8,column=0)

        Date2=Entry(DataFrameLeft,width=30,textvariable=self.vardate)
        Date2.grid(row=8, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select DoctorID from doctable")
        row3 = mycursor.fetchall()

        DoctorId = Label(DataFrameLeft, text="Doctor ID", padx=2, pady=6, font=("times new roman", 12, "bold"))
        DoctorId.grid(row=1, column=0)

        DoctorId2 = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var2)
        DoctorId2["values"]=row3
        DoctorId2.grid(row=1, column=1)


        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select PatientID from pattable")
        row3b = mycursor.fetchall()


        slot1 = Label(DataFrameLeft, text="10:30 AM-11:00 AM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot1.grid(row=2, column=0)

        self.slot1b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),state="readonly",textvariable=self.var3)

        self.slot1b.grid(row=2, column=1)


        AId=Label(DataFrameLeft,text="App ID",padx=2,pady=6, font=("times new roman", 12, "bold"),fg="blue")
        AId.grid(row=9,column=0)

        AId2=Entry(DataFrameLeft,width=30,textvariable=self.varaid)
        AId2.grid(row=9, column=1)


        slot2 = Label(DataFrameLeft, text="11:00 AM - 11:30 AM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot2.grid(row=3, column=0)

        self.slot2b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),state="readonly",textvariable=self.var4)

        self.slot2b.grid(row=3, column=1)



        slot3 = Label(DataFrameLeft, text="11:30 AM - 12:00 AM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot3.grid(row=4, column=0)

        self.slot3b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),state="readonly",textvariable=self.var5)

        self.slot3b.grid(row=4, column=1)

        slot4 = Label(DataFrameLeft, text="12:00 AM - 12:30 AM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot4.grid(row=5, column=0)

        self.slot4b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var6)

        self.slot4b.grid(row=5, column=1)

        slot5 = Label(DataFrameLeft, text="12:30 AM - 01:00 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot5.grid(row=6, column=0)

        self.slot5b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var7)

        self.slot5b.grid(row=6, column=1)


        slot6 = Label(DataFrameLeft, text="02:00 PM - 02:30 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot6.grid(row=7, column=0)

        self.slot6b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var8)

        self.slot6b.grid(row=7, column=1)

        #============================Right Slot==============================================================
        slot7 = Label(DataFrameLeft, text="2:30 PM - 3:00 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot7.grid(row=3, column=2)

        self.slot7b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var9)

        self.slot7b.grid(row=3, column=3)

        slot8 = Label(DataFrameLeft, text="3:00 PM - 3:30 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot8.grid(row=4, column=2)

        self.slot8b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var10)

        self.slot8b.grid(row=4, column=3)

        slot8c = Label(DataFrameLeft, text="3:30 PM - 4:00 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot8c.grid(row=5, column=2)

        self.slot8bc = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var11)

        self.slot8bc.grid(row=5, column=3)


        slot9 = Label(DataFrameLeft, text="4:00 PM - 4:30 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot9.grid(row=6, column=2)

        self.slot9b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var12)

        self.slot9b.grid(row=6, column=3)


        slot10 = Label(DataFrameLeft, text="4:30 PM - 5:00 PM", padx=2, pady=6, font=("times new roman", 12, "bold"))
        slot10.grid(row=7, column=2)

        self.slot10b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),state="readonly", textvariable=self.var13)

        self.slot10b.grid(row=7, column=3)

        #=======================================Search================================================================
        Search = Label(DataFrameLeft, text="Search", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Search.place(x=490, y=240)

        Search2 = Entry(DataFrameLeft, width=30,textvariable=self.varsearch)
        Search2.place(x=550, y=245)

        #================================Data Frame Right=====================================================
        self.textPresciption=Text(DataFrameRight,font=("times new roman", 12, "bold"),width=50,height=13,padx=2,pady=6)
        self.textPresciption.grid(row=0,column=0)

        #================================Prescription=========================================================

        btnPrescription=Button(ButtonFrame,text="Appointment",font=("times new roman", 12, "bold"),bg="purple",command=self.Prescription,fg="white",width=16,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)


        btnUpdate=Button(ButtonFrame,text="Search",font=("times new roman", 12, "bold"),command=self.FetchWho,bg="orange",fg="white",width=16,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=1)


        btnClear=Button(ButtonFrame,text="Clear",font=("times new roman", 12, "bold"),command=self.Clear,bg="red",fg="white",width=16,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=2)

        btnExit=Button(ButtonFrame,text="Exit",font=("times new roman", 12, "bold"),command=self.Exit,bg="black",fg="white",width=16,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=3)

        btnUpdate = Button(ButtonFrame, text="Update", font=("times new roman", 12, "bold"), bg="black",
                                 command=self.update, fg="white", width=16, height=1, padx=2, pady=6)
        btnUpdate.grid(row=0, column=4)

        #===================================Table============================================================
        ScrollX2 = ttk.Scrollbar(DataFrame, orient=HORIZONTAL)

        self.pattable2 = ttk.Treeview(DataFrameLeft, column=("AID", "Date",
                                                         "Doctor ID", "Slot1", "Slot2", "Slot3", "Slot4", "Slot5",
                                                         "Slot6",
                                                         "Slot7", "Slot8", "Slot9", "Slot10", "Slot11"),
                                      xscrollcommand=ScrollX2)

        ScrollX2.pack(side=BOTTOM, fill=X)
        ScrollX2.config(command=self.pattable2.xview)

        self.pattable2.heading("AID", text="AID")
        self.pattable2.heading("Date", text="Date")
        self.pattable2.heading("Doctor ID", text="Doctor ID")
        self.pattable2.heading("Slot1", text="Slot1")
        self.pattable2.heading("Slot2", text="Slot2")
        self.pattable2.heading("Slot3", text="Slot3")
        self.pattable2.heading("Slot4", text="Slot4")
        self.pattable2.heading("Slot5", text="Slot5")
        self.pattable2.heading("Slot6", text="Slot6")
        self.pattable2.heading("Slot7", text="Slot7")
        self.pattable2.heading("Slot8", text="Slot8")
        self.pattable2.heading("Slot9", text="Slot9")
        self.pattable2.heading("Slot10", text="Slot10")
        self.pattable2.heading("Slot11", text="Slot11")

        self.pattable2.column("AID", width=70)
        self.pattable2.column("Date", width=70)
        self.pattable2.column("Doctor ID", width=100)
        self.pattable2.column("Slot1", width=70)
        self.pattable2.column("Slot2", width=70)
        self.pattable2.column("Slot3", width=70)
        self.pattable2.column("Slot4", width=70)
        self.pattable2.column("Slot5", width=70)
        self.pattable2.column("Slot6", width=70)
        self.pattable2.column("Slot7", width=70)
        self.pattable2.column("Slot8", width=70)
        self.pattable2.column("Slot9", width=70)
        self.pattable2.column("Slot10", width=70)
        self.pattable2.column("Slot11", width=70)

        self.pattable2.place(x=350, y=20, width=380, height=50)

        # ----------------------------------Scroll Bar--------------------------------------------

        # ----------------------------------Scroll Bar--------------------------------------------

        ScrollX = ttk.Scrollbar(DetailFrame, orient=HORIZONTAL)
        ScrollY = ttk.Scrollbar(DetailFrame, orient=VERTICAL)
        self.pattable = ttk.Treeview(DetailFrame, column=("AID", "Date",
                                                          "Doctor ID", "Slot1", "Slot2", "Slot3", "Slot4", "Slot5",
                                                          "Slot6",
                                                          "Slot7", "Slot8", "Slot9", "Slot10", "Slot11"),
                                     xscrollcommand=ScrollX,
                                     yscrollcommand=ScrollY)

        ScrollX.pack(side=BOTTOM, fill=X)
        ScrollY.pack(side=RIGHT, fill=Y)

        ScrollX.config(command=self.pattable.xview)
        ScrollY.config(command=self.pattable.yview)

        self.pattable.heading("AID", text="AID")
        self.pattable.heading("Date", text="Date")
        self.pattable.heading("Doctor ID", text="Doctor ID")
        self.pattable.heading("Slot1", text="Slot1")
        self.pattable.heading("Slot2", text="Slot2")
        self.pattable.heading("Slot3", text="Slot3")
        self.pattable.heading("Slot4", text="Slot4")
        self.pattable.heading("Slot5", text="Slot5")
        self.pattable.heading("Slot6", text="Slot6")
        self.pattable.heading("Slot7", text="Slot7")
        self.pattable.heading("Slot8", text="Slot8")
        self.pattable.heading("Slot9", text="Slot9")
        self.pattable.heading("Slot10", text="Slot10")
        self.pattable.heading("Slot11", text="Slot11")

        self.pattable.column("AID", width=70)
        self.pattable.column("Date", width=70)
        self.pattable.column("Doctor ID", width=100)
        self.pattable.column("Slot1", width=70)
        self.pattable.column("Slot2", width=70)
        self.pattable.column("Slot3", width=70)
        self.pattable.column("Slot4", width=70)
        self.pattable.column("Slot5", width=70)
        self.pattable.column("Slot6", width=70)
        self.pattable.column("Slot7", width=70)
        self.pattable.column("Slot8", width=70)
        self.pattable.column("Slot9", width=70)
        self.pattable.column("Slot10", width=70)
        self.pattable.column("Slot11", width=70)

        self.pattable.pack(fill=BOTH, expand=1)
        self.FetchData()
        self.pattable.bind("<ButtonRelease-1>", self.medget)
        #=====================================Functionality==================================

    def PrescriptionData(self):
        if self.var2.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
            mycursor=conn.cursor()
            mycursor.execute("insert into apttable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.varaid.get(),self.vardate.get(),
                                 self.var2.get(),self.var3.get(),self.var4.get(),self.var5.get(),self.var6.get(),self.var7.get()
                                 ,self.var8.get(),self.var9.get(),self.var10.get(),self.var11.get(),self.var12.get(),self.var13.get()))

            conn.commit()
            self.FetchData()
            conn.close()
            messagebox.showinfo("Success","Data inserted")

    def FetchData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
        mycursor=conn.cursor()
        mycursor.execute("select * from apttable")

        row=mycursor.fetchall()

        if len(row)!=0:
            self.pattable.delete(*self.pattable.get_children())
            for i in row:
                self.pattable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def FetchWho(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM apttable WHERE DoctorID=%s",(self.var2.get(), ))
        row3=mycursor.fetchall()
        if len(row3)!=0:
            self.pattable2.delete(*self.pattable2.get_children())
            for i in row3:
                self.pattable2.insert("",END,values=i)
            conn.commit()
        conn.close()

    def Prescription(self):

        self.textPresciption.insert(END, "Date:\t\t" + self.ti + "\n")
        self.textPresciption.insert(END,"Doctor ID:\t\t" +  self.var2.get()+  "\n")
        self.textPresciption.insert(END, "10:30-11:00:\t\t" + self.var3.get() + "\n")
        self.textPresciption.insert(END, "11:00-11:30:\t\t" + self.var4.get() + "\n")
        self.textPresciption.insert(END, "11:30-12:00:\t\t" +  self.var5.get() + "\n")
        self.textPresciption.insert(END, "12:00-12:30:\t\t"   +  self.var6.get() + "\n")
        self.textPresciption.insert(END, "12:30-01:00:\t\t"+  self.var7.get() + "\n")
        self.textPresciption.insert(END, "02:00-02:30:\t\t" + self.var8.get() + "\n")
        self.textPresciption.insert(END, "02:30-03:00:\t\t"+  self.var9.get() + "\n")
        self.textPresciption.insert(END, "03:00-03:30:\t\t" + self.var10.get() + "\n")
        self.textPresciption.insert(END, "03:30-04:00:\t\t"+  self.var11.get() + "\n" )
        self.textPresciption.insert(END, "04:00-04:30:\t\t" + self.var12.get() + "\n")
        self.textPresciption.insert(END, "04:30-05:00:\t\t" + self.var13.get() + "\n")
        self.textPresciption.insert(END,"---------------------------------------\n\n")
        messagebox.showinfo("Success","Appointment Added")


    def Clear(self):

        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("")
        self.var6.set("")
        self.var7.set("")
        self.var8.set("")
        self.var9.set("")
        self.var10.set("")
        self.var11.set("")
        self.var12.set("")
        self.var13.set("")

        self.textPresciption.delete("1.0",END)

    def Exit(self):
        Ex=messagebox.askyesno("Book Your Appointment","Confirm Exit")
        if Ex>0:
            self.root.destroy()
            return

    def printfun(self):

        self.predata=self.textPresciption.get(1.0,END)
        f1=open("Prescriptions/"+str(self.varaid.get())+".txt",'w')
        f1.write(self.predata)
        f1.close()

    def update(self):
        if self.var2.get() == "" or self.vardate.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                           database="pharma")
            mycursor = conn.cursor()
            mycursor.execute(
                "update apttable set Slot1=%s,Slot2=%s,Slot3=%s,Slot4=%s,Slot5=%s,Slot6=%s,Slot7=%s,Slot8=%s,Slot9=%s,"
                "Slot10=%s,Slot11=%s where DoctorID=%s",
                ( self.var3.get(), self.var4.get(), self.var5.get(), self.var6.get(), self.var7.get(),
                  self.var8.get(), self.var9.get(), self.var10.get(), self.var11.get(),self.var12.get(),self.var13.get(), self.var2.get()))

            conn.commit()
            self.FetchData()
            conn.close()
            messagebox.showinfo("Success", "Data Updated")

    def medget(self, event=""):


        cursorrow = self.pattable.focus()
        content = self.pattable.item(cursorrow)
        row = content["values"]

        self.varaid.set(row[0])
        self.vardate.set(row[1])
        self.var2.set(row[2])
        self.var3.set(row[3])
        self.var4.set(row[4])
        self.var5.set(row[5])
        self.var6.set(row[6])
        self.var7.set(row[7])
        self.var8.set(row[8])
        self.var9.set(row[9])
        self.var10.set(row[10])
        self.var11.set(row[11])
        self.var12.set(row[12])
        self.var13.set(row[13])

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select PatientID from pattable")
        row3b = mycursor.fetchall()


        if(int(self.var3.get())==0):
            self.slot1b["values"] = row3b
        if (int(self.var4.get()) == 0):
            self.slot2b["values"] = row3b
        if (int(self.var5.get()) == 0):
            self.slot3b["values"] = row3b
        if (int(self.var6.get()) == 0):
            self.slot4b["values"] = row3b
        if (int(self.var7.get())== 0):
            self.slot5b["values"] = row3b
        if (int(self.var8.get()) == 0):
            self.slot6b["values"] = row3b
        if (int(self.var9.get()) == 0):
            self.slot7b["values"] = row3b
        if (int(self.var10.get()) == 0):
            self.slot8b["values"] = row3b
        if (int(self.var11.get()) == 0):
            self.slot8bc["values"] = row3b
        if (int(self.var12.get()) == 0):
            self.slot9b["values"] = row3b
        if (int(self.var13.get()) == 0):
            self.slot10b["values"] = row3b


if __name__=="__main__":

    root=Tk()
    ob=Appointment(root)
    root.mainloop()

