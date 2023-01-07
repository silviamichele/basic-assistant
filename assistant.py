# Import the required module for text
# to speech conversion
import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init("espeak")

voices = engine.getProperty('voices')

assistant_voice = voices[58]

engine.setProperty('voice', assistant_voice.id)

# say method on the engine that passing input text to be spoken
engine.say('Olá, como posso te ajudar?')

# run and wait method, it processes the voice commands.
engine.runAndWait()
