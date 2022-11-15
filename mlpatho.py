from tkinter import *
import numpy as np
import pandas as pd
import seaborn as sns
import webbrowser
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mysql.connector
from tkinter import messagebox
import random


class Mlpatho:
    heart_data = pd.read_csv('data.csv')
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Disease Predictor")
        self.root.geometry("700x700")
        self.root.configure(background="light green")

        Button(self.root, text="Prediction", width=15, command=self.info, bg="sky blue").place(x=950, y=300)
        Button(self.root, text="Termination", width=15, command=root.destroy, bg="red").place(x=950, y=340)

        Label(self.root,text="Heart Disease Predictor",font=("Helvetica",15,'bold'),bg="light green",relief="solid").pack()
        Label(self.root,text="application version 1.1",font=("Helvetica",15,'bold'),bg="light green",relief="solid").pack(side=BOTTOM)

        Label(self.root,text="Age",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=60)
        Label(self.root,text="Sex",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=100)
        Label(self.root,text="Chest Pain",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=140)
        Label(self.root,text="Resting Blood Pressure",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=180)
        Label(self.root,text="Serum Cholestrol mg/dl",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=220)
        Label(self.root,text="Fasting Blood Sugar",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=260)
        Label(self.root,text="Resting Ecardiagraphic",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=300)
        Label(self.root,text="Maximum Heart Rate",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=340)
        Label(self.root,text="Exercised Induced Angina",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=380)
        Label(self.root,text="Oldpeak",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=420)
        Label(self.root,text="Slope",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=460)
        Label(self.root,text="No. of major vessels",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=500)
        Label(self.root,text="Thal",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=540)

        self.var = StringVar()
        z = random.randint(1000, 9999)
        self.var.set(z)
        self.var1=StringVar()
        self.var2=StringVar()

        self.d1=StringVar()
        self.d2=StringVar()
        self.d3=StringVar()
        self.d4=StringVar()
        self.d5=StringVar()
        self.d6=StringVar()
        self.d7=StringVar()
        self.d8=StringVar()
        self.d9=StringVar()
        self.d10=StringVar()
        self.d11=StringVar()
        self.d12=StringVar()
        self.d13=StringVar()



        Entry(self.root,textvariable=self.d1,width=30).place(x=440,y=60)
        Entry(self.root,textvariable=self.d2,width=30).place(x=440,y=100)
        Entry(self.root,textvariable=self.d3,width=30).place(x=440,y=140)
        Entry(self.root,textvariable=self.d4,width=30).place(x=440,y=180)
        Entry(self.root,textvariable=self.d5,width=30).place(x=440,y=220)
        Entry(self.root,textvariable=self.d6,width=30).place(x=440,y=260)
        Entry(self.root,textvariable=self.d7,width=30).place(x=440,y=300)
        Entry(self.root,textvariable=self.d8,width=30).place(x=440,y=340)
        Entry(self.root,textvariable=self.d9,width=30).place(x=440,y=380)
        Entry(self.root,textvariable=self.d10,width=30).place(x=440,y=420)
        Entry(self.root,textvariable=self.d11,width=30).place(x=440,y=460)
        Entry(self.root,textvariable=self.d12,width=30).place(x=440,y=500)
        Entry(self.root,textvariable=self.d13,width=30).place(x=440,y=540)


        Label(self.root,text="Information",font=("Helvetica",10,"bold",),bg="light green",relief="solid",
              width=25).place(x=900,y=250)

        self.textPrediction = Text(self.root, font=("times new roman", 12, "bold"), width=30, height=2, fg="white",
                                   bg="black", padx=2, pady=6)
        self.textPrediction.place(x=900, y=50)

        self.textPrediction2 = Text(self.root, font=("times new roman", 12, "bold"), width=30, height=2, fg="white",
                                    bg="black",
                                    padx=2, pady=6)
        self.textPrediction2.place(x=900, y=150)

        self.textPrediction.insert(END,"Result")
        self.textPrediction2.insert(END, "Accuracy")


        Button(self.root, text="Contact", width=15, command=self.contact, bg="green").place(x=950, y=380)

        lbl4 = Label(self.root, font=("arial", 12, "bold"), fg="White", bg="Black", text="PatientID", padx=2)
        lbl4.place(x=900, y=460)

        lbl5 = Label(self.root, font=("arial", 12, "bold"), fg="White", bg="Black", text="    Date    ", padx=2)
        lbl5.place(x=900, y=500)

        Entry1 = Entry(self.root, textvariable=self.var1, bd=3, relief=RIDGE, width=10, font=("arial", 12, "bold"))
        Entry1.place(x=1000, y=460)

        Entry2 = Entry(self.root, textvariable=self.var2, bd=3, relief=RIDGE, width=10, font=("arial", 12, "bold"))
        Entry2.place(x=1000, y=500)

        btndatabase = Button(self.root, bg="Red", height=3, width=10, text="SAVE", fg="white",
                             font=("times new roman", 10, "bold"), command=self.save)
        btndatabase.place(x=900, y=540)

        btnclear = Button(self.root, bg="Black", height=3, width=10, text="CLEAR", fg="white",
                          font=("times new roman", 10, "bold"), command=self.clear)
        btnclear.place(x=1000, y=540)

    def info(self):
        heart_data = pd.read_csv('data.csv')

        X=heart_data.drop(columns='target',axis=1)
        Y=heart_data['target']

        model=LogisticRegression()
        model.fit(X,Y)

        #accuracy
        Xpredict=model.predict(X)
        accuracy=accuracy_score(Xpredict,Y)
        print(accuracy)
        acc=float(accuracy*100)
        acc2=round(acc,2)
        acc2=str(acc2)
        self.textPrediction2.delete("1.0",END)
        self.textPrediction2.insert(END,acc2)



        inputdata=(int(self.d1.get()),int(self.d2.get()),int(self.d3.get()),int(self.d4.get()),int(self.d5.get())
                   ,int(self.d6.get()),int(self.d7.get()),int(self.d8.get()),int(self.d9.get()),
                   float(self.d10.get()),int(self.d11.get()),int(self.d12.get()),int(self.d13.get()))


        inputdataarray=np.asarray(inputdata)
        inputdatareshaped=inputdataarray.reshape(1,-1)
        prediction=model.predict(inputdatareshaped)
        print(prediction)

        if(prediction[0]==1):
            self.textPrediction.delete("1.0", END)
            self.textPrediction.insert(END,"Heart Disease")
        else:
            self.textPrediction.delete("1.0", END)
            self.textPrediction.insert(END,"Normal")


        

    def contact(self):
        heart_data = pd.read_csv('data.csv')
        webbrowser.open("https://www.google.com/search?q=cardiologist+near+me&rlz=1C1AWFC_enIN995IN996&oq=cardiologist+near+me&aqs=chrome..69i57j0i402j0i512l8.5971j0j9&sourceid=chrome&ie=UTF-8")
        heart_data.hist(figsize=(14, 14))
        plt.show()

    def plot(self):
        heart_data = pd.read_csv('data.csv')
        attr1=heart_data[heart_data['target']==1]

        attr0=heart_data[heart_data['target']==0]

        sns.pairplot(self.heart_data,hue='target',vars=['age','trestbps','chol'])
        plt.show()


    def save(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()

        mycursor.execute("insert into reporttable (IDNO,PatientID,Date,Accuracy,Result,Predictionfor) values(%s,%s,%s,%s,%s,%s)",
                         (self.var.get(), self.var1.get(),self.var2.get(), self.textPrediction2.get("1.0",END),self.textPrediction.get("1.0",END),"Diabetes"))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data Saved")

    def clear(self):
        self.var1.set("")
        self.var2.set("")
        self.d1.set("")
        self.d2.set("")
        self.d3.set("")
        self.d4.set("")
        self.d5.set("")
        self.d6.set("")
        self.d7.set("")
        self.d8.set("")
        self.d9.set("")
        self.d10.set("")
        self.d11.set("")
        self.d12.set("")
        self.d13.set("")


if __name__=="__main__":

    root = Tk()
    obj = Mlpatho(root)
    root.mainloop()


