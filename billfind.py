from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import Image,ImageTk
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import messagebox
import mysql.connector

class Billfind:

    def __init__(self,root):
        self.a=StringVar()
        self.var=StringVar()
        self.var2=StringVar()


        self.root=root
        self.root.title("Find Your Bill")
        self.root.geometry("1200x720")

        img = Image.open("C:\window2.jpg")
        img = img.resize((1680, 1020))

        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, bd=15, relief=RIDGE,
                       image=self.photoimg, padx=2,
                       pady=4, height=500)
        lblimg.place(x=0, y=0, width=1600, height=920)

        self.frame=Frame(lblimg)
        self.frame.place(x=40, y=100)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select distinct patid from bill")
        row = mycursor.fetchall()


        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select billid from bill")
        row2 = mycursor.fetchall()

        drop = ttk.Combobox(lblimg, width=25, textvariable=self.var, font=("arial", 12, "bold"))
        drop["values"] = row
        drop.place(x=40, y=20)
        drop.current(1)



        drop2 = ttk.Combobox(lblimg, width=25, textvariable=self.var2, font=("arial", 12, "bold"))
        drop2["values"] = row2
        drop2.place(x=40, y=420)
        drop2.current(1)

        self.text=Text(lblimg,width=110,height=8)
        self.text.place(x=40,y=480)

        btn3=Button(lblimg,bg="green",text="Print",fg="white",font=("arial",12,"bold"),width=15,command=self.Print)
        btn3.place(x=400,y=420)

        ScrollX=ttk.Scrollbar(lblimg,orient=HORIZONTAL)
        ScrollY=ttk.Scrollbar(lblimg,orient=VERTICAL)


        self.table=ttk.Treeview(self.frame,column=("Bill ID","Bill Type","Patient ID","Total","Date"),xscrollcommand=ScrollX,yscrollcommand=ScrollY)
        ScrollX.pack(side=BOTTOM,fill=X)
        ScrollY.pack(side=RIGHT,fill=Y)

        btn=Button(lblimg,bg="red",text="Show",fg="white",font=("arial",12,"bold"),width=15,command=self.FetchData)
        btn.place(x=400,y=20)

        btn2=Button(lblimg,bg="black",text="Exit",fg="white",font=("arial",12,"bold"),width=15,command=root.destroy)
        btn2.place(x=600,y=20)

        ScrollX.config(command=self.table.xview)
        ScrollY.config(command=self.table.yview)

        self.table.heading("Bill ID", text="Bill ID")
        self.table.heading("Bill Type", text="Bill Type")
        self.table.heading("Patient ID", text="Patient ID")
        self.table.heading("Total", text="Total")
        self.table.heading("Date", text="Date")


        self.table.column("Bill ID", width=100)
        self.table.column("Bill Type", width=100)
        self.table.column("Patient ID", width=100)
        self.table.column("Total", width=100)
        self.table.column("Date", width=100)
        self.table.pack(fill=BOTH, expand=1)

        self.FetchData()


    def FetchData(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
        mycursor=conn.cursor()
        mycursor.execute("select * from bill where patid=%s",(self.var.get(),))
        row=mycursor.fetchall()
        if len(row)!=0:
            self.table.delete(*self.table.get_children())
            for i in row:
                self.table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def Print(self):

        self.a=self.var2.get()

        f1=open("bills/"+str(self.var2.get())+".txt",'r')
        for i in f1:
            self.text.insert(END,i)
            self.text.insert(END,"\n")


        f1.close()


if __name__=="__main__":

    root = Tk()
    obj = Billfind(root)
    root.mainloop()
