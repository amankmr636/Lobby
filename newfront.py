from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from diseaseml import Diseaseml
from mlpatho import Mlpatho
from diabetes import Diabetes
from voice import Widget
from plot import Plot
from reg import Reg
from chatbotml import Mlbot
from drugbot import Drugbot
from bookappoint2 import Appointment
from docfind import Docfind
from billfind import Billfind


class Front:
       def __init__(self,root):

           self.pid=StringVar()

           self.root=root
           self.root.title("PhaREXHA User")
           self.root.geometry("1550x800+0+0")
           lbltitle = Label(self.root, text="PhaREXHA Lobby HelpDesk", bd=15, relief=RIDGE,
                            bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
           lbltitle.pack(side=TOP, fill=X)


           img = Image.open("C:\wfornt.jpg")
           img = img.resize((1280, 580))

           self.photoimg = ImageTk.PhotoImage(img)

           lbltitle2 = Label(self.root, bd=15, relief=RIDGE,
                            bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), image=self.photoimg,padx=2, pady=4,height=500)
           lbltitle2.place(x=0, y=110, width=1280, height=400)

           DetailFrame = Frame(self.root, bd=20, relief=RIDGE)
           DetailFrame.place(x=0, y=510, width=1280, height=150)

           img1 = Image.open("C:\diseaselogo.png")
           img1 = img1.resize((80, 80))

           self.photoimg1 = ImageTk.PhotoImage(img1)


           img2 = Image.open("C:\heartlogo.jpg")
           img2 = img2.resize((80, 80))

           self.photoimg2 = ImageTk.PhotoImage(img2)

           img3 = Image.open("C:\diabeteslogo.jpg")
           img3 = img3.resize((80, 80))

           self.photoimg3 = ImageTk.PhotoImage(img3)


           img4 = Image.open("C:\doctorlogo.jpg")
           img4 = img4.resize((80, 80))

           self.photoimg4 = ImageTk.PhotoImage(img4)

           img5 = Image.open("C:\ppointmentlogo.png")
           img5 = img5.resize((80, 80))

           self.photoimg5 = ImageTk.PhotoImage(img5)

           img6 = Image.open("C:\graphlogo.jpg")
           img6 = img6.resize((80, 80))

           self.photoimg6 = ImageTk.PhotoImage(img6)

           img7 = Image.open("C:\oicerecognition.jpg")
           img7 = img7.resize((80, 80))

           self.photoimg7 = ImageTk.PhotoImage(img7)

           img8 = Image.open("C:\chatbotlogo.png")
           img8 = img8.resize((80, 80))

           self.photoimg8 = ImageTk.PhotoImage(img8)

           img9 = Image.open("C:\druglogo.jpg")
           img9 = img9.resize((80, 80))

           self.photoimg9 = ImageTk.PhotoImage(img9)


           img10 = Image.open("C:\illlogo.jpg")
           img10 = img10.resize((350, 48))

           self.photoimg10 = ImageTk.PhotoImage(img10)

           img11 = Image.open("C:\eg.png")
           img11 = img11.resize((80, 80))

           self.photoimg11 = ImageTk.PhotoImage(img11)

           b1 = Button(self.root, image=self.photoimg1, borderwidth=0,command=self.disease)
           b1.place(x=100, y=140)
           b2 = Button(self.root, image=self.photoimg2, borderwidth=0,command=self.patho)
           b2.place(x=240, y=140)
           b3 = Button(self.root, image=self.photoimg3, borderwidth=0,command=self.diabetes)
           b3.place(x=380, y=140)

           b4 = Button(self.root, image=self.photoimg7, borderwidth=0,command=self.widget)
           b4.place(x=100, y=240)
           b5 = Button(self.root, image=self.photoimg8, borderwidth=0,command=self.widget2)
           b5.place(x=240, y=240)
           b6 = Button(self.root, image=self.photoimg9, borderwidth=0,command=self.drugbot)
           b6.place(x=380, y=240)


           b7 = Button(self.root, image=self.photoimg5, borderwidth=0,command=self.bookapt)
           b7.place(x=100, y=340)
           b8 = Button(self.root, image=self.photoimg6, borderwidth=0,command=self.plot)
           b8.place(x=240, y=340)
           b9 = Button(self.root, image=self.photoimg4, borderwidth=0,command=self.docfind)
           b9.place(x=380, y=340)

           b10 = Button(self.root, image=self.photoimg10, borderwidth=0,command=self.billfind)
           b10.place(x=100, y=440)

           b11 = Button(self.root, image=self.photoimg11, borderwidth=0,command=self.reg)
           b11.place(x=1130, y=140)

           self.entrypid = ttk.Entry(self.root, font=("times new roman", 10, "bold"),show="*", width=18,textvariable=self.pid)
           self.entrypid.place(x=1020,y=473)
           btnpid = Button(self.root, bg="Red", height=1, width=10, text="show", fg="white",
                           font=("times new roman", 10, "bold"),command=self.FetchData)
           btnpid.place(x=1160, y=470)

           #=========================DetailFrameDetails=========================================================================
           ScrollX = ttk.Scrollbar(DetailFrame, orient=HORIZONTAL)
           ScrollY = ttk.Scrollbar(DetailFrame, orient=VERTICAL)
           ScrollX.pack(side=BOTTOM, fill=X)
           ScrollY.pack(side=RIGHT, fill=Y)

           self.rtable = ttk.Treeview(DetailFrame, column=("IDNO",
           "PatientID", "Date", "Accuracy", "Result", "Predictionfor"),
                                        xscrollcommand=ScrollX, yscrollcommand=ScrollY)



           ScrollX.config(command=self.rtable.xview)
           ScrollY.config(command=self.rtable.yview)

           self.rtable.heading("IDNO", text="IDNO")
           self.rtable.heading("PatientID", text="PatientID")
           self.rtable.heading("Date", text="Date")
           self.rtable.heading("Accuracy", text="Accuracy")
           self.rtable.heading("Result", text="Result")
           self.rtable.heading("Predictionfor", text="Predictionfor")

           self.rtable.column("IDNO", width=100)
           self.rtable.column("PatientID", width=100)
           self.rtable.column("Date", width=100)
           self.rtable.column("Accuracy", width=100)
           self.rtable.column("Result", width=100)
           self.rtable.column("Predictionfor", width=100)

           self.rtable.pack(fill=BOTH, expand=1)

           self.FetchData()

       def disease(self):
           self.new_window = Toplevel(self.root)
           self.app = Diseaseml(self.new_window)


       def widget2(self):
           self.new_window = Toplevel(self.root)
           self.app = Mlbot(self.new_window)

       def diabetes(self):
           self.new_window = Toplevel(self.root)
           self.app = Diabetes(self.new_window)

       def widget(self):
           self.new_window = Toplevel(self.root)
           self.app = Widget(self.new_window)

       def patho(self):
           self.new_window = Toplevel(self.root)
           self.app = Mlpatho(self.new_window)

       def bookapt(self):
           self.new_window = Toplevel(self.root)
           self.app = Appointment(self.new_window)

       def plot(self):
           self.new_window = Toplevel(self.root)
           self.app = Plot(self.new_window)

       def docfind(self):
           self.new_window = Toplevel(self.root)
           self.app = Docfind(self.new_window)

       def billfind(self):
           self.new_window = Toplevel(self.root)
           self.app = Billfind(self.new_window)

       def drugbot(self):
           self.new_window = Toplevel(self.root)
           self.app = Drugbot(self.new_window)

       def reg(self):
           self.new_window = Toplevel(self.root)
           self.app = Reg(self.new_window)

       def FetchData(self):

           conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                        database="pharma")

           mycursor = conn.cursor()

           mycursor.execute("SELECT * FROM reporttable WHERE PatientID=%s",(self.pid.get(),))

           row = mycursor.fetchall()
           if len(row) != 0:
               self.rtable.delete(*self.rtable.get_children())
               for i in row:
                   self.rtable.insert("", END, values=i)
               conn.commit()
           conn.close()




if __name__=="__main__":
    root=Tk()
    obj=Front(root)
    root.mainloop()