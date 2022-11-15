from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from patient import Hospital
from doctor import Doctor
from chatbot import Chatbot
from bill import Bill
from voice import Widget
import webbrowser
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
       def __init__(self,root):
           self.root=root
           self.root.title("PhaREXHA")
           self.root.geometry("1550x800+0+0")

           # ====================ADD MEDICINE VARIABLE===============================================
           self.var=StringVar()
           self.var2=StringVar()

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





           lbltitle=Label(self.root,text="PhaREXHA",bd=15,relief=RIDGE,
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

           b1=Button(self.root,image=self.photoimg1,borderwidth=0,command=self.chatbot)
           b1.place(x=100,y=20)
           b1 = Button(self.root, image=self.photoimg2, borderwidth=0, command=self.voice)
           b1.place(x=240, y=20)
           b3 = Button(self.root, image=self.photoimg3, borderwidth=0)
           b3.place(x=370, y=20)

           img4a = Image.open("C:\patient.jpg")
           img4a = img4a.resize((80, 80))

           self.photoimg4a = ImageTk.PhotoImage(img4a)

           img5 = Image.open("C:\doctor.png")
           img5 = img5.resize((80, 80))

           self.photoimg5 = ImageTk.PhotoImage(img5)

           img6 = Image.open("C:\Abill.jfif")
           img6 = img6.resize((80, 80))

           self.photoimg6 = ImageTk.PhotoImage(img6)

           b4 = Button(self.root, image=self.photoimg4a, borderwidth=0, command=self.patient)
           b4.place(x=900, y=20)
           b5 = Button(self.root, image=self.photoimg5, borderwidth=0, command=self.doctor)
           b5.place(x=1040, y=20)
           b6 = Button(self.root, image=self.photoimg6, borderwidth=0,command=self.bill)
           b6.place(x=1170, y=20)

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
           btnAddData.grid(row=0,column=0)

           btnUpdateMed=Button(ButtonFrame,text="Update",width=10,font=("arial",12,"bold"),bg="darkgreen",fg="white")
           btnUpdateMed.grid(row=0,column=1)

           btnDeleteMed = Button(ButtonFrame, text="Delete",width=10, font=("arial", 12, "bold"), bg="red", fg="white")
           btnDeleteMed.grid(row=0, column=2)

           btnRestMed = Button(ButtonFrame, text="Reset ",width=10, font=("arial", 12, "bold"), bg="darkgreen", fg="white")
           btnRestMed.grid(row=0, column=3)

           btnExitMed = Button(ButtonFrame, text="Exit",width=10, font=("arial", 12, "bold"), bg="darkgreen", fg="white")
           btnExitMed.grid(row=0,column=4)

        #=======================Search By====================================================

           lblSearch=Label(ButtonFrame,font=("arial", 15 , "bold"),text="Search by",padx=2,bg="red",fg="white")
           lblSearch.grid(row=0,column=5,sticky=W)

           search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial", 12, "bold"),state="readonly")
           search_combo["values"]=("Ref","Medname","Lot")
           search_combo.grid(row=0,column=6)
           search_combo.current(0)

           txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial", 12, "bold"))
           txtSearch.grid(row=0,column=7)

           searchBtn =Button(ButtonFrame, text="Search", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
           searchBtn.grid(row=0, column=8)

           showAll = Button(ButtonFrame, text="Show All", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
           showAll.grid(row=0, column=9)

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

           TypeOfMed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Type", padx=2)
           TypeOfMed.grid(row=2, column=0, sticky=W)

           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                          database="pharma")
           mycursor = conn.cursor()
           mycursor.execute("select MedName from pharmacy2")
           row2=mycursor.fetchall()

           TypeOfMedText = ttk.Combobox(DataFrameLeft, width=25,textvariable=self.var5, font=("arial", 12, "bold"), state="readonly")
           TypeOfMedText["values"] =("Tablet","Syrup","Capsule","Injection")
           TypeOfMedText.grid(row=2, column=1)
           TypeOfMedText.current(0)

           MedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2)
           MedicineName.grid(row=3, column=0, sticky=W)

           MedicineName2= ttk.Combobox(DataFrameLeft, width=25,textvariable=self.var6, font=("arial", 12, "bold"), state="readonly")
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

       #============================Med Aadd Button================================================================================


           downframe=Frame(DataFrameRight,relief=RIDGE,bg="darkgreen")
           downframe.place(x=0,y=220,width=320,height=35)

           btnAddmed=Button(downframe,text="Add",width=7,font=("arial",12,"bold"),bg="orange",fg="white",pady=2,command=self.AddMed)
           btnAddmed.grid(row=0,column=0)


           btnUpdatemed=Button(downframe,text="Update",width=7,font=("arial",12,"bold"),bg="purple",fg="white",pady=2)
           btnUpdatemed.grid(row=0,column=1)

           btnDeletemed=Button(downframe,text="Delete",width=7,font=("arial",12,"bold"),bg="red",fg="white",pady=2)
           btnDeletemed.grid(row=0,column=2)

           btnClearmed=Button(downframe,text="Clear",width=7,font=("arial",12,"bold"),bg="lime",fg="white",pady=2)
           btnClearmed.grid(row=0,column=3)

        #=================frame details=======================================
           Framedetails=Frame(self.root,bd=14,relief=RIDGE)
           Framedetails.place(x=0,y=530,width=1270,height=120)

        #=================Main table and Scroll Bar===========================



           scrollX2 = ttk.Scrollbar(Framedetails, orient=HORIZONTAL)
           scrollX2.pack(side=BOTTOM, fill=X)
           scrollY2 = ttk.Scrollbar(Side, orient=VERTICAL)
           scrollY2.pack(side=RIGHT, fill=Y)

           self.medtable=ttk.Treeview(Framedetails,column=("ref","companyname","type","tabletname","qty","price","expdate","uses",
                                                         "sideeffects"),xscrollcommand=scrollX2.set,yscrollcommand=scrollY2.set)
           scrollX2.config(command=self.medtable.xview)
           scrollY2.config(command=self.medtable.yview)

           self.medtable["show"]="headings"

           self.medtable.heading("ref",text="Reference No")
           self.medtable.heading("companyname",text="Company")
           self.medtable.heading("type",text="Type")
           self.medtable.heading("tabletname",text="Name")
           self.medtable.heading("qty",text="Quantity")
           self.medtable.heading("price",text="Price")
           self.medtable.heading("expdate",text="Expiry")
           self.medtable.heading("uses",text="Uses")
           self.medtable.heading("sideeffects",text="Side Effects")


           self.medtable.column("ref",width=60)
           self.medtable.column("companyname", width=60)
           self.medtable.column("type", width=60)
           self.medtable.column("tabletname", width=60)
           self.medtable.column("qty", width=60)
           self.medtable.column("price", width=60)
           self.medtable.column("expdate", width=60)
           self.medtable.column("uses",width=60)
           self.medtable.column("sideeffects", width=60)

           self.medtable.pack(fill=BOTH, expand=1)
           self.FetchMed()
           self.FetchData()


       def covid(self):
           webbrowser.open("https://covid19.who.int/")


       def chatbot(self):
            self.new_window=Toplevel(self.root)
            self.app=Chatbot(self.new_window)

       def patient(self):
            self.new_window=Toplevel(self.root)
            self.app=Hospital(self.new_window)

       def doctor(self):
            self.new_window=Toplevel(self.root)
            self.app=Doctor(self.new_window)

       def voice(self):
           self.new_window = Toplevel(self.root)
           self.app = Widget(self.new_window)

       def bill(self):
           self.new_window = Toplevel(self.root)
           self.app = Bill(self.new_window)



       #========================Add Medicine==============================

       def AddMed(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
           mycursor=conn.cursor()
           mycursor.execute("insert into pharmacy2 (Ref,MedName) values(%s,%s)",(self.var.get(),self.var2.get()))

           conn.commit()
           self.FetchMed()
           conn.close()
           messagebox.showinfo("Success","Medicine Added")


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
           conn.close()
           messagebox.showinfo("Success", "Data is inserted")


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


if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
