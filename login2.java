from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk


class Login2:
    def __init__(self, root , root2):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1599x1000+0+0")

        self.root2=root2
        self.root2.title("Register")
        self.root2.configure(bg="sky blue")
        self.root2.geometry("600x220")
        # ------------------------image--------------------------
        img1 = Image.open("C:\login1.jpg")
        img1 = img1.resize((1320, 920))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelphoto = Label(self.root, image=self.photoimg1, borderwidth=0, )
        labelphoto.place(x=0, y=0, relwidth=1, relheight=1)
        # -------------------Frame-------------------------------------

        framelogin = Frame(self.root, bg="white", height=340, width=500).place(x=660, y=150)

        # ------------------------title--------------------------------
        title = Label(framelogin, text="PhaReXha", font=("Impact", 35, "bold"), fg="powder blue", width=15,
                      bg="white").place(x=740, y=150)
        desc = Label(framelogin, text="Login", font=("Goudy old style", 35, "bold"), fg="#d25d17", bg="white",
                     width=15).place(x=700, y=200)
        username = Label(framelogin, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                         width=15).place(x=670, y=290)
        self.text = Entry(framelogin, font=("times new roman", 30), bg="lightgray")
        self.text.place(x=850, y=290, width=300, height=35)

        password = Label(framelogin, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                         width=15).place(x=670, y=350)
        self.pss = Entry(framelogin, font=("times new roman", 30), show="*", bg="lightgray")
        self.pss.place(x=850, y=350, width=300, height=35)

        forget = Button(framelogin, text="Forget Password", bg="white", cursor="hand2", border=0, fg="#d25d17",
                        font=("times new roman", 12)).place(x=850, y=400)
        loginbtn = Button(framelogin, command=self.loginfun, text="Login", cursor="hand2", fg="white", bg="#d25d17",
                          font=("times new roman", 20)).place(x=1000, y=400, width=130, height=35)

        register = Button(self.root, command=self.registerfun, text="Register", cursor="hand2", fg="white",
                          bg="#d25d17",
                          font=("times new roman", 20)).place(x=900, y=500, width=130, height=35)
        reguser = Label(root2, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                        width=15).place(x=10, y=10)
        regtext = Entry(root2, font=("times new roman", 30), bg="lightgray")
        regtext.place(x=200, y=10, width=300, height=35)

        regpass = Label(root2, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white",
                        width=15).place(x=10, y=60)
        regpss = Entry(root2, font=("times new roman", 30), show="*", bg="lightgray")
        regpss.place(x=200, y=60, width=300, height=35)

        regbtn = Button(root2, text="Sign in", command=self.check, cursor="hand2", fg="white", bg="#d25d17",
                        font=("times new roman", 20)).place(x=170, y=120)
    def registerfun(self):
       pass




    def check(self):
        if (self.regtext.get() != "") or (self.regpass.get() != ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root2)


    def loginfun(self):
        if (self.text.get() == "") or (self.pss.get() == ""):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)

        elif (self.text.get() != "user") or (self.pss.get() != "pharmacy"):
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)

        else:
            messagebox.showinfo("Welcome", f"Welcome {self.text.get()}", parent=self.root)


root = Tk()
root2=Tk()
obj = Login(root,root2)
root.mainloop()
root2.mainloop()

