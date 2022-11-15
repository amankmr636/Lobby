from tkinter import *
from tkinter import ttk


import datetime
from tkinter import messagebox
import mysql.connector
import random

class Hospital:

    def __init__(self,root):
        self.root=root
        self.root.title("Patient Information System")
        self.root.geometry("1040x600+10+10")

        self.q1=StringVar()
        self.q2 = StringVar()
        self.q3 = StringVar()
        self.q4 = StringVar()
        self.q5 = StringVar()

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
        self.var20 = StringVar()
        self.var21 = StringVar()
        tim = datetime.datetime.now().date()
        self.ti = str(tim)

        TitleLabel=Label(self.root,bd=20,relief=RIDGE,text="Patient Information System",fg="red",bg="white",font=("times new roman",50,"bold"))
        TitleLabel.pack(side=TOP,fill=X)

        #============================Data Frame==========================================================

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=120,width=1280,height=370)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Info")
        DataFrameLeft.place(x=0,y=5,width=780,height=330)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select RID from register")
        row = mycursor.fetchall()

        combo = ttk.Combobox(DataFrameLeft, textvariable=self.var1, width=25, font=("arial", 12, "bold"),
                             state="readonly")
        combo["values"] = row
        combo.grid(row=0, column=1)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                   text="Prescription")
        DataFrameRight.place(x=790, y=5, width=440, height=300)

        #=================================Button Frame=======================================================

        ButtonFrame =Frame(self.root,bd=10,relief=RIDGE)
        ButtonFrame.place(x=0,y=490,width=1280,height=60)

        #=================================Detail Frame=======================================================

        DetailFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailFrame.place(x=0, y=550, width=1280, height=120)

        #=====================================Data Frame Left====================================================

        PatientId=Label(DataFrameLeft,text="Patient ID",padx=2,pady=6, font=("times new roman", 12, "bold"))
        PatientId.grid(row=0,column=0)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select DoctorID from doctable")
        row3 = mycursor.fetchall()

        DoctorId = Label(DataFrameLeft, text="Doctor ID", padx=2, pady=6, font=("times new roman", 12, "bold"))
        DoctorId.grid(row=1, column=0)

        DoctorId2 = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var2)
        DoctorId2["values"]=row3
        DoctorId2.grid(row=1, column=1)

        Disease = Label(DataFrameLeft, text="Disease", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Disease.grid(row=2, column=0)

        Disease2 = Entry(DataFrameLeft, width=30,textvariable=self.var3)
        Disease2.grid(row=2, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select Name from medtable")
        row2 = mycursor.fetchall()


        Refno1a = Label(DataFrameLeft, text="Medicine 1", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Refno1a.grid(row=3, column=0)

        Refno1b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var4)
        Refno1b["values"]=row2
        Refno1b.grid(row=3, column=1)


        Refno2a = Label(DataFrameLeft, text="Medicine 2", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Refno2a.grid(row=4, column=0)

        Refno2b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var5)
        Refno2b["values"]=row2
        Refno2b.grid(row=4, column=1)


        Refno3a = Label(DataFrameLeft, text="Medicine 3", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Refno3a.grid(row=5, column=0)

        Refno3b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var6)
        Refno3b["values"]=row2
        Refno3b.grid(row=5, column=1)

        Refno4a = Label(DataFrameLeft, text="Medicine 4", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Refno4a.grid(row=6, column=0)

        Refno4b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var8)
        Refno4b["values"]=row2
        Refno4b.grid(row=6, column=1)

        Refno5a = Label(DataFrameLeft, text="Medicine 5", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Refno5a.grid(row=7, column=0)

        Refno5b = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.var9)
        Refno5b["values"]=row2
        Refno5b.grid(row=7, column=1)


        #============================Quantity==============================================================
        Q1a = Label(DataFrameLeft, text="Qty", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Q1a.grid(row=3, column=2)

        Q1b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.q1)
        Q1b["values"] = ("0","1","2","3","4")
        Q1b.grid(row=3, column=3)
        Q1b.current(0)

        Q2a = Label(DataFrameLeft, text="Qty", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Q2a.grid(row=4, column=2)

        Q2b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"),  textvariable=self.q2)
        Q2b["values"] = ("0","1","2","3","4")
        Q2b.grid(row=4, column=3)
        Q2b.current(0)

        Q3a = Label(DataFrameLeft, text="Qty", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Q3a.grid(row=5, column=2)

        Q3b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.q3)
        Q3b["values"] = ("0","1","2","3","4")
        Q3b.grid(row=5, column=3)
        Q3b.current(0)

        Q4a = Label(DataFrameLeft, text="Qty", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Q4a.grid(row=6, column=2)

        Q4b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.q4)
        Q4b["values"] = ("0","1","2","3","4")
        Q4b.grid(row=6, column=3)
        Q4b.current(0)

        Q5a = Label(DataFrameLeft, text="Qty", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Q5a.grid(row=7, column=2)

        Q5b = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.q5)
        Q5b["values"] = ("0","1","2","3","4")
        Q5b.grid(row=7, column=3)
        Q5b.current(0)
        #=======================================Search================================================================
        Search = Label(DataFrameLeft, text="Search", padx=2, pady=6, font=("times new roman", 12, "bold"))
        Search.place(x=580, y=140)

        Search2 = Entry(DataFrameLeft, width=30,textvariable=self.var7)
        Search2.place(x=580, y=175)

        #================================Data Frame Right=====================================================
        self.textPresciption=Text(DataFrameRight,font=("times new roman", 12, "bold"),width=50,height=13,padx=2,pady=6)
        self.textPresciption.grid(row=0,column=0)


        PatientName=Label(DataFrameLeft,text="Patient Name",padx=2,pady=6, font=("times new roman", 12, "bold"))
        PatientName.grid(row=0,column=2)
        PatientName2 = Entry(DataFrameLeft, width=30, textvariable=self.var20)
        PatientName2.grid(row=0, column=3)


        Patientage=Label(DataFrameLeft,text="Patient Age",padx=2,pady=6, font=("times new roman", 12, "bold"))
        Patientage.grid(row=0,column=4)
        Patientage2 = Entry(DataFrameLeft, width=30, textvariable=self.var21)
        Patientage2.grid(row=0,column=5)
        #================================Prescription=========================================================

        btnPrescription=Button(ButtonFrame,text="Prescription",font=("times new roman", 12, "bold"),bg="purple",command=self.Prescription,fg="white",width=16,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,text="Prescription Data",font=("times new roman", 12, "bold"),command=self.PrescriptionData,bg="blue",fg="white",width=16,height=1,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,text="Search",font=("times new roman", 12, "bold"),command=self.FetchWho,bg="orange",fg="white",width=16,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,text="Delete",font=("times new roman", 12, "bold"),bg="green",fg="white",width=16,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,text="Clear",font=("times new roman", 12, "bold"),command=self.Clear,bg="red",fg="white",width=16,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,text="Exit",font=("times new roman", 12, "bold"),command=self.Exit,bg="purple",fg="white",width=16,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        btnPrint=Button(ButtonFrame,text="Print Prescription",font=("times new roman", 12, "bold"),command=self.printfun,bg="green",fg="white",width=16,height=1,padx=2,pady=6)
        btnPrint.grid(row=0,column=6)


        #===================================Table============================================================

        ScrollX2 = ttk.Scrollbar(DataFrame, orient=HORIZONTAL)

        self.pattable2 = ttk.Treeview(DataFrame, column=(
        "Patient ID", "Doctor ID", "Disease", "Medicine 1", "Medicine 2", "Medicine 3", "Medicine 4", "Medicine 5"),
                                     xscrollcommand=ScrollX2)
        ScrollX2.pack(side=BOTTOM, fill=X)


        ScrollX2.config(command=self.pattable2.xview)


        self.pattable2.heading("Patient ID", text="Patient ID")
        self.pattable2.heading("Doctor ID", text="Doctor ID")
        self.pattable2.heading("Disease", text="Disease")
        self.pattable2.heading("Medicine 1", text="Medicine 1")
        self.pattable2.heading("Medicine 2", text="Medicine 2")
        self.pattable2.heading("Medicine 3", text="Medicine 3")
        self.pattable2.heading("Medicine 4", text="Medicine 4")
        self.pattable2.heading("Medicine 5", text="Medicine 5")

        self.pattable2.column("Patient ID", width=100)
        self.pattable2.column("Doctor ID", width=100)
        self.pattable2.column("Disease", width=100)
        self.pattable2.column("Medicine 1", width=100)
        self.pattable2.column("Medicine 2", width=100)
        self.pattable2.column("Medicine 3", width=100)
        self.pattable2.column("Medicine 4", width=100)
        self.pattable2.column("Medicine 5", width=100)

        self.pattable2.place(x=300,y=70,width=450,height=50)

        #----------------------------------Scroll Bar--------------------------------------------

        ScrollX=ttk.Scrollbar(DetailFrame,orient=HORIZONTAL)
        ScrollY=ttk.Scrollbar(DetailFrame,orient=VERTICAL)
        self.pattable=ttk.Treeview(DetailFrame,column=("Patient ID","Doctor ID","Disease","Medicine 1","Medicine 2","Medicine 3","Medicine 4","Medicine 5"),xscrollcommand=ScrollX,yscrollcommand=ScrollY)
        ScrollX.pack(side=BOTTOM,fill=X)
        ScrollY.pack(side=RIGHT,fill=Y)


        ScrollX.config(command=self.pattable.xview)
        ScrollY.config(command=self.pattable.yview)

        self.pattable.heading("Patient ID",text="Patient ID")
        self.pattable.heading("Doctor ID", text="Doctor ID")
        self.pattable.heading("Disease", text="Disease")
        self.pattable.heading("Medicine 1", text="Medicine 1")
        self.pattable.heading("Medicine 2", text="Medicine 2")
        self.pattable.heading("Medicine 3", text="Medicine 3")
        self.pattable.heading("Medicine 4", text="Medicine 4")
        self.pattable.heading("Medicine 5", text="Medicine 5")

        self.pattable.column("Patient ID",width=100)
        self.pattable.column("Doctor ID", width=100)
        self.pattable.column("Disease", width=100)
        self.pattable.column("Medicine 1", width=100)
        self.pattable.column("Medicine 2", width=100)
        self.pattable.column("Medicine 3", width=100)
        self.pattable.column("Medicine 4", width=100)
        self.pattable.column("Medicine 5", width=100)

        self.pattable.pack(fill=BOTH, expand=1)
        self.FetchData()
        #=====================================Functionality==================================

    def PrescriptionData(self):
        if self.var1.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
            mycursor=conn.cursor()
            mycursor.execute("insert into pattable values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.var1.get(),
                                 self.var2.get(),self.var3.get(),self.var4.get(),self.var5.get(),self.var6.get()
                                 ,self.var8.get(),self.var9.get()))

            mycursor.execute("insert into patienttable values(%s,%s,%s,%s,%s,%s)",(self.var1.get(),
                                 self.var20.get(),self.var21.get(),self.var2.get(),self.var3.get(),self.ti))

            mycursor.execute("insert into consumes values(%s,%s,%s)",(self.var1.get(),self.var4.get(),self.q1.get()))
            mycursor.execute("insert into consumes values(%s,%s,%s)", (self.var1.get(), self.var5.get(),self.q2.get()))
            mycursor.execute("insert into consumes values(%s,%s,%s)", (self.var1.get(), self.var6.get(),self.q3.get()))
            mycursor.execute("insert into consumes values(%s,%s,%s)", (self.var1.get(), self.var8.get(),self.q4.get()))
            mycursor.execute("insert into consumes values(%s,%s,%s)", (self.var1.get(), self.var9.get(),self.q5.get()))
            mycursor.execute("insert into treats values(%s,%s)", (self.var2.get(), self.var1.get()))

            conn.commit()
            self.FetchData()
            conn.close()
            messagebox.showinfo("Success","Data inserted")

    def FetchData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
        mycursor=conn.cursor()
        mycursor.execute("select * from pattable where PatientID IN(select PatientID from consumes)")

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

        mycursor.execute("SELECT * FROM pattable WHERE PatientID=%s",(self.var7.get(), ))
        row3=mycursor.fetchall()
        if len(row3)!=0:
            self.pattable2.delete(*self.pattable2.get_children())
            for i in row3:
                self.pattable2.insert("",END,values=i)
            conn.commit()
        conn.close()

    def Prescription(self):

        self.textPresciption.insert(END, "Date:\t\t" + self.ti + "\n")
        self.textPresciption.insert(END,"Patient ID:\t\t" +  self.var1.get()+  "\n")
        self.textPresciption.insert(END, "Patient Name:\t\t" + self.var20.get() + "\n")
        self.textPresciption.insert(END, "Age:\t\t" + self.var21.get() + "\n")
        self.textPresciption.insert(END, "Doctor ID:\t\t" +  self.var2.get() + "\n")
        self.textPresciption.insert(END, "Disease:\t\t"   +  self.var3.get() + "\n")
        self.textPresciption.insert(END, "Medicine 1:\t\t"+  self.var4.get() + "\t\t")
        self.textPresciption.insert(END, "Qty1:\t\t" + self.q1.get() + "\n")
        self.textPresciption.insert(END, "Medicine 2:\t\t"+  self.var5.get() + "\t\t")
        self.textPresciption.insert(END, "Qty2:\t\t" + self.q2.get() + "\n")
        self.textPresciption.insert(END, "Medicine 3:\t\t"+  self.var6.get() + "\t\t" )
        self.textPresciption.insert(END, "Qty3:\t\t" + self.q3.get() + "\n")
        self.textPresciption.insert(END, "Medicine 4:\t\t" + self.var8.get() + "\t\t")
        self.textPresciption.insert(END, "Qty4:\t\t" + self.q4.get() + "\n")
        self.textPresciption.insert(END, "Medicine 5:\t\t" + self.var9.get()+ "\t\t")
        self.textPresciption.insert(END, "Qty5:\t\t" + self.q5.get() + "\n")
        self.textPresciption.insert(END, "Remarks:\t\t" + self.remarks.get() + "\n\n\n")
        self.textPresciption.insert(END,"---------------------------------------\n\n")
        messagebox.showinfo("Success","Prescription Added")


    def Clear(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("")
        self.textPresciption.delete("1.0",END)

    def Exit(self):
        Ex=messagebox.askyesno("Patient Information System","Confirm Exit")
        if Ex>0:
            self.root.destroy()
            return
    def printfun(self):

        self.predata=self.textPresciption.get(1.0,END)
        f1=open("Prescriptions/"+str(self.var1.get())+".txt",'w')
        f1.write(self.predata)
        f1.close()

if __name__=="__main__":

    root=Tk()
    ob=Hospital(root)
    root.mainloop()

