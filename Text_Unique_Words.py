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
def Unique(data):
        file = open(data,'r') 
        text = file.read()
        file.close()
        word_list = text.split()
        
        word_list = [word.replace(".", "") for word in word_list]
        word_list = [word.replace(",", "") for word in word_list]
       
        file = open ('Text_Unique_Words.txt', 'w')
        
        unique_words = set(word_list)
       
        for word in unique_words:
        	file.write(str(word)+" ")
        file.close()
        return file

