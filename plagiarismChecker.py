import re
from nltk import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter
import requests



try:
    train_data_file = requests.get("https://raw.githubusercontent.com/notChewy1324/miniProjects/master/training_data.json") #File with training data
except:
    print("Failed to create an connection. Check your internet.")
    
train_data_json = train_data_file.json()['TestingINFO']

print(f"DEBUG INFO: {train_data_json}")
    
train_data_json = re.sub(r"\[.*\]|\{.*\}", "", train_data_json["line1"]) #selected a line to fix TypeError
train_data_json = re.sub(r'[^\w\s]', "", train_data_json)

n = 4

training_data = list(pad_sequence(word_tokenize(train_data_json), n, 
                                  pad_left=True, 
                                  left_pad_symbol="<s>"))

ngrams = list(everygrams(pad_sequence, max_len=n))
print("Number of ngrams: ", len(ngrams))

model = WittenBellInterpolated(n)
model.fit([ngrams], vocabulary_text=training_data)
print(model.vocab)



try:
    test_data_file = requests.get("https://raw.githubusercontent.com/notChewy1324/miniProjects/master/testing_data.json") #File with training data
except:
    print("Failed to create an connection. Check your internet.")
    
test_text = test_data_file.json()["line1"]

test_text = re.sub(r'[^\w\s]', "", test_text)


testing_data = list(pad_sequence(word_tokenize(test_text), n, 
                                 pad_left=True,
                                 left_pad_symbol="<s>"))
print("Length of test data:", len(testing_data))