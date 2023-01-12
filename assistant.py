import speech_recognition as sr

from openapi_adapter.open_api import open_api_search

recognition = sr.Recognizer()

print("Python Assistant")

microphone_list = sr.Microphone.list_microphone_names()

print(microphone_list)

microphone_index = microphone_list.index("default") \
    if "default" in microphone_list else microphone_list[0]


def main():
    with sr.Microphone(device_index=microphone_index) as source:
        recognition.adjust_for_ambient_noise(source=source)

        print("We're listening u!")

        audio = recognition.listen(source)

        try:
            print(f"Audio object: <{audio}>")

            text = recognition.recognize_google(audio)

            answer = open_api_search(text)

            print(answer)

        except:
            print("I can't understand...")


if __name__ == "__main__":
    main()

# sudo apt install portaudio19-dev
# sudo apt-get install python3-pyaudio
