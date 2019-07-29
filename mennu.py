from tkinter import *
import tkinter
from tkinter import messagebox
import time
import pyaudio
import wave
import RPi.GPIO as GPIO
import csv
import pyaudio
import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn import mixture
import warnings
import os
from featureextraction import extract_features

fan = 16              # PWM pin connected to LED
light1 = 18
light2 = 24
global z
z=1

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(fan,GPIO.OUT)
GPIO.setup(light1,GPIO.OUT)
GPIO.setup(light2,GPIO.OUT)



top = tkinter.Tk()
top.geometry('2000x1000')
CheckVar1 = IntVar()
CheckVar2 = IntVar()
def user():
    global z
    top = tkinter.Tk()
    top.geometry('2000x1000')
    print(z)
    def login(a,b):
        global z
        c=a+b
        username=c
        print(username)
        with open('database.txt', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
               # print(row)
                row=row[0]
                if row ==username:
                    print("go away")
                    z=0
                    print(z)
                    break
                
                
        if z==0:
            top = tkinter.Tk()
            top.geometry('2000x1000')
            def fan_on():
                GPIO.output(fan,True)
            def fan_off():
                GPIO.output(fan,False)
            def light1_on():
                GPIO.output(light1,True)
            def light1_off():
                GPIO.output(light1,False)
            def light2_on():
                GPIO.output(light2,True)
            def light2_off():
                GPIO.output(light2,False)
            L1 = Label(top, text="Fan",fg="#97c7f1",bg="#5c6268",font=('Times',22,"bold"))
            L1.pack( side = LEFT)
            L1.place(x=200,y=100)
            
            L1 = Label(top, text="light1",fg="#97c7f1",bg="#5c6268",font=('Times',22,"bold"))
            L1.pack( side = LEFT)
            L1.place(x=400,y=100)
            
            L1 = Label(top, text="light2",fg="#97c7f1",bg="#5c6268",font=('Times',22,"bold"))
            L1.pack( side = LEFT)
            L1.place(x=600,y=100)
            
            B_1=Button(top,text="ON",command=fan_on,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=150,y=200)
            
            B_1=Button(top,text="OFF",command=fan_off,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=250,y=200)
            
            B_1=Button(top,text="ON",command=light1_on,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=350,y=200)
            
            B_1=Button(top,text="OFF",command=light1_off,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=450,y=200)
            
            B_1=Button(top,text="ON",command=light2_on,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=550,y=200)
            
            B_1=Button(top,text="OFF",command=light2_off,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=680,y=200)
        else:
            tkinter.messagebox.showinfo("ALERT", "invalid username or password")
            
                
    B_1=Button(top,text="LOGIN",command=lambda:login(E1.get(),E2.get()))
    B_1.place(x=615,y=500)
    
    L1 = Label(top, text="Welcome User!!",fg="black",font=('Times',32,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=500,y=50)

    L1 = Label(top, text="Username",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=380,y=290)

    L1 = Label(top, text=":",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=510,y=290)

    E1 = Entry(top, bd =2)
    E1.pack(side = RIGHT)
    E1.place(x=580,y=300)

    L1 = Label(top, text="Password",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=380,y=390)

    L1 = Label(top, text=":",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=500,y=390)

    E2 = Entry(top, bd =2)
    E2.pack(side = RIGHT)
    E2.place(x=580,y=400)

    

def admin():
    top = tkinter.Tk()
    top.geometry('2000x1000')
    
    def verify(a,b):
        if a=="admin" and b=="admin":
            top = tkinter.Tk()
            top.geometry('2000x1000')
            def fan_on():
                GPIO.output(fan,True)
            def fan_off():
                GPIO.output(fan,False)
            def light1_on():
                GPIO.output(light1,True)
            def light1_off():
                GPIO.output(light1,False)
            def light2_on():
                GPIO.output(light2,True)
            def light2_off():
                GPIO.output(light2,False)
            def adduser():
                top = tkinter.Tk()
                top.geometry('2000x1000')
                
            #taking 1st voice
                def sample(no):
                    FORMAT = pyaudio.paInt16
                    CHANNELS = 1
                    RATE = 44100#48000
                    CHUNK = 1024
                    RECORD_SECONDS = 2
                    p = E3.get()
                    WAVE_OUTPUT_FILENAME = "/home/pi/Downloads/Speaker-Identification-Python-master/trainingData/"+ p + no +".wav"

                    audio = pyaudio.PyAudio()
                    csv=p+no+".wav"
                    csv=csv+"\n"
                    f=open("trainingDataPath.txt","a")
                    f.write(csv)
                    f.close

                    # start Recording
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

                
                def register(c,d):
                    csv=c+d
                    csv=csv+"\n"
                    f=open("database.txt","a")
                    f.write(csv)
                    f.close
                    
                    warnings.filterwarnings("ignore")
                    source  = "trainingData/"   
                    dest = "Speakers_models/"
                    train_file = "trainingDataPath.txt"        
                    file_paths = open(train_file,'r')
                    count = 1
                    features = np.asarray(())
                    for path in file_paths:
                            path = path.strip()   
                            print (path)
                            sr,audio=read(source+path)
                            print(sr)
                            vector = extract_features(audio,sr)
                            if features.size == 0:
                                features = vector
                                print('count',count)
                            else:
                                features = np.vstack((features, vector))
                                print(features.shape)
                                print('count',count)
                            print('count',count)
                            if count==3:
                                gmm =mixture.GaussianMixture(n_components = 16,  covariance_type='diag',n_init = 3)
                                print('path')
                                path1='Speakers_models/'
                                gmm=gmm.fit(features)
                                count=0
                                picklefile=path.split('.')
                                print(str(picklefile))
                                picklefile = picklefile[0]
                                print(picklefile)
                                picklefile = picklefile[0:-1]+".gmm"
                                print(picklefile)
                            #if(picklefile=='deepankar/deepankar'):
                                
                                pickle.dump(features,open(dest+picklefile,'wb'))
                                print ('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)
                                features = np.asarray(())
                            count=count+1
                    top = tkinter.Tk()
                    top.geometry('200x50')
                    top.configure(background="#5c6268")
                    
                    
                    
                    L1 = Label(top, text="user registered")
                    L1.pack( side = LEFT)
                    L1.place(x=10,y=10)
                     
                
                L1 = Label(top, text="Add User",fg="black",font=('Times',32,"bold"))
                L1.pack( side = LEFT)
                L1.place(x=550,y=50)

                L1 = Label(top, text="Username",fg="black",font=('Times',22,"bold"))
                L1.pack( side = LEFT)
                L1.place(x=380,y=290)

                L1 = Label(top, text=":",fg="black",font=('Times',22,"bold"))
                L1.pack( side = LEFT)
                L1.place(x=510,y=290)

                E3 = Entry(top, bd =2)
                E3.pack(side = RIGHT)
                E3.place(x=580,y=300)

                L1 = Label(top, text="password",fg="black",font=('Times',22,"bold"))
                L1.pack( side = LEFT)
                L1.place(x=380,y=390)

                L3 = Label(top, text=":",fg="black",font=('Times',22,"bold"))
                L3.pack( side = LEFT)
                L3.place(x=510,y=390)

                E4 = Entry(top, bd =2)
                E4.pack(side = RIGHT)
                E4.place(x=580,y=400)
                
                B_1=Button(top,text="REGISTER",command=lambda:register(E3.get(),E4.get()))
                B_1.place(x=515,y=600)
                
                B_1=Button(top,text="voice sample 1",command=lambda:sample("1"))
                B_1.place(x=350,y=500)
                
                B_1=Button(top,text="voice sample 2",command=lambda:sample("2"))
                B_1.place(x=500,y=500)
                
                B_1=Button(top,text="voice sample 3",command=lambda:sample("3"))
                B_1.place(x=650,y=500)
        
            
            
            B_1=Button(top,text="Click Here To Add User",command=adduser,activebackground="green")
            B_1.place(x=450,y=400)
            
            
            L1 = Label(top, text="Fan1",fg="black",font=('Times',22,"bold"))
            L1.pack( side = LEFT)
            L1.place(x=200,y=100)
            
            L1 = Label(top, text="Light1",fg="black",font=('Times',22,"bold"))
            L1.pack( side = LEFT)
            L1.place(x=400,y=100)
            
            L1 = Label(top, text="Light2",fg="black",font=('Times',22,"bold"))
            L1.pack( side = LEFT)
            L1.place(x=600,y=100)
            
            B_1=Button(top,text="ON",command=fan_on,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=150,y=200)
            
            B_1=Button(top,text="OFF",command=fan_off,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=250,y=200)
            
            B_1=Button(top,text="ON",command=light1_on,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=350,y=200)
            
            B_1=Button(top,text="OFF",command=light1_off,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=450,y=200)
            
            B_1=Button(top,text="ON",command=light2_on,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=550,y=200)
            
            B_1=Button(top,text="OFF",command=light2_off,bg="black",fg="#14cece",activebackground="green")
            B_1.place(x=650,y=200)
                
        else:
            top = tkinter.Tk()
            top.geometry('200x50')
            top.configure(background="#5c6268")
            
            L1 = Label(top, text="Invalid Username or Password")
            L1.pack( side = LEFT)
            L1.place(x=10,y=10)
            
            tkinter.messagebox.showinfo("ALERT", "invalid username or password") 
            
    
    def login():
        pass
    
    
    L1 = Label(top, text="Welcome Admin!!",fg="black",font=('Times',32,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=500,y=50)

    L1 = Label(top, text="Username",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=380,y=290)

    L1 = Label(top, text=":",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=510,y=290)

    E1 = Entry(top, bd =2)
    E1.pack(side = RIGHT)
    E1.place(x=580,y=300)

    L1 = Label(top, text="password",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=380,y=390)

    L1 = Label(top, text=":",fg="black",font=('Times',22,"bold"))
    L1.pack( side = LEFT)
    L1.place(x=510,y=390)

    E2 = Entry(top, bd =2)
    E2.pack(side = RIGHT)
    E2.place(x=580,y=400)
    
    B_1=Button(top,text="LOGIN",command=lambda:verify(E1.get(),E2.get()))
    B_1.place(x=615,y=500)
    

B_1=Button(top,text="ADMIN",command=admin)
B_1.place(x=465,y=200)

B_1=Button(top,text="USER",command=user)
B_1.place(x=465,y=300)

L1 = Label(top, text="USER TYPE",font=('Times',32,"bold"))
L1.pack( side = LEFT)
L1.place(x=400,y=100)

top.mainloop()
