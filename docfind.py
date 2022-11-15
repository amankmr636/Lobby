from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import Image,ImageTk
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import messagebox
import mysql.connector

class Docfind:

    def __init__(self,root):
        self.a=StringVar()
        self.var=StringVar()


        self.root=root
        self.root.title("Find Your Doctor")
        self.root.geometry("1000x520")
        self.root.maxsize(1000,520)

        img = Image.open("C:\window.jpg")
        img = img.resize((1200, 520))

        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, bd=15, relief=RIDGE,
                       image=self.photoimg, padx=2,
                       pady=4, height=500)
        lblimg.place(x=0, y=0, width=1000, height=520)

        self.frame=Frame(lblimg)
        self.frame.place(x=40, y=100)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select Specialization from doctable")
        row = mycursor.fetchall()

        drop = ttk.Combobox(lblimg, width=25, textvariable=self.var, font=("arial", 12, "bold"))
        drop["values"] = row
        drop.place(x=40, y=20)
        drop.current(1)

        ScrollX=ttk.Scrollbar(lblimg,orient=HORIZONTAL)
        ScrollY=ttk.Scrollbar(lblimg,orient=VERTICAL)

        self.doctable=ttk.Treeview(self.frame,column=("Doctor ID","Doctor Name","Qualification","Specialization","Experience","Contact No"),xscrollcommand=ScrollX,yscrollcommand=ScrollY)
        ScrollX.pack(side=BOTTOM,fill=X)
        ScrollY.pack(side=RIGHT,fill=Y)

        btn=Button(lblimg,bg="red",text="Show",fg="white",font=("arial",12,"bold"),width=15,command=self.FetchData)
        btn.place(x=400,y=20)

        btn2=Button(lblimg,bg="black",text="Exit",fg="white",font=("arial",12,"bold"),width=15,command=root.destroy)
        btn2.place(x=600,y=20)

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


    def FetchData(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="Aman9174245164@",database="pharma")
        mycursor=conn.cursor()
        mycursor.execute("select * from doctable where Specialization=%s",(self.var.get(),))
        row=mycursor.fetchall()
        if len(row)!=0:
            self.doctable.delete(*self.doctable.get_children())
            for i in row:
                self.doctable.insert("",END,values=i)
            conn.commit()
        conn.close()





if __name__=="__main__":

    root = Tk()
    obj = Docfind(root)
    root.mainloop()
