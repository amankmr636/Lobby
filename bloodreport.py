from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import random,os
from tkinter import messagebox
import datetime

class bloodreport:

    def __init__(self, root):
        self.root = root
        self.root.title("Blood Report Generator")
        self.root.geometry("1550x700+0+0")
        self.var = StringVar()
        self.var2 = StringVar()
        self.row2 = StringVar()
        a1 = random.randint(1000,10000)

        self.a1=StringVar()
        self.a1.set(a1)
        self.a2 = StringVar()
        self.a3 = StringVar()
        self.a4 = StringVar()
        self.a5 = StringVar()
        self.a6 = StringVar()
        self.a7 = StringVar()
        self.a8 = StringVar()
        self.a9 = StringVar()
        self.a10 = StringVar()
        self.a11=0
        self.a12 = 0
        self.a13 = 0
        self.a14=datetime.datetime.now().date()
        self.a15=str(self.a14)
        self.a16=StringVar()

        img = Image.open("C:\Billy.jpg")
        img = img.resize((1300, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        labelimg = Label(self.root, image=self.photoimg)
        labelimg.place(x=0, y=0, width=1300, height=90)
        labelttl = Label(self.root, text="Blood Report Generator", font=("times new roman", 30, "bold"), bg="white",
                         fg="red")
        labelttl.place(x=0, y=90, width=1540, height=45)


        MainFrame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        MainFrame.place(x=0, y=130, width=1530, height=620)


        #================================Label Frame 1====================================================

        lblframe = LabelFrame(MainFrame, text="Generate", font=("times new roman", 13, "bold"), fg="red", bg="white")
        lblframe.place(x=0, y=2, width=300, height=150)


        self.RID = Label(lblframe, text="Report ID", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.RID.grid(row=0, column=0, padx=5, pady=2)

        self.entryRID = ttk.Entry(lblframe, font=("times new roman", 10, "bold"), width=18, textvariable=self.a1)
        self.entryRID.grid(row=0, column=1, padx=5, pady=2)

        self.BloodGroup = Label(lblframe, text="Blood Group", font=("times new roman", 13, "bold"), fg="green",
                                 bg="white")
        self.BloodGroup.grid(row=1, column=0, padx=5, pady=2)

        BloodGroupCombo = ttk.Combobox(lblframe, width=12, font=("arial", 12, "bold"), state="readonly",
                                     textvariable=self.a2)
        BloodGroupCombo["values"] = ("A+", "O+", "O-","B+","AB-")
        BloodGroupCombo.grid(row=1, column=1)
        BloodGroupCombo.current(0)

        self.lblpatid = Label(lblframe, text="Patient ID", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.lblpatid.grid(row=2, column=0, padx=5, pady=2)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select distinct PatientID from consumes")
        row = mycursor.fetchall()

        lblpatidcombo = ttk.Combobox(lblframe, width=12, font=("arial", 12, "bold"), state="readonly",
                                     textvariable=self.a3)
        lblpatidcombo["values"] = row
        lblpatidcombo.grid(row=2, column=1)
        lblpatidcombo.current(0)

        btnadd = Button(lblframe, text="Add Header", width=10, font=("arial", 12, "bold"), bg="brown", fg="white",
                        pady=2, command=self.add)
        btnadd.grid(row=3, column=0)


        # =============================================Report Window=========================================

        self.textPresciption = Text(MainFrame, font=("times new roman", 12, "bold"), padx=4,
                                    pady=6, bg="gray", fg="white")
        self.textPresciption.place(x=0, y=160, width=1260, height=320)


        # ===========================================Label Frame 2================================================================

        lblframe2 = LabelFrame(MainFrame, text="Results", font=("times new roman", 13, "bold"), fg="red", bg="white")
        lblframe2.place(x=320, y=2, width=700, height=150)


        self.Bilirubin = Label(lblframe2, text="Bilirubin", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.Bilirubin.grid(row=2, column=0, padx=5, pady=2)


        Bilirubin2 = Entry(lblframe2, width=30, textvariable=self.a6)
        Bilirubin2.grid(row=2, column=1)

        self.ALT = Label(lblframe2, font=("times new roman", 13, "bold"), fg="Green", bg="white",text="ALT",
                             width=7)
        self.ALT.grid(row=0, column=0)


        ALT2 = Entry(lblframe2, width=30, textvariable=self.a4)
        ALT2.grid(row=0, column=1)


        self.ALP = Label(lblframe2, text="ALP", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.ALP.grid(row=1, column=0, padx=5, pady=2)

        ALP2 = Entry(lblframe2, width=30, textvariable=self.a5)
        ALP2.grid(row=1, column=1)

        self.RBC = Label(lblframe2, text="RBC", font=("times new roman", 13, "bold"), fg="green",
                               bg="white")
        self.RBC.grid(row=2, column=2, padx=5, pady=2)

        RBC2 = Entry(lblframe2, width=30, textvariable=self.a9)
        RBC2.grid(row=2, column=3)

        self.WBC = Label(lblframe2, font=("times new roman", 13, "bold"), fg="Green", bg="white", text="WBC",
                         width=7)
        self.WBC.grid(row=0, column=2)

        WBC2 = Entry(lblframe2, width=30, textvariable=self.a7)
        WBC2.grid(row=0, column=3)

        self.Haemoglobin = Label(lblframe2, text="Haemoglobin", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.Haemoglobin.grid(row=1, column=2, padx=5, pady=2)

        Haemoglobin2 = Entry(lblframe2, width=30, textvariable=self.a8)
        Haemoglobin2.grid(row=1, column=3)


        # ==================Label Frame 4======================================================================


        btninclude = Button(lblframe2, text="Include", width=7, font=("arial", 12, "bold"), bg="orange", fg="white", pady=2,
                          command=self.roomcart)
        btninclude.grid(row=3, column=2)

        lblframe5 = LabelFrame(MainFrame, text="Search", font=("times new roman", 13, "bold"), fg="red", bg="white")
        lblframe5.place(x=1030, y=2, width=230, height=150)


        self.docid = Label(lblframe5, text="Doctor ID", font=("times new roman", 13, "bold"), fg="green", bg="white")
        self.docid.grid(row=0, column=0, padx=5, pady=2)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select DoctorID from doctable")
        row3 = mycursor.fetchall()

        docid2 = ttk.Combobox(lblframe5, width=12, font=("arial", 12, "bold"), state="readonly", textvariable=self.a10)
        docid2["values"] = row3
        docid2.grid(row=0, column=1)
        docid2.current(0)


        btnprint = Button(self.root, text="Print", width=7, font=("arial", 12, "bold"), bg="Black", fg="white", pady=2,
                          command=self.print)
        btnprint.place(x=1173, y=244)


        btnClear = Button(self.root, text="Clear", width=7, font=("arial", 12, "bold"), bg="Blue", fg="white", pady=2,
                          command=self.clear)
        btnClear.place(x=1073,y=244)

        self.searc = ttk.Entry(lblframe5, font=("times new roman", 10, "bold"), width=18, textvariable=self.a16)
        self.searc.grid(row=1, column=1, padx=5, pady=2)


        btnsearc = Button(lblframe5, text="Search", width=7, font=("arial", 12, "bold"), bg="Green", fg="white", pady=2,
                          command=self.searchbill)
        btnsearc.grid(row=1, column=0)


    def print(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("insert into report values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.a1.get(),self.a3.get(),self.a15,self.a4.get(),self.a5.get(),self.a6.get(),self.a7.get(),self.a8.get(),self.a9.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Report Added to Database")

        self.reportdata=self.textPresciption.get(1.0,END)
        f1=open("Reports/"+str(self.a1.get())+".txt",'w')
        f1.write(self.reportdata)
        f1.close()

    def searchbill(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM report WHERE ReportID=%s", (self.a16.get(),))
        row8 = mycursor.fetchall()
        print(row8)

        self.textPresciption.delete("1.0", END)
        self.textPresciption.insert(END,
                                    "RNo PatId ALT ALP Bilir WBC Haemo RBC\n----------------------------------------------------------------------\n")

        for i in row8:
            self.textPresciption.insert(END,i)
            conn.commit()


        conn.close()


    def add(self):
        self.textPresciption.insert(END, "\t\t\t\t\t\t\t----------Blood Report----------- \n")
        self.textPresciption.insert(END,
                                    "Report ID: " + self.a1.get() + "\t\t Blood Group: " + self.a2.get() + "\t\t\tPatient ID: " + self.a3.get() + "\t\t\tDoc ID: " + self.a10.get() + "\t\t\tDate: "+self.a15+"\n\n")

        self.textPresciption.insert(END,
                                    "Component: " +  "\t\t\t\t" + "Result: " + "\t\t\t\t" + "Normal Range" + "\n\n")



    def roomcart(self):
            self.textPresciption.insert(END,
                                        "ALT : " +   "\t\t\t\t"+ self.a4.get() +"\t\t\t\t" +"7 to 56 U/L"+ "\n" + "ALP : "+"\t\t\t\t"+ self.a5.get() +"\t\t\t\t" +"44 to 147 U/L"+ "\n" + "Bilirubin : " + "\t\t\t\t" +
                                        self.a6.get() +"\t\t\t\t" +"0.3 to 1.2 "+"\n" + "WBC : " +"\t\t\t\t" + self.a7.get() +"\t\t\t\t" +"4500 to 11000 U/L"+"\n" + "Haemoglobin : " + "\t\t\t\t" + self.a8.get() +"\t\t\t\t" +"13.2 to 16.6 g/dL"+"\n" +"RBC : "+"\t\t\t\t" +self.a9.get()+"\t\t\t\t"+"4.35 to 5.45M " )


    def clear(self):
        self.textPresciption.delete("1.0", END)
        self.a4.set("")
        self.a5.set("")
        self.a6.set("")
        self.a7.set("")
        self.a8.set("")
        self.a9.set("")

        self.textPresciption.delete("1.0", END)


if __name__ == "__main__":
    root = Tk()
    obj = bloodreport(root)
    root.mainloop()
