import speech_recognition as sr
import RPi.GPIO as GPIO

mot_1 = 16              # PWM pin connected to LED
mot_2 = 18
en_1 = 24
led_1 = 26

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(mot_1,GPIO.OUT)
GPIO.setup(mot_2,GPIO.OUT)
GPIO.setup(en_1,GPIO.OUT)
GPIO.setup(led_1,GPIO.OUT)


# obtain audio from the microphone
while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
        print("Say something!")
        audio = r.listen(source)
        print("Audio taken.")
        a=r.recognize_google(audio)
        print("Audio fetched.")
        a=a.split()
        a=a[0]
        print(r.recognize_google(audio))
        if a=="on":
            GPIO.output(led_1,True)
        if a=="bright":
            GPIO.output(led_1,False)
        if a=="hot":
            GPIO.output(mot_1,True)
            GPIO.output(mot_2,False)
            GPIO.output(en_1,True)
        if a=="cold":
            GPIO.output(mot_1,False)
            GPIO.output(mot_2,False)
            GPIO.output(en_1,False)
