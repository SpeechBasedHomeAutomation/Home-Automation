  
import os
import pickle
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time
import pyaudio
import wave
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
import RPi.GPIO as GPIO
"""
#path to training data
source   = "development_set/"   
modelpath = "speaker_models/"
test_file = "development_set_test.txt"        
file_paths = open(test_file,'r')

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
"""
fan = 16              # PWM pin connected to LED
light1 = 18
light2 = 24

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(fan,GPIO.OUT)
GPIO.setup(light1,GPIO.OUT)
GPIO.setup(light2,GPIO.OUT)


#path to training data
source1  = "record/"   

#path where training speakers will be saved
modelpath = "Speakers_models/"

gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
              in gmm_files]

error = 0
total_sample = 0.0

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100#48000 #44100
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "pyaudio_test22.wav"
#WAVE_OUTPUT_FILENAME = "aasish1.wav"

take=input("Do you want to Test a Single Audio: Press '1' or The complete Test Audio Sample: Press '0' ?")
#take = int(input().strip())
take=int(take)
if take == 1:
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print ("say something")

    frames = []
    for i in range(0, int( RATE / CHUNK * RECORD_SECONDS ) ):
        data = stream.read( CHUNK, exception_on_overflow = False )
        frames.append(data)
    print ("finished recording...")
    #stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    path=WAVE_OUTPUT_FILENAME
    #path = raw_input().strip()   
    print("Testing Audio : ", path)
    sr1,audio = read(path)
    vector   = extract_features(audio,sr1)
    #vector=np.ndarray.flatten(vector)
   # vector=np.concatenate(vector,axis=0)
    
    log_likelihood = np.zeros(len(models))
    #print(len(models))
    
    for i in range(len(models)):
        gmm    = models[i]  #checking with each model one by one
        #gmm =np.ndarray.flatten(gmm)
        #gmm=np.ndarray.array(gmm)
        #print('i am in')
        scores = np.corrcoef(vector,gmm)
        #print(scores)
        log_likelihood[i] = scores.sum()
    #print(log_likelihood)
    if (log_likelihood[0]<3000):
        winner='medha'
    elif(log_likelihood[1]>30000):
        winner='gaurav'
    else:
        messagebox.showinfo("ALERT", ' voice not recognised')
        winner='None'
        
    
    ss=1    
    if(winner=='medha' or winner=='gaurav'):
        print ("\tdetected as - ", winner)
        # obtain audio from the microphone
        while True:
            mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
            #Sample rate is how often values are recorded 
            sample_rate = 48000
            #Chunk is like a buffer. It stores 2048 samples (bytes of data) 
            #here.  
            #it is advisable to use powers of 2 such as 1024 or 2048 
            chunk_size = 2048
            #Initialize the recognizer 
            r = sr.Recognizer() 
              
            #generate a list of all audio cards/microphones 
            mic_list = sr.Microphone.list_microphone_names() 
              
            #the following loop aims to set the device ID of the mic that 
            #we specifically want to use to avoid ambiguity. 
            for i, microphone_name in enumerate(mic_list): 
                if microphone_name == mic_name: 
                    device_id = i 
              
            #use the microphone as source for input. Here, we also specify  
            #which device ID to specifically look for incase the microphone  
            #is not working, an error will pop up saying "device_id undefined" 
            with sr.Microphone(device_index = 2, sample_rate = sample_rate,  
                                    chunk_size = chunk_size) as source: 
                #wait for a second to let the recognizer adjust the  
                #energy threshold based on the surrounding noise level 
                r.adjust_for_ambient_noise(source) 
                print ("Say Something")
                #listens for the user's input 
                audio = r.listen(source) 
                      
                
                text = r.recognize_google(audio) 
                print ("you said: " + text )
                  
                #error occurs when google could not understand what was said 
                  
                            #            r = sr.Recognizer()
            #            with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
            #                print("Say something!")
            #                audio = r.listen(source)
            #                print("Audio taken.")
            #                a=r.recognize_google(audio)
            #                print("Audio fetched.")
                
                a=text.split()
                a=a[0]
                print(r.recognize_google(audio))
                if a=="on":
                    GPIO.output(light1,True)  #GPIO.output(light1,True)
                if a=="of":
                    GPIO.output(light1,False) #GPIO.output(light1,False)
                if a=="hot":
                    GPIO.output(fan,True)  #GPIO.output(fan,True)
                    
                if a=="cold":
                    print('you said cold')
                    GPIO.output(fan,False) #GPIO.output(fan,False)
                    

            
        
 