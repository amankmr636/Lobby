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

class Diabetes:
    def __init__(self,root):
        diabdata = pd.read_csv("diabetes.csv")
        self.root=root
        self.root.title("Diabetes Predictor")
        self.root.geometry("700x700")
        self.root.configure(background="aqua")

        Label(self.root,text="Pregnancies",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=60)
        Label(self.root,text="Glucose",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=100)
        Label(self.root,text="BloodPressure",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=140)
        Label(self.root,text="SkinThickness",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=180)
        Label(self.root,text="Insulin",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=220)
        Label(self.root,text="BMI",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=260)
        Label(self.root,text="DiabetesPedigreeFunction",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=300)
        Label(self.root,text="Age",font=("Helvetica",15,'bold'),bg="light green",relief="solid",width=20).place(x=40,y=340)

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


        Entry(self.root,textvariable=self.d1,width=30).place(x=440,y=60)
        Entry(self.root,textvariable=self.d2,width=30).place(x=440,y=100)
        Entry(self.root,textvariable=self.d3,width=30).place(x=440,y=140)
        Entry(self.root,textvariable=self.d4,width=30).place(x=440,y=180)
        Entry(self.root,textvariable=self.d5,width=30).place(x=440,y=220)
        Entry(self.root,textvariable=self.d6,width=30).place(x=440,y=260)
        Entry(self.root,textvariable=self.d7,width=30).place(x=440,y=300)
        Entry(self.root,textvariable=self.d8,width=30).place(x=440,y=340)


        diabdata['Glucose']=diabdata['Glucose'].replace(0,diabdata['Glucose'].mean())
        diabdata['BloodPressure'] = diabdata['BloodPressure'].replace(0, diabdata['BloodPressure'].mean())
        diabdata['SkinThickness'] = diabdata['SkinThickness'].replace(0, diabdata['SkinThickness'].mean())
        diabdata['Insulin'] = diabdata['Insulin'].replace(0, diabdata['Insulin'].mean())
        diabdata['BMI'] = diabdata['BMI'].replace(0, diabdata['BMI'].mean())
        diabdata2=diabdata


        Button(self.root, text="Prediction", width=15, command=self.info, bg="sky blue").place(x=940, y=300)
        Button(self.root, text="Termination", width=15, command=root.destroy, bg="red").place(x=940, y=350)
        Button(self.root, text="Contact", width=15, command=self.contact, bg="green").place(x=940, y=400)

        Label(self.root,text="Information",font=("Helvetica",10,"bold",),bg="gray",relief="solid",width=25).place(x=900,y=250)
        Label(self.root,text="Diabetes Predictor",font=("Helvetica",15,'bold'),bg="light green",relief="solid").pack()
        Label(self.root,text="application version 1.1",font=("Helvetica",15,'bold'),bg="light green",relief="solid").pack(side=BOTTOM)

        Label(self.root, text="Information", font=("Helvetica", 10, "bold",), bg="gray", relief="solid",
              width=25).place(x=900, y=250)
        self.textPrediction = Text(self.root, font=("times new roman", 12, "bold"), width=30, height=2,fg="white",bg="black", padx=2, pady=6)
        self.textPrediction.place(x=900,y=50)

        self.textPrediction2 = Text(self.root, font=("times new roman", 12, "bold"), width=30, height=2,fg="white", bg="black",
                              padx=2, pady=6)
        self.textPrediction2.place(x=900,y=150)

        self.textPrediction.insert(END,"Result")
        self.textPrediction2.insert(END, "Accuracy")

        lbl4 = Label(self.root, font=("arial", 12, "bold"), fg="White", bg="Black", text="PatientID", padx=2)
        lbl4.place(x=150 ,y=490)

        lbl5 = Label(self.root, font=("arial", 12, "bold"), fg="White", bg="Black", text="    Date    ", padx=2)
        lbl5.place(x=150, y=540)

        Entry1 = Entry(self.root, textvariable=self.var1, bd=3, relief=RIDGE, width=10, font=("arial", 12, "bold"))
        Entry1.place(x=280, y=490)

        Entry2 = Entry(self.root, textvariable=self.var2, bd=3, relief=RIDGE, width=10, font=("arial", 12, "bold"))
        Entry2.place(x=280, y=540)

        btndatabase = Button(self.root, bg="Red", height=3, width=10, text="SAVE", fg="white",
                             font=("times new roman", 10, "bold"), command=self.save)
        btndatabase.place(x=500, y=490)

        btnclear = Button(self.root, bg="Black", height=3, width=10, text="CLEAR", fg="white",
                          font=("times new roman", 10, "bold"), command=self.clear)
        btnclear.place(x=700, y=490)

    def info(self):

        diabdata = pd.read_csv("diabetes.csv")
        diabdata['Glucose'] = diabdata['Glucose'].replace(0, diabdata['Glucose'].mean())
        diabdata['BloodPressure'] = diabdata['BloodPressure'].replace(0, diabdata['BloodPressure'].mean())
        diabdata['SkinThickness'] = diabdata['SkinThickness'].replace(0, diabdata['SkinThickness'].mean())
        diabdata['Insulin'] = diabdata['Insulin'].replace(0, diabdata['Insulin'].mean())
        diabdata['BMI'] = diabdata['BMI'].replace(0, diabdata['BMI'].mean())
        diabdata2 = diabdata


        X=diabdata2.drop('Outcome',axis=1)
        Y=diabdata2['Outcome']

        Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.20,random_state=42)

        model=LogisticRegression()
        model.fit(Xtrain,Ytrain)

        #accuracy
        Xpredict=model.predict(Xtest)
        accuracy=accuracy_score(Xpredict,Ytest)
        acc=accuracy
        acc=float(accuracy*100)
        acc2=round(acc,2)
        acc2=str(acc2)
        self.textPrediction2.delete("1.0", END)
        self.textPrediction2.insert(END,acc2)



        inputdata=(int(self.d1.get()),float(self.d2.get()),float(self.d3.get()),float(self.d4.get()),float(self.d5.get())
                   ,float(self.d6.get()),float(self.d7.get()),int(self.d8.get()))


        inputdataarray=np.asarray(inputdata)
        inputdatareshaped=inputdataarray.reshape(1,-1)
        prediction=model.predict(inputdatareshaped)

        print(prediction)

        if(prediction[0]==1):
            self.textPrediction.delete("1.0", END)
            self.textPrediction.insert(END,"Diabetes")
        else:
            self.textPrediction.delete("1.0", END)
            self.textPrediction.insert(END, "Normal")

    def contact(self):
        webbrowser.open("https://www.google.com/search?q=diabetes+doctor+near+me&rlz=1C1AWFC_enIN995IN996&oq=diabetes+doctor+near+me&aqs=chrome..69i57j0i402l2j0i512l2j0i22i30l5.6304j1j7&sourceid=chrome&ie=UTF-8")

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
        self.t6.delete("1.0", END)
        self.t7.delete("1.0", END)

def plot(self):
        diabdata = pd.read_csv('diabetes.csv')
        attr1=diabdata[diabdata['target']==1]

        attr0=diabdata[diabdata['target']==0]

        sns.pairplot(self.heart_data,hue='target',vars=['age','trestbps','chol'])
        plt.show()




if __name__=="__main__":

    root = Tk()
    obj = Diabetes(root)
    root.mainloop()




