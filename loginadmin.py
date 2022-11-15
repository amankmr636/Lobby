from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from main import PharmacyManagementSystem
from doctor import Doctor
class Loginadm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1599x1000+0+0")


        # ------------------------image-----------------------------------
        img1 = Image.open("C:\loginadm.jpg")
        img1 = img1.resize((1320, 920))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelphoto = Label(self.root, image=self.photoimg1, borderwidth=0, )
        labelphoto.place(x=0, y=0,relwidth=1, relheight=1)
        # -------------------Frame-------------------------------------

        framelogin = Frame(self.root, bg="white", height=340, width=500).place(x=660, y=150)

        # ------------------------title--------------------------------------------------------------
        title = Label(framelogin, text="Employee Mgmt", font=("Impact", 35, "bold"), fg="powder blue", width=15,
                      bg="white").place(x=740, y=150)
        desc = Label(framelogin, text="Admin Login", font=("Goudy old style", 35, "bold"), fg="#d25d17", bg="white",
                     width=15).place(x=700, y=200)
        username = Label(framelogin, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                         width=15).place(x=670, y=290)
        self.text = Entry(framelogin, font=("times new roman", 30), bg="lightgray")
        self.text.place(x=850, y=290, width=300, height=35)

        password = Label(framelogin, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                         width=15).place(x=670, y=350)
        self.pss = Entry(framelogin, font=("times new roman", 30), show="*", bg="lightgray")
        self.pss.place(x=850, y=350, width=300, height=35)

        loginbtn = Button(framelogin, command=self.loginfun, text="Login", cursor="hand2", fg="white", bg="#d25d17",
                          font=("times new roman", 20)).place(x=1000, y=400, width=130, height=35)





    def loginfun(self):

        with open("credential2.txt","r") as f:
            info = f.readlines()
            for e in info:
                u,p=e.split("@")

                if (self.text.get()==u.strip()) and (self.pss.get()== p.strip()):

                    i=1

                    break
                else:
                        i=0

        if i==1:
            messagebox.showinfo("Welcome", f"Welcome {self.text.get()}", parent=self.root)
            self.doctor()
        else:
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)


    def doctor(self):
        self.new_window = Toplevel(self.root)
        self.app = Doctor(self.new_window)



root = Tk()
obj = Loginadm(root)
root.mainloop()


