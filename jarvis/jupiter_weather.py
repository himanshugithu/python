import pyttsx3
import speech_recognition as sr
import requests
import time
target_ip = "192.168.0.102"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

wake_up_keyword = "jupiter"  # Adjust the wake-up keyword as needed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def weather():

    url = f"http://{target_ip}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            print(f"Received data: {data}")
            speak(f"{data} degree celcius")
        else:
            print(f"Error in HTTP GET request. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}")
    time.sleep(1)    

if __name__ == "__main__":

    while True:
        query = takecommand()
        if 'weather' in query:
            weather()
            
