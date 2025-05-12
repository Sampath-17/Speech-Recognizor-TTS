import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Please Say Somthing")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:"+ text)
    engine.say("You said "+text)
    engine.runAndWait()
except sr.UnknownValueError:
    text = "Sorry, I did not understand that."
    print(text)
    engine.say(text)
    engine.runAndWait()
