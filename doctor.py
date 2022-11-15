from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class Doctor:
    def __init__(self,root):
        self.root=root
        self.root.title("Doctor Information System")
        self.root.geometry("1040x600+10+10")


        self.var1=StringVar()
        self.var2= StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6=StringVar()
        self.var7=StringVar()
        z = random.randint(1000, 9999)
        self.var1.set(z)
        TitleLabel=Label(self.root,bd=20,relief=RIDGE,text="Doctor Information System",fg="red",bg="white",font=("times new roman",50,"bold"))
        TitleLabel.pack(side=TOP,fill=X)

        #============================Data Frame==========================================================

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=120,width=1280,height=350)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Doctor Info",fg="green")
        DataFrameLeft.place(x=0,y=5,width=780,height=300)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                   text="Display",fg="green")
        DataFrameRight.place(x=790, y=5, width=440, height=300)

        #=================================Button Frame=======================================================

        ButtonFrame =Frame(self.root,bd=10,relief=RIDGE)
        ButtonFrame.place(x=0,y=450,width=1280,height=60)

        # =================================Detail Frame=======================================================

        DetailFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailFrame.place(x=0, y=510, width=1280, height=150)

        #=====================================Data Frame Left====================================================

        DoctorId=Label(DataFrameLeft,text="Doctor ID",padx=2,pady=6, font=("times new roman", 12, "bold"),fg="blue")
        DoctorId.grid(row=0,column=0)

        DoctorId2=Entry(DataFrameLeft,width=30,textvariable=self.var1)
        DoctorId2.grid(row=0, column=1)


        DoctorName = Label(DataFrameLeft, text="Doctor Name", padx=2, pady=6, font=("times new roman", 12, "bold"),fg="blue")
        DoctorName.grid(row=1, column=0)

        DoctorName2=Entry(DataFrameLeft,width=30,textvariable=self.var2)
        DoctorName2.grid(row=1, column=1)

        Qualification= Label(DataFrameLeft, text="Qualification", padx=2, pady=6, font=("times new roman", 12, "bold"),fg="blue")
        Qualification.grid(row=2, column=0)

        Qualification2 = Entry(DataFrameLeft, width=30,textvariable=self.var3)
        Qualification2.grid(row=2, column=1)

        Specialization = Label(DataFrameLeft, text="Specialization", padx=2, pady=6, font=("times new roman", 12, "bold"),fg="blue")
        Specialization.grid(row=3, column=0)

        Specialization2 =Entry(DataFrameLeft, width=30,textvariable=self.var4)
        Specialization2.grid(row=3, column=1)


        Experience = Label(DataFrameLeft, text="Experience", padx=2, pady=6, font=("times new roman", 12, "bold"),fg="blue")
        Experience.grid(row=4, column=0)

        Experience2= Entry(DataFrameLeft, width=30,textvariable=self.var5)
        Experience2.grid(row=4, column=1)

        ContactNo=Label(DataFrameLeft, text="Contact No", padx=2, pady=6, font=("times new roman", 12, "bold"),fg="blue")
        ContactNo.grid(row=5, column=0)

        ContactNo2= Entry(DataFrameLeft, width=30,textvariable=self.var7)
        ContactNo2.grid(row=5, column=1)

        Search=Label(DataFrameLeft, text="Search", padx=2, pady=6, font=("times new roman", 12, "bold"),fg="red",bg="white")
        Search.place(x=350, y=200,width=80,height=40)

        Search2 = Entry(DataFrameLeft, width=30, textvariable=self.var6)
        Search2.place(x=431, y=200,width=240,height=40)
        #==================================Doctor Search Window==============================================

        ScrollX2 = ttk.Scrollbar(DataFrame, orient=HORIZONTAL)

        self.pattable2 = ttk.Treeview(DataFrame, column=(
        "Doctor ID", "Doctor Name", "Qualification", "Specialization", "Experience"),
                                     xscrollcommand=ScrollX2)
        ScrollX2.pack(side=BOTTOM, fill=X)


        ScrollX2.config(command=self.pattable2.xview)


        self.pattable2.heading("Doctor ID", text="Doctor ID")
        self.pattable2.heading("Doctor Name", text="Doctor Name")
        self.pattable2.heading("Qualification", text="Qualification")
        self.pattable2.heading("Specialization", text="Specialization")
        self.pattable2.heading("Experience", text="Experience")

        self.pattable2.column("Doctor ID", width=100)
        self.pattable2.column("Doctor Name", width=100)
        self.pattable2.column("Qualification", width=100)
        self.pattable2.column("Specialization", width=100)
        self.pattable2.column("Experience", width=100)

        self.pattable2.place(x=340,y=38,width=400,height=150)


        #================================Data Frame Right=====================================================
        self.textDisplay=Text(DataFrameRight,font=("times new roman", 12, "bold"),width=50,height=13,padx=2,pady=6)
        self.textDisplay.grid(row=0,column=0)

        #================================Prescription=========================================================
        btnAdd=Button(ButtonFrame,text="ADD",font=("times new roman", 12, "bold"),bg="purple",command=self.Add,fg="white",
                      width=16,height=1,padx=2,pady=6)
        btnAdd.grid(row=0,column=0)

        btnDisplay=Button(ButtonFrame,text="DISPLAY",font=("times new roman", 12, "bold"),command=self.Display,bg="blue",fg="white",width=16,height=1,padx=2,pady=6)
        btnDisplay.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,text="Update",font=("times new roman", 12, "bold"),bg="orange",fg="white",width=16,height=1,padx=2,pady=6,command=self.update)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,text="Delete",font=("times new roman", 12, "bold"),bg="green",fg="white",width=16,height=1,padx=2,pady=6,command=self.delete)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,text="Clear",font=("times new roman", 12, "bold"),bg="red",fg="white",command=self.Clear,width=16,height=1,padx=2,pady=6,)
        btnClear.grid(row=0,column=4)


        btnSearch=Button(ButtonFrame,text="Search",font=("times new roman", 12, "bold"),command=self.search,bg="green",fg="white",width=16,height=1,padx=2,pady=6)
        btnSearch.grid(row=0,column=5)

        btnExit=Button(ButtonFrame,text="Exit",font=("times new roman", 12, "bold"),command=self.Exit,bg="purple",fg="white",width=16,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=6)

        #===================================Table============================================================


        #----------------------------------Scroll Bar--------------------------------------------------------

        ScrollX=ttk.Scrollbar(DetailFrame,orient=HORIZONTAL)
        ScrollY=ttk.Scrollbar(DetailFrame,orient=VERTICAL)
        self.doctable=ttk.Treeview(DetailFrame,column=("Doctor ID","Doctor Name","Qualification","Specialization","Experience","Contact No"),xscrollcommand=ScrollX,yscrollcommand=ScrollY)
        ScrollX.pack(side=BOTTOM,fill=X)
        ScrollY.pack(side=RIGHT,fill=Y)


        ScrollX.config(command=self.doctable.xview)
        ScrollY.config(command=self.doctable.yview)

        self.doctable.heading("Doctor ID", text="Doctor ID")
        self.doctable.heading("Doctor Name", text="Doctor Name")
        self.doctable.heading("Qualification", text="Qualification")
        self.doctable.heading("Specialization", text="Specialization")
        self.doctable.heading("Experience", text="Experience")
        self.doctable.heading("Contact No", text="Contact No")


        self.doctable.column("Doctor ID", width=100)
        self.doctable.column("Doctor Name", width=100)
        self.doctable.column("Qualification", width=100)
        self.doctable.column("Specialization", width=100)
        self.doctable.column("Experience", width=100)
        self.doctable.column("Contact No", width=100)
        self.doctable.pack(fill=BOTH, expand=1)

        self.FetchData()
        self.doctable.bind("<ButtonRelease-1>", self.medget)
        #=====================================Functionality==================================

    def Add(self):
        if self.var1.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
            mycursor=conn.cursor()
            mycursor.execute("insert into doctable values(%s,%s,%s,%s,%s,%s)",(self.var1.get(),
                                 self.var2.get(),self.var3.get(),self.var4.get(),self.var5.get(),self.var7.get()))
            conn.commit()
            messagebox.showinfo("Success", "Data inserted")
            self.FetchData()
            self.medget()
            conn.close()


    def FetchData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
        mycursor=conn.cursor()
        mycursor.execute("select * from doctable")
        row=mycursor.fetchall()
        if len(row)!=0:
            self.doctable.delete(*self.doctable.get_children())
            for i in row:
                self.doctable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def Display(self):

        self.textDisplay.insert(END, "Doctor ID:\t\t" +  self.var1.get() + "\n")
        self.textDisplay.insert(END, "Doctor Name:\t\t"   +  self.var2.get() + "\n")
        self.textDisplay.insert(END, "Qualification:\t\t"+  self.var3.get() + "\n")
        self.textDisplay.insert(END, "Specialization:\t\t"+  self.var4.get() + "\n")
        self.textDisplay.insert(END, "Experience:\t\t" + self.var5.get() + "\n")
        self.textDisplay.insert(END, "Contact No:\t\t" + self.var7.get() + "\n")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM doctable WHERE DoctorID=%s", (self.var6.get(),))
        row3 = mycursor.fetchall()
        if len(row3) != 0:
            self.pattable2.delete(*self.pattable2.get_children())
            for i in row3:
                self.pattable2.insert("", END, values=i)
            conn.commit()
        conn.close()

    def medget(self, event=""):
        cursorrow = self.doctable.focus()
        content = self.doctable.item(cursorrow)
        row = content["values"]
        self.var1.set(row[0])
        self.var2.set(row[1])
        self.var3.set(row[2])
        self.var4.set(row[3])
        self.var5.set(row[4])
        self.var7.set(row[5])

    def update(self):
        if self.var1.get() == "" or self.var2.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                           database="pharma")
            mycursor = conn.cursor()
            mycursor.execute(
                "update doctable set DoctorName=%s,Qualification=%s,Specialization=%s,Experience=%s,ContactNo=%s where DoctorID=%s",
                (self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get(), self.var7.get(), self.var1.get()))

            conn.commit()
            self.FetchData()
            conn.close()
            messagebox.showinfo("Success", "Data Updated")



    def delete(self):
        if self.var1.get() == "" or self.var2.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                           database="pharma")
            mycursor = conn.cursor()

            mycursor.execute("delete from doctable where DoctorID=%s", (self.var1.get(),))
            conn.commit()
            self.FetchData()
            conn.close()
            messagebox.showinfo("Success", "Data Deleted")

    def Clear(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("")
        self.var6.set("")
        self.var7.set("")
        self.textDisplay.delete("1.0",END)

    def Exit(self):
        Ex=messagebox.askyesno("Doctor Information System","Confirm Exit")
        if Ex>0:
            root.destroy()
            return
if __name__=="__main__":
    root=Tk()
    ob=Doctor(root)
    root.mainloop()
