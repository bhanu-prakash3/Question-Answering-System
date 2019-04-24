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

def remove_stopwords(data):
       file = open(data,'r') 
       text = file.read()
       file.close()
       

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
          
            
             file.write(temp)
       temp1=file
       file.close()
       return temp1
       
       
       

