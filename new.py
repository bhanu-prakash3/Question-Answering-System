#from nltk import RegexpParser
#from nltk import tokenize
#from nltk.tree import *
#from tempfile import TemporaryFile
import nltk
#import os
import csv
import pandas as pd
#import itertools
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#from nltk import word_tokenize, pos_tag, ne_chunk
#import numpy as np
#import math

#Python 2.x program for Speech Recognition
 
import speech_recognition as sr
 
#enter the name of usb microphone that you found
#using lsusb
#the following name is only used as an example
mic_name = "Microphone (High Definition Aud"
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
    if microphone_name ==mic_list[2]:
        device_id = 2
 
#use the microphone as source for input. Here, we also specify 
#which device ID to specifically look for incase the microphone 
#is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
    #wait for a second to let the recognizer adjust the 
    #energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print ("Say Something")
    #listens for the user's input
    audio = r.listen(source)
         
    try:
        text = r.recognize_google(audio)
        print ("you said:"  + text)
     
    #error occurs when google could not understand what was said
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))




def one():
   
    stop_words = set(stopwords.words('english'))
    sent_text = nltk.sent_tokenize(text)
    file = open('Text_Without_Stopwords.txt','w') 
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        filtered_sentence = [w for w in tokenized_text if not w in stop_words]
        filtered_sentence = []
        temp=""
        
        for w in tokenized_text:
            if w not in stop_words:
                filtered_sentence.append(w)
                temp = temp + w +" "

    #print(temp)
        file.write(temp)
    file.close()
    
    
    
def two():
    file = open('Text_Without_Stopwords.txt','r') 
    text = file.read()
    file.close()
    lemmatizer = WordNetLemmatizer()

    stop_words = set(stopwords.words('english'))
    sent_text = nltk.sent_tokenize(text)
    file = open('Text_Lemmatized.txt','w') 
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        filtered_sentence = [w for w in tokenized_text if not w in stop_words]
        #filtered_sentence = []
        temp=""
        tokenized_text = nltk.word_tokenize(sentence)
        for w in tokenized_text:
        #filtered_sentence.append(w)
            temp = temp + lemmatizer.lemmatize(w) +" "
        file.write(temp)
    file.close()
    

def three():
    file = open('Text_Lemmatized.txt','r') 
    text = file.read()
    file.close()
    word_list = text.split()
    word_list = [word.replace(".", "") for word in word_list]
    word_list = [word.replace(",", "") for word in word_list]
    file = open ('Text_Unique_Words.txt', 'w')
    #print(word_list)
    unique_words = set(word_list)
    #print(unique_words)
    for word in unique_words:
        file.write(str(word)+" ")
    file.close()
    
    
def four():
    file = open('Text_Unique_Words.txt','r') 
    text = file.read()
    file.close()
    wordlist = text.split()
    file = open('Text_to_Vector.txt','w') 
    
    file1 = open('Text_Lemmatized.txt','r') 
    text = file1.read()
    file1.close()
    sent_text = nltk.sent_tokenize(text)
    file.write(str(wordlist) + '\n')
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        wordfreq = []
        for w in wordlist:
            wordfreq.append(sentence.count(w))

        file.write(str(wordfreq) + '\n')
    file.close()

    # Read in the file
    with open('Text_to_Vector.txt', 'r') as file :
      filedata = file.read()
    file.close()
    
    # Replace the target string
    filedata = filedata.replace('[', '')
    filedata = filedata.replace(']', '')
    
    # Write the file out again
    with open('Text_to_Vector.txt', 'w') as file:
      file.write(filedata)
    file.close()


def five():
   with open('Text_to_Vector.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)

    lines = (line.split(",") for line in stripped if line)
    with open('WordVectortest.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('title', 'intro'))
        writer.writerows(lines)
        
one()
two()
three()
four()
five()
    

testset = pd.read_csv('WordVectortest.csv')
testsetval = list(testset)
#print(testsetval)

for i in range(len(testsetval)):
    testsetval[i] = testsetval[i].lower()
    if ' ' in testsetval[i]:
        testsetval[i] = testsetval[i].replace(' ','')
    


dataset = pd.read_csv('WordVector.csv')
datasetval = list(dataset)
#print(datasetval)


for i in range(len(datasetval)):
    datasetval[i] = datasetval[i].lower()
    if ' ' in datasetval[i]:
        datasetval[i] = datasetval[i].replace(' ','')
        
        
        
        

count = []
for k in range(len(dataset)):
    myset = dataset.iloc[k]
    c = 0
    for i  in range(len(testsetval)):
        if myset[datasetval.index(testsetval[i])]==1:
                c = c + 1
    count.append(c)
    

#print(count.index(max(count)))


myfile = open('passage.txt','r')

data = myfile.read()

mydata = data.split('.')
ans=mydata[count.index(max(count))]

myfile.close()
print(ans)
from gtts import gTTS
tts = gTTS(text=ans, lang='en')
tts.save('ans2.mp3')
import pygame
pygame.init()
pygame.mixer.music.load("ans2.mp3")
pygame.mixer.music.play()
'''from playsound import playsound
playsound('ans2.mp3')'''