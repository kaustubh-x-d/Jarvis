import speech_recognition as sr
import pyttsx3
import pyaudio
import pocketsphinx
import webbrowser
import musiclib
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https;//google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https;//youtube.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com/")
    elif "play" in c.lower():
        song=c.lower.split(" ")[1]
        webbrowser.open(musiclib.music[song])
r=sr.Recognizer()
if __name__=="__main__": 

    speak("Intializing Jarvis")


    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    while True:
        

        try:        
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=4,phrase_time_limit=5)
            c= r.recognize_google(audio)
            if c.lower()=="jarvis":
                speak("Yes,How may I help you")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source,timeout=4,phrase_time_limit=5)
                    command=r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("hello")
# yoih'n            
            
        
        
