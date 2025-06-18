#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition pyttsx3 pyaudio


# # Combining STT & TTS for a Voice Chatbot

# In[38]:


import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... speak now")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.RequestError:
        print("could not request results")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        user_input = listen()
        if "exit" in user_input or "bye" in user_input:
            speak("Goodbye! Have a nice day!")
            break
        elif "your name" in user_input:
            speak("My name is Chatbot. How can I assist you?")
        elif "How are you?" in user_input:
            speak("I'm just a computer program, but I'm here to help. How can I assist you?")
        elif "capital of India" in user_input:
            speak("New Delhi")
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

chatbot()


# In[ ]:





# In[ ]:





# In[ ]:




