from tkinter import *
from tkinter import ttk

import pandas as pd
from PIL import Image,ImageTk
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import messagebox


class Plot:

    def __init__(self,root):
        self.a=StringVar()
        self.var=StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()

        self.root=root
        self.root.title("Visualization")
        self.root.geometry("600x220")
        self.root.maxsize(600,220)

        self.root.configure(background="gray")


        img = Image.open("C:\wfront3.jpg")
        img = img.resize((1000, 500))

        self.photoimg = ImageTk.PhotoImage(img)


        lblimg = Label(self.root, bd=15, relief=RIDGE,
                          image=self.photoimg, padx=2,
                          pady=4, height=500)
        lblimg.place(x=0, y=0, width=600, height=220)

        lbl = Label(lblimg, font=("arial", 12, "bold"), text="Type", padx=2,bg="black",fg="white")
        lbl.place(x=10,y=20)

        plot = ttk.Combobox(lblimg, width=25, textvariable=self.var, font=("arial", 12, "bold"))
        plot["values"] = ('relplot','linear','boxplot')
        plot.place(x=90,y=20)

        lblheart = Label(lblimg, font=("arial", 12, "bold"), text="Para1", padx=2, bg="black", fg="white")
        lblheart.place(x=10, y=50)

        plot2 = ttk.Combobox(lblimg, width=25, textvariable=self.var2, font=("arial", 12, "bold"))
        plot2["values"] = ('age', 'cp','trestbps','target')
        plot2.place(x=90, y=50)

        lblheart2 = Label(lblimg, font=("arial", 12, "bold"), text="Para2", padx=2, bg="black", fg="white")
        lblheart2.place(x=10, y=80)

        plot3 = ttk.Combobox(lblimg, width=25, textvariable=self.var3, font=("arial", 12, "bold"))
        plot3["values"] = ('age', 'cp','trestbps','target')
        plot3.place(x=90, y=80)


        lbldiab = Label(lblimg, font=("arial", 12, "bold"), text="Para1", padx=2, bg="brown", fg="white")
        lbldiab.place(x=10, y=110)

        plot4 = ttk.Combobox(lblimg, width=25, textvariable=self.var4, font=("arial", 12, "bold"))
        plot4["values"] = ('Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Outcome')
        plot4.place(x=90, y=110)


        lbldiab = Label(lblimg, font=("arial", 12, "bold"), text="Para2", padx=2, bg="brown", fg="white")
        lbldiab.place(x=10, y=140)

        plot5 = ttk.Combobox(lblimg, width=25, textvariable=self.var5, font=("arial", 12, "bold"))
        plot5["values"] = ('Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Outcome')
        plot5.place(x=90, y=140)

        Button(lblimg, text="Heart", width=15, command=self.ploth, bg="red").place(x=370, y=50)
        Button(lblimg, text="Diab ", width=15, command=self.plotd, bg="sky blue").place(x=370, y=110)

    def ploth(self):
        data=pd.read_csv("data.csv")
        self.a=self.var.get()

        if(self.a=="relplot"):

                sns.relplot(x=self.var2.get(),y=self.var3.get(),data=data,hue='sex')
                plt.show()

        elif(self.a=="linear"):
                sns.lineplot(x=self.var2.get(), y=self.var3.get(), data=data, hue='sex')
                plt.show()

        else:
                sns.boxplot(x=self.var2.get(), y=self.var3.get(), data=data, hue='sex')
                plt.show()


    def plotd(self):
        data=pd.read_csv("diabetes.csv")
        self.a=self.var.get()

        if(self.a=="relplot"):

                sns.relplot(x=self.var4.get(),y=self.var5.get(),data=data)
                plt.show()

        elif(self.a=="linear"):
                sns.lineplot(x=self.var4.get(), y=self.var5.get(), data=data)
                plt.show()

        else:
                sns.boxplot(x=self.var4.get(), y=self.var5.get(), data=data)
                plt.show()


if __name__=="__main__":

    root = Tk()
    obj = Plot(root)
    root.mainloop()




