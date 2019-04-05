import pyaudio
import pickle

import numpy as np
from scipy.io.wavfile import read
from sklearn import mixture
import warnings
import os
from featureextraction import extract_features

warnings.filterwarnings("ignore")

#path to training data
# source   = "development_set/"
#gg=os.path.dirname(path)
#print(gg)
#for path in filepaths:
#    print(path)
    
source  = "trainingData/"   

#path where training speakers will be saved

# dest = "speaker_models/"
# train_file = "development_set_enroll.txt"

dest = "Speakers_models/"
train_file = "trainingDataPath.txt"        
file_paths = open(train_file,'r')

count = 1
# Extracting features for each speaker (5 files per speakers)
features = np.asarray(())
for path in file_paths:
    #if(count<=6):
        path = path.strip()   
        print (path)
#        print(source+path)
    # read the audio
    #with audioread.audio_open(source+path) as f:
        sr,audio=read(source+path)
        print(sr)
        
        
    
    # extract 40 dimensional MFCC & delta MFCC features
        vector = extract_features(audio,sr)
        print(vector)
    
        if features.size == 0:
            features = vector
            
            print('count',count)
        else:
            features = np.vstack((features, vector))
            
            print('count',count)
    # when features of 5 files of speaker are concatenated, then do model training
    # -> if count == 5: --> edited below

    #features = np.asarray(())

        print('count',count)
        if count==3:
            gmm =mixture.GaussianMixture(n_components = 16,  covariance_type='diag',n_init = 3)
            print('path')
            path1='Speakers_models/'
            gmm.fit(features)
            count=0
    
         
        
            # dumping the trained gaussian model
            picklefile = path.split(".")[0]+".gmm"
            print(picklefile)
            pickle.dump(gmm,open(dest+picklefile,'wb'))
            print ('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)
        count=count+1