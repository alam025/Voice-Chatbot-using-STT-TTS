<h1>🗣️ Voice Chatbot using Speech Recognition & Text-to-Speech</h1>

<p>A simple yet powerful voice-based chatbot built with Python. This project demonstrates the integration of Speech Recognition (STT) and Text-to-Speech (TTS) to create an interactive voice assistant that listens to your commands and responds naturally.</p>

<h2>✨ Features</h2>

🎙️ Listens to your voice input using the microphone

🧠 Processes speech with Google's Speech Recognition API

🔊 Responds back using synthesized voice with pyttsx3

🤖 Includes a basic conversational flow (e.g., greetings, questions)

❌ Supports voice-controlled exit by saying "bye" or "exit"

<h2>📦 Installation</h2>

<p>Make sure you have Python 3 installed. Then install the required packages:

# pip install SpeechRecognition pyttsx3 pyaudio

<h2>🧠 How It Works</h2>

STT (Speech-to-Text): Captures your voice and converts it to text using Google's API.

Command Processing: Responds to specific keywords and phrases.

TTS (Text-to-Speech): Speaks back the appropriate response using pyttsx3.

<h2>🚀 Getting Started</h2>

Run the chatbot with:
python your_script_name.py
Then just speak into your microphone. Try saying things like:

"What's the capital of India?"

"What is your name?"

"How are you?"

"Bye" or "Exit" to quit.

<h2>🧾 Example Code </h2>

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
        print("Could not request results")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        user_input = listen()
        if user_input is None:
            continue
        if "exit" in user_input or "bye" in user_input:
            speak("Goodbye! Have a nice day!")
            break
        elif "your name" in user_input:
            speak("My name is Chatbot. How can I assist you?")
        elif "how are you" in user_input:
            speak("I'm just a computer program, but I'm here to help. How can I assist you?")
        elif "capital of india" in user_input:
            speak("New Delhi")
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

chatbot()

<h2>🔧 Customization Ideas</h2>

Add more conversational rules or integrate with an NLP model like OpenAI GPT.

Log conversation history.

Add GUI support using Tkinter or PyQt.

Extend it to control smart home devices.

<h2>📄 License</h2>

This project is open source and available under the MIT License.

<h2>🙌 Acknowledgements</h2>

SpeechRecognition

pyttsx3

PyAudio

