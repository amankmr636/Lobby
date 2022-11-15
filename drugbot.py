import csv
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import pandas as pd
import mysql.connector

class Drugbot:
    def __init__(self,root):
        self.root=root
        self.root.title("Chatbot")
        self.root.geometry("730x620+0+0")

        self.var=StringVar()
        self.var2=StringVar()
        self.drugrec = StringVar()
        self.drugavail = StringVar()

        self.var.set("Drug Recom")
        self.var2.set("Drug Avail")

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open("C:\logo2.jpg")
        img_chat=img_chat.resize((150,70))

        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,width=730,compound=LEFT,
                          image=self.photoimg,text="DrugBoT",font=("arial",30,"bold"),padx=10,fg="green",bg="white")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),
                        yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=1030)
        btn_frame.pack(fill=X)

        label=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),fg="green",bg="white")
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=ttk.Entry(btn_frame,width=10,font=("times new roman",17,"bold"),textvariable=self.var)
        self.entry.grid(row=0,column=1,padx=5,sticky=W)


        self.entry2=ttk.Entry(btn_frame,width=10,font=("times new roman",17,"bold"),textvariable=self.var2)
        self.entry2.grid(row=0,column=2,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=("arial",13,"bold"),width=8,bg="red",fg="white")
        self.send.grid(row=0,column=3,padx=5,sticky=W)

        self.send2=Button(btn_frame,text="Send",command=self.send2,font=("arial",13,"bold"),width=8,bg="blue",fg="white")
        self.send2.grid(row=0,column=4,padx=5,sticky=W)

        self.clear = Button(btn_frame, text="Clear Data",command=self.cler ,font=("arial", 13, "bold"), width=8,fg="white", bg="green")
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg=''
        self.label1 = Label(btn_frame, text=self.msg, font=("arial", 14, "bold"), fg="green", bg="white")
        self.label1.grid(row=1, column=1, padx=5, sticky=W)

    #==========================Function Declaration=========================

    def send(self):

        data = csv.reader(open("final.csv",'r'))

        send='\t\t\t\t\t'+'You: '+ self.entry.get()
        self.text.insert(END,'\n'+send)

        if (self.entry.get()==''):
            self.msg="Please Enter Some Input"
            self.label1.config(text=self.msg,fg='red')

        else:
            data = csv.reader(open("final.csv", 'r'))
            self.msg=''
            self.label1.config(text=self.msg,fg='red')

            self.drugrec=self.entry.get()

            self.text.insert(END, '\n\n' + 'Drug Recommended:'+"\n"+"-----------------------------------------------------"+"\n\n")

            for i in data:
                if self.drugrec==i[1]:
                    self.text.insert(END,'\n\n'+i[2])


        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'BoT: Hello User')

        elif (self.entry.get() == 'hi'):
            self.text.insert(END,'\n\n' + 'BoT: Hello User'+"\n")

        elif "rexha" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Click on the Voice Assistant logo at the top of the pharmacy page'+"\n")

        elif (self.entry.get() == 'who are you'):
            self.text.insert(END, '\n\n' + 'BoT: I am MistrBoT and I can help you understanding this app'+"\n")

        elif "covid" in self.entry.get():
            self.text.insert(END,'\n\n'+'BoT: Click on the Fight Covid Picture on the pharmacy'+'\n'+'\tpage to get all the info regarding covid'+"\n")


        self.entry.delete(0,END)

    def send2(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aman9174245164@",
                                       database="pharma")
        mycursor = conn.cursor()

        mycursor.execute("SELECT Name,Price,Uses FROM medtable WHERE Formula=%s", (self.entry2.get(),))
        row3 = mycursor.fetchall()
        if len(row3) != 0:
            self.text.delete("1.0",END)
            self.text.insert(END,"Drug Availability"+"\n\n")

            self.text.insert(END, "Drug" +"\t"+ "Price"+"\t"+"Use"+"\t"+"\n")
            self.text.insert(END, "-------------------------------------------" + "\n\n")

            for i in row3:
                self.text.insert(END, i)
                self.text.insert(END,"\n")
            conn.commit()
        conn.close()

    def cler(self):
        self.text.delete('0.0',END)



if __name__=="__main__":

    root=Tk()
    obj=Drugbot(root)
    root.mainloop()
