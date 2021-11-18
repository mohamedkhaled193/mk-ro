import os
import glob
import sys
import playsound
import speech_recognition as sr
import webbrowser

def listen_user():
  rec = sr.Recognizer()
  
  with sr.Microphone() as source:
    print("Mr Robot Is Listening....")
    audio = rec.listen(source , pharse_time_limit=5)
  try:
    text = rec.recognize_google(audio , language='ar-EG')
    return text
  except:
    print("Sorry I had a Problem")
    return 0
def talk(text , file):
    tts = gTTS(text=text , lang="ar")
    filename = "%s.mp3"%file
    tts.save(filename)
    playsound.playsound(filename)
def contact():
    text_returned = listen_user()
    print(text_returned)
