import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
   engine.say(text)
   engine.runAndWait()

def processcommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing jarvis")
    while True:
    #Listan for the wake word "jarvis"
    #obtain audio from the microphone
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listining...")
                audio = r.listen(source,timeout = 2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if ( word.lower() == "jarvis" or word.lower() == "nannu"):
                speak("hasaa")
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source,timeout = 2,phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    if "stop jarvis" in command.lower():
                        break
                    processcommand(command)
        except Exception as e:
            print ("Error; {0}".format(e))
