from tkinter import*
from PIL import Image,ImageTk
from patient import Hospital
from doctor import Doctor
from chatbot import Chatbot
from bill import Bill
from voice import Widget
from main import PharmacyManagementSystem
from appointment import Appointment
from bloodreport import bloodreport



class Front:
       def __init__(self,root):
           self.root=root
           self.root.title("PhaREXHA")
           self.root.geometry("1550x800+0+0")
           lbltitle = Label(self.root, text="PhaREXHA", bd=15, relief=RIDGE,
                            bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
           lbltitle.pack(side=TOP, fill=X)

           img1 = Image.open("C:\logo11.jpg")
           img1 = img1.resize((80, 80))

           self.photoimg1 = ImageTk.PhotoImage(img1)

           img2 = Image.open("C:\logovoice.jpg")
           img2 = img2.resize((80, 80))

           self.photoimg2 = ImageTk.PhotoImage(img2)

           img3 = Image.open("C:\logo.png")
           img3 = img3.resize((80, 80))

           self.photoimg3 = ImageTk.PhotoImage(img3)

           b1 = Button(self.root, image=self.photoimg1, borderwidth=0, command=self.chatbot)
           b1.place(x=100, y=20)
           b2 = Button(self.root, image=self.photoimg2, borderwidth=0, command=self.voice)
           b2.place(x=240, y=20)
           b3 = Button(self.root, image=self.photoimg3, borderwidth=0,command=self.pharma)
           b3.place(x=370, y=20)

           img4a = Image.open("C:\patient.jpg")
           img4a = img4a.resize((80, 80))

           self.photoimg4a = ImageTk.PhotoImage(img4a)

           img5 = Image.open("C:\doctor.jpg")
           img5 = img5.resize((80, 80))

           self.photoimg5 = ImageTk.PhotoImage(img5)

           img6 = Image.open("C:\Abill.jfif")
           img6 = img6.resize((80, 80))

           self.photoimg6 = ImageTk.PhotoImage(img6)

           b4 = Button(self.root, image=self.photoimg4a, borderwidth=0, command=self.patient)
           b4.place(x=900, y=20)
           b5 = Button(self.root, image=self.photoimg5, borderwidth=0, command=self.doctor)
           b5.place(x=1040, y=20)
           b6 = Button(self.root, image=self.photoimg6, borderwidth=0, command=self.bill)
           b6.place(x=1170, y=20)

           img7 = Image.open("C:\pharma.jpg")
           img7 = img7.resize((1280, 580))

           self.photoimg7 = ImageTk.PhotoImage(img7)

           img8 = Image.open("C:\Appoint.png")
           img8 = img8.resize((80, 80))

           self.photoimg8 = ImageTk.PhotoImage(img8)

           img9 = Image.open("C:\Blood.jpg")
           img9 = img9.resize((80, 80))

           self.photoimg9 = ImageTk.PhotoImage(img9)


           lbltitle2 = Label(self.root, bd=15, relief=RIDGE,
                            bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), image=self.photoimg7,padx=2, pady=4,height=500)
           lbltitle2.pack(side=TOP, fill=X)

           b8 = Button(self.root, image=self.photoimg8, borderwidth=0, command=self.appoint)
           b8.place(x=100, y=140)
           b9 = Button(self.root, image=self.photoimg9, borderwidth=0, command=self.blood)
           b9.place(x=240, y=140)

           img10 = Image.open("C:\logo2.png")
           img10 = img10.resize((80, 80))

           self.photoimg10 = ImageTk.PhotoImage(img10)

           img11 = Image.open("C:\diag.jpg")
           img11 = img11.resize((80, 80))

           self.photoimg11 = ImageTk.PhotoImage(img11)

           img12 = Image.open("C:\disease.jpg")
           img12 = img12.resize((80, 80))

           self.photoimg12 = ImageTk.PhotoImage(img12)

           b10 = Button(self.root, image=self.photoimg10, borderwidth=0, command=self.chatbotm)
           b10.place(x=900, y=140)
           b11 = Button(self.root, image=self.photoimg11, borderwidth=0, command=self.diag)
           b11.place(x=1040, y=140)
           b12 = Button(self.root, image=self.photoimg12, borderwidth=0, command=self.disease)
           b12.place(x=1170, y=140)



       def chatbot(self):
            self.new_window=Toplevel(self.root)
            self.app=Chatbot(self.new_window)

       def appoint(self):
            self.new_window=Toplevel(self.root)
            self.app=Appointment(self.new_window)

       def blood(self):
            self.new_window=Toplevel(self.root)
            self.app=bloodreport(self.new_window)



       def patient(self):
            self.new_window=Toplevel(self.root)
            self.app=Hospital(self.new_window)

       def doctor(self):
            self.new_window=Toplevel(self.root)
            self.app=Doctor(self.new_window)

       def voice(self):
           self.new_window = Toplevel(self.root)
           self.app = Widget(self.new_window)

       def pharma(self):
           self.new_window = Toplevel(self.root)
           self.app = PharmacyManagementSystem(self.new_window)

       def bill(self):
           self.new_window = Toplevel(self.root)
           self.app = Bill(self.new_window)

       def chatbotm(self):
           self.new_window = Toplevel(self.root)
           self.app = chatbotml(self.new_window)

       def diag(self):
           self.new_window = Toplevel(self.root)
           self.app = mlpatho(self.new_window)

       def disease(self):
           self.new_window = Toplevel(self.root)
           self.app = diseaseml(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Front(root)
    root.mainloop()