import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    speak("I am Jarvis Sir......How can I help you")        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognition.......")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) 

        print("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('multra050@gmail.com','Sig@2000')
    server.sendmail('multra050@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe() 
    #while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\sasis\\Music\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codepath = "C:\\Users\\sasis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to bug' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "multra050@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except  Exception  as e:
                print(e)
                speak("Sorry friend I can't able to send the mail")
