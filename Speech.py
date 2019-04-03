import speech_recognition as sr

r = sr.Recognizer()
mic= sr.Microphone()
word=["turn on light","turn off light","Turn on fan","turn off fan"]

sr.Microphone.list_microphone_names()
print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
    print("Speak :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
    if text in word:
        print("valid command")
    else:
        print("invalid Command")
