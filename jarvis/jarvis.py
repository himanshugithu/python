import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("GOOD EVENING")
    
    speak("hello himanshu how can i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing......")
        querry = r.recognize_google(audio, language='en-in')
        print(f"user said,{querry}\n")

    except Exception as e:
        print(e)
        print("say again")
        return "none"
    return querry

if __name__=="__main__":
    wishme()
    while  1:
        querry = takecommand().lower()
        if 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open google' in querry:
            webbrowser.open('www.google.com')

        elif 'time' in querry:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"time is {strtime}")  
            print(strtime) 

        elif 'open notepad' in querry:
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad")