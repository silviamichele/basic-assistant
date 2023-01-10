import pyttsx3

engine = pyttsx3.init("espeak")

voices = engine.getProperty('voices')

assistant_voice = voices[58]

engine.setProperty('voice', assistant_voice.id)

