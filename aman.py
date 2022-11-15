from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



class Widget2:
    def __init__(self):
        root=Tk()
        root.title("REXHA")
        root.geometry('980x620')

        img=Image.open("C:\logo1.jpg")
        img=img.resize((500,700))
        img2=ImageTk.PhotoImage(img)
        panel=Label(root,image=img2)
        panel.pack(side='right',fill='both',expand='no')

        self.userText=StringVar()
        self.compText=StringVar()

        self.userText.set("RexHa Initializing")
        self.compText.set("Hi!! I am RexHa\nHow can I help you?")

        userFrame=LabelFrame(root,text="User",font=('Black ops one',10,"italic"),bd=3)
        userFrame.pack(fill="both",expand="yes")

        left=Message(userFrame,textvariable=self.userText,bg="black",fg="white")
        left.config(font=("Century Gothic",15,"bold"))
        left.pack(side='top',fill="both",expand="yes")

        compFrame=LabelFrame(root,text="RexHa",font=('Black ops one',10,"italic"))
        compFrame.pack(fill="both",expand="yes")


        left2=Message(compFrame,textvariable=self.compText,bg="black",fg="white")
        left2.config(font=("Century Gothic",15,"bold"))
        left2.pack(side='top',fill="both",expand="yes")



        btn=Button(root,text="Run Rexha",font=('Railways',10,"bold"),bg="yellow",fg="Black",command=self.clicked).pack(fill='x',expand='no')
        btn2=Button(root,text="Close",font=('Railways',10,"bold"),bg="#4B4B4B",fg="white",command=root.destroy).pack(fill='x',expand='no')


        root.mainloop()


    def clicked(self):
        self.compText.set("Working")
        query=self.takecommand().lower()
        self.compText.set('Working it out')
        self.userText.set(query)


        if 'youtube' in query:
            self.speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'social' in query:
            self.speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'mail' in query:
            self.speak("opening gmail")
            webbrowser.open("gmail.com")

        elif 'thank you' in query:
            self.speak("pleasure is all mine")

        elif 'wikipedia' in query:
            self.speak('Searching Wikipedia...')
            self.compText.set("According to wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            self.compText.set(results)
            self.speak("According to wikipedia")
            self.speak(results)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Go Ahead I am Listening")
            audio = r.listen(source)
        try:
            self.speak("Recognizing")
            query = r.recognize_google(audio, language='en-in')

        except Exception as e:
            self.speak("Sorry!!Say that again please")
            query = None
        return query


if __name__ == '__main__':

    widget = Widget2()


