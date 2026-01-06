import os
import json
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# --- CONFIGURATION ---
# Replace with your actual Gemini API Key
GEMINI_API_KEY = "AIzaSyDXs-hPinpozKUoDKyuhnc8zzl7VmkDUz0"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Index 0 is usually male, 1 is female

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# --- SYSTEM PROMPT ---
# This ensures Gemini behaves as a controller and a tutor
SYSTEM_INSTRUCTION = """
You are an advanced AI Home & Study Assistant. 
1. If the user asks to control lights (on, off, dim, color), respond ONLY with a JSON object: {"action": "light_control", "state": "on/off", "value": "optional_level"}.
2. If the user asks a study question, provide a concise, expert explanation.
3. If the user asks for both, prioritize the light command first in JSON, then the text.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_INSTRUCTION
)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception:
        return ""

def handle_home_automation(command_json):
    """
    This is where you would integrate with Philips Hue, Tuya, or Home Assistant.
    """
    action = command_json.get("state")
    if action == "on":
        print(">>> SYSTEM: Executing Light ON signal...")
        # Add your IoT SDK code here
    elif action == "off":
        print(">>> SYSTEM: Executing Light OFF signal...")

def run_assistant():
    speak("System online. How can I help you with your studies or home today?")
    
    while True:
        user_input = listen()
        
        if not user_input:
            continue
            
        if "exit" in user_input.lower() or "stop" in user_input.lower():
            speak("Goodbye.")
            break

        # Generate response from Gemini
        response = model.generate_content(user_input)
        response_text = response.text.strip()

        # Check if the response is a JSON command for lights
        if response_text.startswith("{") and "light_control" in response_text:
            try:
                data = json.loads(response_text)
                handle_home_automation(data)
                speak(f"Turning the lights {data['state']}.")
            except json.JSONDecodeError:
                speak(response_text)
        else:
            # It's a study/guiding response
            speak(response_text)

if __name__ == "__main__":
    run_assistant()
