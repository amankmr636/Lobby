from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):

    engine.say(text)
    engine.runAndWait()


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Go Ahead I am Listening")
        audio=r.listen(source)
    try:
        speak("Recognizing")
        query=r.recognize_google(audio,language='en-in')

    except Exception as e:
        speak("Sorry!!Say that again please")
        query=''

    return query


class Widget:
    def __init__(self, root):
        self.root= root
        self.root.title("REXHA")
        self.root.geometry('980x620')

        self.img=Image.open("C:\logorex.jpg")
        self.img=self.img.resize((500,700))
        self.img2=ImageTk.PhotoImage(self.img)
        self.panel=Label(root,image=self.img2)
        self.panel.pack(side='right',fill='both',expand='no')

        self.userText=StringVar()
        self.compText=StringVar()

        self.userText.set("RexHa Initializing")
        self.compText.set("Hi!! I am RexHa\nHow can I help you?")

        self.userFrame=LabelFrame(root,text="User",font=('Black ops one',10,"italic"),bd=3)
        self.userFrame.pack(fill="both",expand="yes")

        self.left=Message(self.userFrame,textvariable=self.userText,bg="black",fg="white")
        self.left.config(font=("Century Gothic",15,"bold"))
        self.left.pack(side='top',fill="both",expand="yes")

        self.compFrame=LabelFrame(root,text="RexHa",font=('Black ops one',10,"italic"))
        self.compFrame.pack(fill="both",expand="yes")

        self.left2=Message(self.compFrame,textvariable=self.compText,bg="black",fg="white")
        self.left2.config(font=("Century Gothic",15,"bold"))
        self.left2.pack(side='top',fill="both",expand="yes")


        self.btn=Button(root,text="Run Rexha",font=('Railways',10,"bold"),bg="yellow",fg="Black",command=self.clicked).pack(fill='x',expand='no')
        self.btn2=Button(root,text="Close",font=('Railways',10,"bold"),bg="#4B4B4B",fg="white",command=self.root.destroy).pack(fill='x',expand='no')



    def clicked(self):
        self.compText.set("Working")
        query=takecommand().lower()
        self.compText.set('Working it out')


        if 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'social' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'mail' in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")


        elif 'master' in query:
            speak("showing master on youtube")
            webbrowser.open("https://www.youtube.com/results?search_query=aman+kumar+nimcet")



        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            self.compText.set("According to wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.compText.set(results)
            speak("According to wikipedia")
            speak(results)



if __name__ == '__main__':
    root=Tk()
    widget = Widget(root)
    root.mainloop()

