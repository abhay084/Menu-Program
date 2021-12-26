import pyttsx3

def speech(text):

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()




while True:
    text = str(input("input text here : "))

    if not text:
        print("exiting")
        break
    speech(text)
