import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

wake_up_keyword = "jupiter"  # Adjust the wake-up keyword as needed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
    speak("Hello Himanshu, how can I help you")

def takecommand():
    r = sr.Recognizer()

    # Listen for the wake-up keyword
    while True:
        with sr.Microphone() as source:
            print("Listening for wake-up keyword....")
            r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            audio = r.listen(source)

        try:
            print("Recognizing......")
            keyword = r.recognize_google(audio, language='en-in').lower()
            if wake_up_keyword in keyword:
                speak("I'm listening. How can I assist you?")
                break
        except sr.UnknownValueError:
            pass

    # Listen for the user command
    while True:
        with sr.Microphone() as source:
            print("Listening for user command....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing......")
            query = r.recognize_google(audio, language='en-in').lower()
            print(f"User said, {query}\n")
            return query
        except Exception as e:
            print(e)
            print("Say that again")

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Time is {strtime}")
            print(strtime)

        elif 'open notepad' in query:
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad")
