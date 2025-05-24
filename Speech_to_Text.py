

import os
import datetime
import playsound
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import shutil

def speak(text):
    tts = gTTS(text=text,lang='en')
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)



def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening")

    

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
      
    try:
        said=r.recognize_google(audio)
        print(said) 
    except Exception as e:
        print("Exception :" + str(e))
        return "None"  
    return said


def sort_file():
    PDF = r'C:\Users\The Slacker\Documents\pdf_section'
    PICTURES = r'C:\Users\The Slacker\Pictures\download'
    PPT = r'C:\Users\The Slacker\Documents\ppt_section'
    DIRS = r'C:\Users\The Slacker\Downloads'

    for root, dirs, files in os.walk(DIRS):
        print("root :",root)
        print("subdirs :",dirs)
        print("file :",files)
        for file in files:
            if file.endswith('.pdf'):
                path = os.path.join(root,file)
                shutil.move(path, PDF)
            elif file.endswith(('.jpg','.png')):
                path = os.path.join(root,file)
                shutil.move(path, PICTURES)
            elif file.endswith('.pptx'):
                path = os.path.join(root,file)
                shutil.move(path, PPT)


    speak("sorted the download section")


if __name__ == "__main__":
    wish()
    if 1:
        query = get_audio().lower()

        if "hello" in query:
            speak("how are you...")
            query=query.replace("hello","")

        elif "open youtube" in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google...")
            webbrowser.open("google.com")

        elif "download section" in query:
            sort_file()

   
