import Text_Remove_Stopwords as t
import text_lemmatizer as l
import Text_Unique_Words as u
import Text_To_Vector as k
import WordVectorCSV as w
import CreateTextDataset as c
import speech as sp

o=open('passage.txt','a')
print('ask question\n')
data=sp.fun()
data=data+'\n'
o.write(data)
o.close()

x=t.remove_stopwords('passage.txt')

a=l.lemaitie(x.name)

uniq=u.Unique(a.name)

tv=k.TexttoVector(uniq.name)

d=w.Wordvector(tv.name)

c.run(d.name)




'''
stop_words = set(t.stopwords.words('english'))
s=t.nltk.word_tokenize(data)
f = [w for w in s if not w in stop_words]
lemmatizer = l.WordNetLemmatizer()
p=''
for i in f:
    p=p+lemmatizer.lemmatize(i)+' '
g=[]
k.'''


    




