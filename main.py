from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from patient import Hospital
from doctor import Doctor
from chatbot import Chatbot
from bill import Bill
from voice import Widget
import webbrowser
import random
import datetime
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
       def __init__(self,root):

           self.root=root
           self.root.title("Pharmacy Management System")
           self.root.geometry("1550x800+0+0")

           # ====================ADD MEDICINE VARIABLE===============================================
           self.var=StringVar()
           self.var2=StringVar()
           self.var20 = StringVar()
           #======================Main Data Variable==================================================
           self.var3=StringVar()
           self.var4 = StringVar()
           self.var5 = StringVar()
           self.var6 = StringVar()
           self.var7 = StringVar()
           self.var8 = StringVar()
           self.var9 = StringVar()
           self.var10 = StringVar()
           self.var11=StringVar()
           self.tim=datetime.datetime.now().date()

           lbltitle=Label(self.root,text="Pharmacy Management System",bd=15,relief=RIDGE,
                                bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
           lbltitle.pack(side=TOP,fill=X)

           img1=Image.open("C:\logo11.jpg")
           img1=img1.resize((80,80))

           self.photoimg1=ImageTk.PhotoImage(img1)

           img2 = Image.open("C:\logovoice.jpg")
           img2 = img2.resize((80, 80))

           self.photoimg2 = ImageTk.PhotoImage(img2)

           img3 = Image.open("C:\logo.png")
           img3 = img3.resize((80, 80))

           self.photoimg3 = ImageTk.PhotoImage(img3)


           img4a = Image.open("C:\patient.jpg")
           img4a = img4a.resize((80, 80))

           self.photoimg4a = ImageTk.PhotoImage(img4a)

           img5 = Image.open("C:\doctor.png")
           img5 = img5.resize((80, 80))

           self.photoimg5 = ImageTk.PhotoImage(img5)

           img6 = Image.open("C:\Abill.jfif")
           img6 = img6.resize((80, 80))

           self.photoimg6 = ImageTk.PhotoImage(img6)
 # ======================== Data Frame===========================

           DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
           DataFrame.place(x=0,y=120,height=340,width=1270 )

           DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                    fg="darkgreen",font=("arial",12,"bold"))
           DataFrameLeft.place(x=0,y=5,width=800,height=300)

           DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                     fg="darkgreen",font=("arial",12,"bold"))

           DataFrameRight.place(x=820,y=5,width=380,height=300)

          #==================== ============BUTTON FRAME======================================


           ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
           ButtonFrame.place(x=0,y=465,width=1530,height=65 )


           #================================Main Button=============== ============

           btnAddData=Button(ButtonFrame,text="Add",width=10,command=self.AddData,font=("arial",12,"bold"),bg="darkgreen",fg="white")
           btnAddData.grid(row=0,column=1)


           btnReference = Button(ButtonFrame, text="Ref", width=7, font=("arial", 12, "bold"), bg="orange", fg="white",
                              pady=2, command=self.Ref)
           btnReference.grid(row=0, column=0)

           btnUpdateMed=Button(ButtonFrame,text="Update",width=10,font=("arial",12,"bold"),bg="darkgreen",fg="white",command=self.updatedata)
           btnUpdateMed.grid(row=0,column=2)

           btnDeleteMed = Button(ButtonFrame, text="Delete",width=10, font=("arial", 12, "bold"), bg="red", fg="white",command=self.deletedata)
           btnDeleteMed.grid(row=0, column=3)

           btnRestMed = Button(ButtonFrame, text="Reset ",width=10, font=("arial", 12, "bold"), bg="darkgreen", fg="white",command=self.reset)
           btnRestMed.grid(row=0, column=4)

           btnExitMed = Button(ButtonFrame, text="Exit",width=10, font=("arial", 12, "bold"), bg="darkgreen", fg="white",command=self.Exit)
           btnExitMed.grid(row=0,column=5)

        #=======================Search By====================================================

           txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial", 12, "bold"),textvariable=self.var20)
           txtSearch.grid(row=0,column=6)

           searchBtn =Button(ButtonFrame, text="Search", font=("arial", 12, "bold"), bg="darkgreen", fg="white",command=self.search)
           searchBtn.grid(row=0, column=7)

           showAll = Button(ButtonFrame, text="Show All", font=("arial", 12, "bold"), bg="darkgreen", fg="white",command=self.FetchData)
           showAll.grid(row=0, column=8)

        #================================label and entry============================================
           lblrefno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference no", padx=2)
           lblrefno.grid(row=0, column=0, sticky=W)

           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                          database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("select Ref from pharmacy2")
           row=mycursor.fetchall()


           ref_combo = ttk.Combobox(DataFrameLeft,textvariable=self.var3, width=25, font=("arial", 12, "bold"), state="readonly")
           ref_combo["values"] = row
           ref_combo.grid(row=0,column=1)
           ref_combo.current(0)

           CompanyName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name", padx=2)
           CompanyName.grid(row=1, column=0)

           CompanyText = Entry(DataFrameLeft,textvariable=self.var4, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           CompanyText.grid(row=1, column=1,pady=2)

           TypeOfMed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Formula", padx=2)
           TypeOfMed.grid(row=2, column=0, sticky=W)


           TypeOfMedText=Entry(DataFrameLeft, textvariable=self.var5, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           TypeOfMedText.grid(row=2, column=1)


           MedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2)
           MedicineName.grid(row=3, column=0, sticky=W)


           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                          database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("select MedName from pharmacy2 where Ref=%s",(self.var3.get(),))
           row2=mycursor.fetchall()

           MedicineName2= ttk.Combobox(DataFrameLeft, width=25,textvariable=self.var6, font=("arial", 12, "bold"))
           MedicineName2["values"] =row2
           MedicineName2.grid(row=3, column=1)
           MedicineName2.current(0)

           Qty = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Quantity", padx=2)
           Qty.grid(row=4, column=0, sticky=W)

           Qty = Entry(DataFrameLeft, textvariable=self.var7, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           Qty.grid(row=4, column=1, pady=2)

           Price = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Price(Per Unit)", padx=2)
           Price.grid(row=5, column=0, sticky=W)

           Price = Entry(DataFrameLeft, textvariable=self.var8, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           Price.grid(row=5, column=1, pady=2)

           ExpiryDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ExpiryDate", padx=2)
           ExpiryDate.grid(row=6, column=0, sticky=W)

           ExpiryDate = Entry(DataFrameLeft, textvariable=self.var9, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           ExpiryDate.grid(row=6, column=1, pady=2)

           Uses = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses", padx=2)
           Uses.grid(row=7, column=0, sticky=W)

           Uses = Entry(DataFrameLeft, textvariable=self.var10, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           Uses.grid(row=7, column=1, pady=2)

           SideEffects = Label(DataFrameLeft, font=("arial", 12, "bold"), text="SideEffects", padx=2)
           SideEffects.grid(row=8, column=0, sticky=W)

           SideEffects= Entry(DataFrameLeft, textvariable=self.var11, bd=3, relief=RIDGE, width=27, font=("arial", 12, "bold"))
           SideEffects.grid(row=8, column=1, pady=2)

           #----------------------------------Covid Image--------------------------

           img4=Image.open("C:\covid.jfif")
           img4=img4.resize((360,210))
           self.photoimg4=ImageTk.PhotoImage(img4)

           btnco=Button(DataFrameLeft,image=self.photoimg4,borderwidth=0,command=self.covid).place(x=400,y=5)

           # ===============================Data Frame Right=============================================

           lblrefno2 = Label(DataFrameRight, font=("arial", 12, "bold"), text="Reference No")
           lblrefno2.grid(row=0, column=0)


           txtrefno2 = Entry(DataFrameRight, textvariable=self.var, bd=3, relief=RIDGE, width=20, font=("arial", 12, "bold"))
           txtrefno2.grid(row=0, column=1)

           lblmedName2 = Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name")
           lblmedName2.grid(row=1, column=0)

           txtmedName2 = Entry(DataFrameRight, textvariable=self.var2, bd=3, relief=RIDGE, width=20, font=("arial", 12, "bold"))
           txtmedName2.grid(row=1, column=1)

           Side=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
           Side.place(x=0,y=60,width=315,height=150)

           scrollX=ttk.Scrollbar(Side,orient=HORIZONTAL)
           scrollX.pack(side=BOTTOM,fill=X)
           scrollY = ttk.Scrollbar(Side,orient=VERTICAL)
           scrollY.pack(side=RIGHT, fill=Y)

           self.pharmacy2=ttk.Treeview(Side,column=("ref","medname"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
           scrollX.config(command=self.pharmacy2.xview)
           scrollY.config(command=self.pharmacy2.yview)

           self.pharmacy2.heading("ref",text="Ref No")
           self.pharmacy2.heading("medname", text="Medicine Name")

           self.pharmacy2["show"]="headings"
           self.pharmacy2.pack(fill=BOTH,expand=1)

           self.pharmacy2.column("ref",width=100)
           self.pharmacy2.column("medname", width=100)

           self.pharmacy2.bind("<ButtonRelease-1>",self.medget)
       #============================Med Aadd Button================================================================================


           downframe=Frame(DataFrameRight,relief=RIDGE,bg="darkgreen")
           downframe.place(x=0,y=220,width=320,height=35)

           btnAddmed=Button(downframe,text="Add",width=7,font=("arial",12,"bold"),bg="orange",fg="white",pady=2,command=self.AddMed)
           btnAddmed.grid(row=0,column=1)


           btnUpdatemed=Button(downframe,text="Update",width=7,font=("arial",12,"bold"),bg="purple",fg="white",pady=2,command=self.updatemedo)
           btnUpdatemed.grid(row=0,column=2)

           btnDeletemed=Button(downframe,text="Delete",width=7,font=("arial",12,"bold"),bg="red",fg="white",pady=2,command=self.deletemedo)
           btnDeletemed.grid(row=0,column=3)

           btnClearmed=Button(downframe,text="Clear",width=7,font=("arial",12,"bold"),bg="lime",fg="white",pady=2,command=self.clearmed)
           btnClearmed.grid(row=0,column=4)

        #=================frame details=======================================
           Framedetails=Frame(self.root,bd=14,relief=RIDGE)
           Framedetails.place(x=0,y=530,width=1270,height=120)

        #=================Main table and Scroll Bar===========================

           scrollX2 = ttk.Scrollbar(Framedetails, orient=HORIZONTAL)
           scrollX2.pack(side=BOTTOM, fill=X)
           scrollY2 = ttk.Scrollbar(Side, orient=VERTICAL)
           scrollY2.pack(side=RIGHT, fill=Y)

           self.medtable=ttk.Treeview(Framedetails,column=("ref","companyname","formula","tabletname","qty","price","expdate","uses",
                                                         "sideeffects"),xscrollcommand=scrollX2.set,yscrollcommand=scrollY2.set)
           scrollX2.config(command=self.medtable.xview)
           scrollY2.config(command=self.medtable.yview)

           self.medtable["show"]="headings"

           self.medtable.heading("ref",text="Reference No")
           self.medtable.heading("companyname",text="Company")
           self.medtable.heading("formula",text="Formula")
           self.medtable.heading("tabletname",text="Name")
           self.medtable.heading("qty",text="Quantity")
           self.medtable.heading("price",text="Price")
           self.medtable.heading("expdate",text="Expiry")
           self.medtable.heading("uses",text="Uses")
           self.medtable.heading("sideeffects",text="Side Effects")


           self.medtable.column("ref",width=60)
           self.medtable.column("companyname", width=60)
           self.medtable.column("formula", width=60)
           self.medtable.column("tabletname", width=60)
           self.medtable.column("qty", width=60)
           self.medtable.column("price", width=60)
           self.medtable.column("expdate", width=60)
           self.medtable.column("uses",width=60)
           self.medtable.column("sideeffects", width=60)

           self.medtable.pack(fill=BOTH, expand=1)
           self.FetchMed()
           self.FetchData()
           self.medtable.bind("<ButtonRelease-1>", self.medget2)


       def covid(self):
           webbrowser.open("https://covid19.who.int/")


       def Exit(self):
           Ex = messagebox.askyesno(" Pharmacy Management System", "Confirm Exit")
           if Ex > 0:
               self.root.destroy()
               return

       def reset(self):
           self.var.set("")
           self.var2.set("")
           self.var20.set("")
           self.var3.set("")
           self.var4.set("")
           self.var5.set("")
           self.var6.set("")
           self.var7.set("")
           self.var8.set("")
           self.var9.set("")
           self.var10.set("")
           self.var11.set("")

       #========================Add Medicine==============================

       def AddMed(self):

           conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
           mycursor=conn.cursor()
           mycursor.execute("insert into pharmacy2 (Ref,MedName) values(%s,%s)",(self.var.get(),self.var2.get()))

           conn.commit()
           self.FetchMed()
           conn.close()

           messagebox.showinfo("Success","Medicine Added")

       def search(self):
           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                          database="pharma")
           mycursor = conn.cursor()

           mycursor.execute("SELECT * FROM medtable WHERE Name=%s", (self.var20.get(),))
           row3 = mycursor.fetchall()
           if len(row3) != 0:
               self.medtable.delete(*self.medtable.get_children())
               for i in row3:
                   self.medtable.insert("", END, values=i)
               conn.commit()
           conn.close()


       def FetchMed(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
           mycursor=conn.cursor()
           mycursor.execute("select * from pharmacy2 ")
           rows=mycursor.fetchall()
           if len(rows)!=0:
               self.pharmacy2.delete(*self.pharmacy2.get_children())

               for i in rows:
                   self.pharmacy2.insert("",END,values=i)
                   conn.commit()

           conn.close()
       def clearmed(self):
           self.var.set("")
           self.var2.set("")

       def Ref(self):

           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                          database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("select MedName from pharmacy2 where Ref=%s",(self.var3.get(),))
           row2=mycursor.fetchall()

           MedicineName3= ttk.Combobox(self.root, width=25,textvariable=self.var6, font=("arial", 12, "bold"))
           MedicineName3["values"] =row2
           MedicineName3.place(x=195,y=243)


       def AddData(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
           mycursor=conn.cursor()
           mycursor.execute("insert into medtable values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                  (self.var3.get(),
                                                                  self.var4.get(),
                                                                  self.var5.get(),
                                                                  self.var6.get(),
                                                                  self.var7.get(),
                                                                  self.var8.get(),
                                                                  self.var9.get(),
                                                                  self.var10.get(),
                                                                  self.var11.get()))

           conn.commit()
           self.FetchData()

           messagebox.showinfo("Success", "Data is inserted")
           conn.close()



       def FetchData(self):
           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                          database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("select * from medtable")

           row=mycursor.fetchall()
           if len(row)!=0:

               self.medtable.delete(*self.medtable.get_children())
               for i in row:
                   self.medtable.insert("",END,values=i)
                   conn.commit()

           conn.close()


           #-----------------------Focus Cursor----------------------------------
       def medget(self,event=""):
          cursorrow=self.pharmacy2.focus()
          content=self.pharmacy2.item(cursorrow)
          row=content["values"]
          self.var.set(row[0])
          self.var2.set(row[1])


       def medget2(self,event=""):
          cursorrow2=self.medtable.focus()
          content2=self.medtable.item(cursorrow2)
          row=content2["values"]
          self.var3.set(row[0])
          self.var4.set(row[1])
          self.var5.set(row[2])
          self.var6.set(row[3])
          self.var7.set(row[4])
          self.var8.set(row[5])
          self.var9.set(row[6])
          self.var10.set(row[7])
          self.var11.set(row[8])

       def updatemedo(self):

           if self.var.get()=="" or self.var2.get()=="":
               messagebox.showerror("Error","All Fields are required")
           else:
               conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                              database="pharma")
               mycursor = conn.cursor()
               mycursor.execute("update pharmacy2 set Medname=%s where Ref=%s",(self.var2.get(),self.var.get()))
               conn.commit()
               self.FetchMed()
               conn.close()
               messagebox.showinfo("Success","Data Updated")

       def deletemedo(self):

           if self.var.get()=="" or self.var2.get()=="":
               messagebox.showerror("Error","All Fields are required")
           else:
               conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                              database="pharma")
               mycursor = conn.cursor()
               mycursor.execute("delete from pharmacy2 where Ref=%s",(self.var.get(),))
               conn.commit()
               self.FetchMed()
               conn.close()
               messagebox.showinfo("Success","Data Deleted")

       def updatedata(self):

           if self.var4.get()=="" or self.var7.get()=="":
               messagebox.showerror("Error","All Fields are required")
           else:
               conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                              database="pharma")
               mycursor = conn.cursor()
               mycursor.execute("update medtable set Company=%s,Formula=%s,Name=%s,Quantity=%s,Price=%s,Expiry=%s,Uses=%s,Sideeffects=%s where RefNo=%s",
                                (self.var4.get(),self.var5.get(),self.var6.get(),self.var7.get(),self.var8.get(),self.var9.get(),self.var10.get(),self.var11.get(),self.var3.get()))
               conn.commit()
               self.FetchData()
               conn.close()
               messagebox.showinfo("Success","Data Updated")

       def deletedata(self):
           if self.var4.get() == "" or self.var7.get() == "":
               messagebox.showerror("Error", "All Fields are required")
           else:
               conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                              database="pharma")
               mycursor = conn.cursor()

               mycursor.execute("delete from medtable where RefNo=%s",(self.var3.get(),))
               conn.commit()
               self.FetchData()
               conn.close()
               messagebox.showinfo("Success","Data Deleted")

if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()

