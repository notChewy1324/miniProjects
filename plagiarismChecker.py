import re
from nltk import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter
import requests

try:
    train_data_file = requests.get("https://raw.githubusercontent.com/notChewy1324/miniProjects/d0627c5dd3581e161a4ce9ec0cedbf48969010e2/training_data.json") #File with training data
except:
    print("Failed to create an connection. Check your internet.")
    
train_data_json = train_data_file.json()['line1']
    
train_data_json = re.sub(r"\[.*\]|\{.*\}", "", train_data_json)
train_data_json = re.sub(r'[^\w\s]', "", train_data_json)

n = 4

training_data = list(pad_sequence(word_tokenize(train_data_json), n, 
                                  pad_left=True, 
                                  left_pad_symbol="<s>"))

ngrams = list(everygrams(pad_sequence, max_len=n))
print("Number of ngrams: ", len(ngrams))