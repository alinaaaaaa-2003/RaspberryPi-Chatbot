# -*- coding: utf-8 -*-
"""

@author: alina
"""
import speech_recognition as sr
import pyttsx3
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Initialize recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Load FLAN-T5 base model (better answers)
model_name = "google/flan-t5-base"
print("Loading FLAN-T5 base model... (first run may take a few minutes)")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
qa_bot = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)  # CPU

def listen_and_respond():
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... (say 'stop' to exit)")
        audio = r.listen(source, timeout=3, phrase_time_limit=10)  # limit listening time

    try:
        question = r.recognize_google(audio).lower().strip()
        if not question:
            return True

        print("You asked:", question)

        # Stop command
        if question in ["stop", "exit", "quit"]:
            print("Exiting...")
            engine.say("Goodbye!")
            engine.runAndWait()
            return False

        # Generate answer (full sentences, no repetition)
        response = qa_bot(question, max_new_tokens=40, do_sample=False)[0]['generated_text']
        print("Answer:", response)

        # Speak the answer
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Could not understand audio.")
        engine.say("I didn't catch that.")
        engine.runAndWait()
    except sr.RequestError as e:
        print("Speech recognition service error:", e)
        engine.say("Service error.")
        engine.runAndWait()
    except Exception as e:
        print("Error:", e)

    return True

if __name__ == "__main__":
    running = True
    while running:
        running = listen_and_respond()
