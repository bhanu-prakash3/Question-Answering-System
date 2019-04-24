import pandas as pd
import csv
import numpy as np


def run(data):
                v = open(data)
                r = csv.reader(v)
                row0 = next(r)
                row0.append('category')
                csv_input1 = pd.read_csv('WordVector.csv')
                csv_input2 = pd.read_csv('WordClass.csv')
                csv_input1['category'] = csv_input2['category']
                csv_input1.to_csv('TextDataset.csv', index=False)
                
                
               
                XT=csv_input1.iloc[4,0:10].values
                X=csv_input1.iloc[:4,0:10].values
                Y=csv_input1.iloc[0:4,10].values
                
                
                '''
                
                k=[0,0,0,0]
                for i in range(len(X)):
                    for j in range(len(X[i])):
                        if(X[i][j]==XT[j]):
                            k[i]=k[i]+1
                
                A=pd.read_csv('C:/Users/venu/Desktop/ml/text/passage.txt',header=None)
                a=max(k)
                s=k.index(a)
                A=np.array(A)
                ans=A[s]
                print(ans)'''
                
                      
                           
                
                
                XT=XT.reshape((1,10))
                Y=Y.reshape((4,1))
                import numpy as np
                Y[0][0]=1
                Y[1][0]=2
                Y[2][0]=3
                Y[3][0]=4
                
                
                
                
                Y=np.array(Y)
                Y=np.reshape(Y,(4,))
                from sklearn.preprocessing import LabelEncoder, OneHotEncoder
                labelencoder_X_1 = LabelEncoder()
                Y = labelencoder_X_1.fit_transform(Y)
                
                Y=np.reshape(Y,(4,1))
                onehotencoder = OneHotEncoder(categorical_features=[0])
                Y = onehotencoder.fit_transform(Y).toarray()
                
                
                
                
                
                
                import keras.utils.np_utils as s
                from keras.models import Sequential
                from keras.layers import Dense
                from  keras.layers import Dropout
                
             
                classifier=Sequential()
                
                classifier.add(Dense(output_dim=7,init='uniform',activation='sigmoid',input_dim=10))
                
                classifier.add(Dense(output_dim=7,init='uniform',activation='sigmoid'))
                
                classifier.add(Dense(output_dim=4,init='uniform',activation='sigmoid'))
                
                
                classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
                
                classifier.fit(X, Y, batch_size = 10, epochs = 5000,verbose=0)
                
                y=classifier.predict(XT)
                
                
                
                
                
                
                y=y.reshape((4,))
                y=y.tolist()
                l=y.index(max(y))
                
                #A=open('passage.txt')
            
                A=pd.read_csv('passage.txt',header=None)
                x=A.iloc[l,:].values
                z=x[0]
                
                from gtts import gTTS
                from playsound import playsound
                import os
                
                tts=gTTS(text=z,lang='en')
                playsound(z+'.mp3',True)
                












