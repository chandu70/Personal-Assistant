import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import webbrowser
import pywhatkit as kit
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
#text to speech
# print(type(str(datetime.datetime.now())))
# print(datetime.datetime.now().time())
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#to convert voice to speech
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.............")
        r.pause_threshold=1
        audio=r.listen(source,timeout=3,phrase_time_limit=5)
    try:
        print("Recognizing...............")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query
#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<12):
        speak("good morning")
    elif(hour>12 and hour<18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Jarvis ma'am please tell me how can i help you")


if __name__=="__main__":
    wish()
    #while True:
    if 1:
        query=takecommand().lower()
        #logic buiding for tasks
        if "open notepad" in query:
            npath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if(k==27):
                    break
            cap.release()
            cv2.destroyAllWindows()
        #elif "play music" in query:
        elif "ip address " in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is{ip}")
        elif "wikipedia" in query:
           speak("searching wikipedia")
           query=query.replace("wikipedia"," ")
           results=wikipedia.summary(query,sentences=2)
           speak("according to wikipedia")
           speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("Ma'am what do you want to search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")
        # elif "send message" in query:
        #     num=takecommand()
        #     msg=takecommand().lower()
        #     kit.sendwhatmsg(f"+91{num}",msg,2,24)
        elif "play song on youtube" in query:
            songname=takecommand().lower()
            kit.playonyt(songname)
        elif "open medium" in query:
            webbrowser.open("www.medium.com")
        elif "time" in query:
            #print(type(str(datetime.datetime.now())))
            #print(datetime.datetime.now())
            speak(str(datetime.datetime.now()))
        # elif "open whatsapp" in query:
        #     wpath = "C:\Users\CHANDRIKA AMALAKANTI\AppData\Local\WhatsApp"
        #     os.startfile(wpath)

        else:
            speak("ma'am do you have any other work")
            dec=takecommand().lower()
            if(dec == "no"):
                speak("ma'am thanks for using me ,have a good day")
                #break












