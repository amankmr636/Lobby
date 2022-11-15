from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Plot:

    def __init__(self,root):
        self.a=StringVar()
        self.var=StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()

        self.root=root
        self.root.title("Book Appointment")
        self.root.geometry("700x520")
        self.root.maxsize(700,520)

        img = Image.open("C:\wfront3.jpg")
        img = img.resize((1000, 500))

        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, bd=15, relief=RIDGE,
                       image=self.photoimg, padx=2,
                       pady=4, height=500)
        lblimg.place(x=0, y=0, width=700, height=520)

        lbl = Label(lblimg, font=("arial", 12, "bold"), text="DocID", padx=2,bg="black",fg="white")
        lbl.place(x=10,y=20)

        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()
        mycursor.execute("select DoctorID from doctable")
        row = mycursor.fetchall()

        plot = ttk.Combobox(lblimg, width=25, textvariable=self.var, font=("arial", 12, "bold"))
        plot["values"] = row
        plot.place(x=100,y=20)












if __name__=="__main__":

    root = Tk()
    obj = Plot(root)
    root.mainloop()












