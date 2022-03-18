from asyncore import read
from importlib.resources import as_file
import re
from urllib import request
from nltk import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter
import requests
import json


requestFile = "https://raw.githubusercontent.com/notChewy1324/miniProjects/master/plagiarismData.json"

try:
    train_data_file = requests.get(f"{requestFile}") #File with training data
except:
    print("Failed to create an connection. Check your internet.")
    
train_data_json = train_data_file.json()['TrainingINFO']
    
train_data_json = re.sub(r"\[.*\]|\{.*\}", "", str(train_data_json)) #selected a line to fix TypeError
train_data_json = re.sub(r'[^\w\s]', "", train_data_json)

n = 4

training_data = str(train_data_json)

ngrams = list(training_data)
print("Number of ngrams: ", len(ngrams))

model = WittenBellInterpolated(n)
model.fit([ngrams], vocabulary_text=training_data)
print(model.vocab)



try:
    test_data_file = requests.get(f"{requestFile}") #File with testing data
except:
    print("Failed to create an connection. Check your internet.")
    
test_text = test_data_file.json()["TestingINFO"]

test_text = re.sub(r'[^\w\s]', "", str(test_text))

testing_data = str(test_text)

print("Length of test data:", len(testing_data))


# assign scores
scores = [] 
for i, item in enumerate(testing_data[n-1:]): 
    s = model.score(item, testing_data[i:i+n-1]) 
    scores.append(s) 
    
    scores_np = np.array(scores)
    

#Gui

width = 8
height = np.ceil(len(testing_data)/width)
print(f"Width: {width}, Height: {height}")