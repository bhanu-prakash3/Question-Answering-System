from nltk import RegexpParser
from nltk import tokenize
from nltk.tree import *
from tempfile import TemporaryFile
import nltk
import os
import itertools
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import word_tokenize, pos_tag, ne_chunk
import numpy
import math
import matplotlib.pyplot as plt

def lemaitie(data):
        file = open(data,'r') 
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
        return file
        
