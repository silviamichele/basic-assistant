from speaker.engine import engine


def speak(message: str):
    engine.say(message)

    engine.runAndWait()
