from tkinter import *
from tkinter import messagebox
import pandas as pd
from tkinter import ttk
from sklearn import tree
import mysql.connector
import random
from sklearn.metrics import accuracy_score
from PIL import Image,ImageTk


class Diseaseml:
    def __init__(self, root):
        self.var2=StringVar()
        self.var3=StringVar()

        self.var = StringVar()
        z = random.randint(1000, 9999)
        self.var.set(z)


        self.root = root
        self.root.title("Disease Predictor")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="Disease Predictor", bd=15, relief=RIDGE,
                         bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4,width=31
                         )
        lbltitle.place(x=0,y=0)

        img = Image.open("C:\wfront2.jpg")
        img = img.resize((1280, 580))

        self.photoimg = ImageTk.PhotoImage(img)

        lbltitle2 = Label(self.root, bd=15, relief=RIDGE,
                            image=self.photoimg, padx=2,
                          pady=4, height=500)
        lbltitle2.place(x=0, y=110, width=1280, height=430)


        lbltitle3 = Label(self.root, bd=15, relief=RIDGE,text="Result",
                          font=("times new roman", 50, "bold"), padx=2,fg="Green", pady=4,width=31,height=1
                         )
        lbltitle3.pack(side=BOTTOM,fill=X)

        self.l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills',
              'joint_pain',
              'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
              'spotting_ urination', 'fatigue',
              'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
              'lethargy', 'patches_in_throat',
              'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
              'dehydration', 'indigestion',
              'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
              'back_pain', 'constipation',
              'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
              'fluid_overload',
              'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
              'throat_irritation',
              'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
              'fast_heart_rate',
              'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
              'dizziness', 'cramps',
              'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
              'brittle_nails',
              'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
              'slurred_speech', 'knee_pain', 'hip_joint_pain',
              'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements',
              'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
              'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine',
              'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
              'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
              'abnormal_menstruation', 'dischromic _patches',
              'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum',
              'lack_of_concentration', 'visual_disturbances',
              'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
              'distention_of_abdomen', 'history_of_alcohol_consumption',
              'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking',
              'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
              'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
              'yellow_crust_ooze']

        self.disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
                   'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
                   ' Migraine', 'Cervical spondylosis',
                   'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
                   'hepatitis A',
                   'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
                   'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                   'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
                   'Osteoarthristis',
                   'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
                   'Psoriasis',
                   'Impetigo']

        self.l2 = []

        self.Symptom1 = StringVar()
        self.Symptom1.set(None)
        self.Symptom2 = StringVar()
        self.Symptom2.set(None)
        self.Symptom3 = StringVar()
        self.Symptom3.set(None)
        self.Symptom4 = StringVar()
        self.Symptom4.set(None)
        self.Symptom5 = StringVar()
        self.Symptom5.set(None)


        S1Lb = Label(lbltitle2, text="Symptom 1",bg="Green",bd=15, relief=RIDGE)
        S1Lb.config(font=("Elephant", 15))
        S1Lb.grid(row=0, column=1, pady=10)

        S2Lb = Label(lbltitle2, text="Symptom 2",bg="Green",bd=15, relief=RIDGE)
        S2Lb.config(font=("Elephant", 15))
        S2Lb.grid(row=1, column=1, pady=10)

        S3Lb = Label(lbltitle2, text="Symptom 3",bg="Green",bd=15, relief=RIDGE)
        S3Lb.config(font=("Elephant", 15))
        S3Lb.grid(row=2, column=1, pady=10)

        S4Lb = Label(lbltitle2, text="Symptom 4",bg="Green",bd=15, relief=RIDGE)
        S4Lb.config(font=("Elephant", 15))
        S4Lb.grid(row=3, column=1, pady=10)

        S5Lb = Label(lbltitle2, text="Symptom 5",bg="Green",bd=15, relief=RIDGE)
        S5Lb.config(font=("Elephant", 15))
        S5Lb.grid(row=4, column=1, pady=10)


        OPTIONS = sorted(self.l1)

        sym1 = ttk.Combobox(lbltitle2, textvariable=self.Symptom1, width=25, font=("arial", 12, "bold"),
                                 state="readonly")
        sym1["values"] = OPTIONS
        sym1.grid(row=0, column=3)


        sym2 = ttk.Combobox(lbltitle2, textvariable=self.Symptom2, width=25, font=("arial", 12, "bold"),
                                 state="readonly")
        sym2["values"] = OPTIONS
        sym2.grid(row=1, column=3)

        sym3 = ttk.Combobox(lbltitle2, textvariable=self.Symptom3, width=25, font=("arial", 12, "bold"),
                            state="readonly")
        sym3["values"] = OPTIONS
        sym3.grid(row=2, column=3)

        sym4 = ttk.Combobox(lbltitle2, textvariable=self.Symptom4, width=25, font=("arial", 12, "bold"),
                            state="readonly")
        sym4["values"] = OPTIONS
        sym4.grid(row=3, column=3)

        sym5 = ttk.Combobox(lbltitle2, textvariable=self.Symptom5, width=25, font=("arial", 12, "bold"),
                            state="readonly")
        sym5["values"] = OPTIONS
        sym5.grid(row=4, column=3)

        lbl1 = Label(lbltitle2, font=("arial", 12, "bold"), fg="White",bg="Black",text="D-Tree  ", padx=2)
        lbl1.place(x=530,y=82)

        lbl2 = Label(lbltitle2, font=("arial", 12, "bold"), fg="White", bg="Black", text="NBayes", padx=2)
        lbl2.place(x=530, y=122)

        lbl3 = Label(lbltitle2, font=("arial", 12, "bold"), fg="White", bg="Black", text="RForest", padx=2)
        lbl3.place(x=530, y=162)

        self.t3 = Text(lbltitle2, height=1, width=10)
        self.t3.config(font=("Elephant", 20))
        self.t3.place(x=600,y=80)

        self.t4 = Text(lbltitle2, height=1, width=10)
        self.t4.config(font=("Elephant", 20))
        self.t4.place(x=600,y=120)

        self.t5 = Text(lbltitle2, height=1, width=10)
        self.t5.config(font=("Elephant", 20))
        self.t5.place(x=600, y=160)

        self.t6 = Text(lbltitle3, height=1, width=20,fg="White",bg="Black")
        self.t6.config(font=("Elephant", 20))
        self.t6.place(x=10, y=20)

        self.t7 = Text(lbltitle3, height=1, width=10, fg="White", bg="Black")
        self.t7.config(font=("Elephant", 20))
        self.t7.place(x=990, y=20)

        self.t6.insert(END, "Result")
        self.t7.insert(END,"Accuracy")

        lbl4 = Label(lbltitle2, font=("arial", 12, "bold"), fg="White", bg="Black", text="PatientID", padx=2)
        lbl4.place(x=1010, y=20)

        lbl5 = Label(lbltitle2, font=("arial", 12, "bold"), fg="White", bg="Black", text="    Date    ", padx=2)
        lbl5.place(x=1010, y=50)

        Entry1 = Entry(lbltitle2, textvariable=self.var2, bd=3, relief=RIDGE, width=10, font=("arial", 12, "bold"))
        Entry1.place(x=1100,y=20)

        Entry2 = Entry(lbltitle2, textvariable=self.var3, bd=3, relief=RIDGE, width=10, font=("arial", 12, "bold"))
        Entry2.place(x=1100,y=50)

        btnpid = Button(lbltitle2, bg="Blue", height=1, width=10, text="PREDICT", fg="white",
                        font=("times new roman", 10, "bold"), command=self.dtree)
        btnpid.place(x=660, y=30)


        btndatabase = Button(lbltitle2, bg="Red", height=3, width=10, text="SAVE", fg="white",
                        font=("times new roman", 10, "bold"), command=self.save)
        btndatabase.place(x=1100, y=150)

        btnclear = Button(lbltitle2, bg="Black", height=1, width=10, text="CLEAR", fg="white",
                        font=("times new roman", 10, "bold"), command=self.clear)
        btnclear.place(x=1100, y=250)

        for x in range(0,len(self.l1)):
            self.l2.append(0)

        df=pd.read_csv("distest.csv")

        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        self.xtest=df[self.l1]
        self.ytest=df[["prognosis"]]

        self.df2=pd.read_csv("distrain.csv")

        self.df2.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        self.xtrain=self.df2[self.l1]
        self.ytrain=self.df2[["prognosis"]]


    def save(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@", database="pharma")
        mycursor = conn.cursor()

        mycursor.execute("insert into reporttable (IDNO,PatientID,Date,Accuracy,Result,Predictionfor) values(%s,%s,%s,%s,%s,%s)",
                         (self.var.get(), self.var2.get(),self.var3.get(), self.t7.get("1.0",END),"Unhealthy","General"))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data Saved")
    def clear(self):
        self.var2.set("")
        self.var3.set("")
        self.t3.delete("1.0", END)
        self.t4.delete("1.0", END)
        self.t5.delete("1.0", END)
        self.t6.delete("1.0", END)
        self.t7.delete("1.0", END)

    def calculate(self):

        if (self.t3.get("1.0",END) == self.t4.get("1.0",END)):
            self.t6.delete("1.0",END)
            self.t6.insert(END,self.t3.get("1.0",END))
            acc2=(self.a+self.b)/2
            self.t7.delete("1.0", END)
            self.t7.insert(END,acc2*100)

        elif (self.t4.get("1.0",END) == self.t5.get("1.0",END)):
            self.t6.delete("1.0", END)
            self.t6.insert(END,self.t4.get("1.0",END))
            acc2 = (self.b + self.c) / 2
            self.t7.delete("1.0", END)
            self.t7.insert(END,acc2*100)

        elif (self.t3.get("1.0",END) == self.t5.get("1.0",END)):
            self.t6.delete("1.0", END)
            self.t6.insert(END,self.t3.get("1.0",END))
            acc2 = (self.c + self.a) / 2
            self.t7.delete("1.0", END)
            self.t7.insert(END,acc2*100)

        else:
            self.t6.delete("1.0", END)
            self.t7.delete("1.0", END)
            self.t6.insert(END,"Cant Determine")
            self.t7.insert(END,"0%")


    def message(self):
        if(self.Symptom1.get()=="None" and self.Symptom2.get()=="None" and self.Symptom3.get()=="None" and self.Symptom4.get() == "None" and self.Symptom5.get() == "None"):
                 messagebox.showinfo("Enter Symptoms Please")

        else:
                self.dtree()

    def dtree(self):
            model=tree.DecisionTreeClassifier()
            model.fit(self.xtrain,self.ytrain)
            ypred=model.predict(self.xtest)
            self.a=accuracy_score(self.ytest,ypred)


            psymptoms = [self.Symptom1.get(), self.Symptom2.get(), self.Symptom3.get(), self.Symptom4.get(), self.Symptom5.get()]

            for k in range(0, len(self.l1)):
                for z in psymptoms:
                    if (z == self.l1[k]):
                        self.l2[k] = 1

            inputtest = [self.l2]
            predict = model.predict(inputtest)
            predicted = predict[0]


            print(predict)
            print(predicted)

            h = 'no'

            for a in range(0, len(self.disease)):
                if (self.disease[predicted] == self.disease[a]):
                    h = 'yes'
                    break

            if (h == 'yes'):
                self.t3.delete("1.0", END)
                self.t3.insert(END, self.disease[a])

            else:
                self.t3.delete("1.0", END)
                self.t3.insert(END, "No Disease")

            self.nbayes()

    def nbayes(self):

        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        model.fit(self.xtrain, self.ytrain)
        ypred = model.predict(self.xtest)
        self.b=model.score(self.xtest, self.ytest)

        psymptoms = [self.Symptom1.get(), self.Symptom2.get(), self.Symptom3.get(), self.Symptom4.get(),
                     self.Symptom5.get()]

        for k in range(0, len(self.l1)):
            for z in psymptoms:
                if (z == self.l1[k]):
                    self.l2[k] = 1

        inputtest = [self.l2]
        predict = model.predict(inputtest)
        predicted = predict[0]


        h = 'no'

        for a in range(0, len(self.disease)):
            if (self.disease[predicted] == self.disease[a]):
                h = 'yes'
                break

        if (h == 'yes'):
            self.t4.delete("1.0", END)
            self.t4.insert(END, self.disease[a])

        else:
            self.t4.delete("1.0", END)
            self.t4.insert(END, "No Disease")

        self.rforest()

    def rforest(self):

        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
        model.fit(self.xtrain, self.ytrain)
        ypred = model.predict(self.xtest)
        self.c=model.score(self.xtest, self.ytest)


        psymptoms = [self.Symptom1.get(), self.Symptom2.get(), self.Symptom3.get(), self.Symptom4.get(),
                     self.Symptom5.get()]

        for k in range(0, len(self.l1)):
            for z in psymptoms:
                if (z == self.l1[k]):
                    self.l2[k] = 1

        inputtest = [self.l2]
        predict = model.predict(inputtest)
        predicted = predict[0]

        print(predict)
        print(predicted)

        h = 'no'

        for a in range(0, len(self.disease)):
            if (self.disease[predicted] == self.disease[a]):
                h = 'yes'
                break

        if (h == 'yes'):
            self.t5.delete("1.0", END)
            self.t5.insert(END, self.disease[a])

        else:
            self.t5.delete("1.0", END)
            self.t5.insert(END, "No Disease")

        self.calculate()

if __name__=="__main__":

    root = Tk()
    obj = Diseaseml(root)
    root.mainloop()