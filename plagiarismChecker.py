import re
from nltk import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter
import requests

try:
    train_data_file = requests.get("https://github.com/notChewy1324/miniProjects/blob/master/training_data.txt") #File with training data
except:
    print("Failed to create an connection. Check your internet.")

with open(train_data_file) as f:
    train_text = f.read().lower()
    
train_text = re.sub(r"\[.*\]|\{.*\}", "", train_text)
train_text = re.sub(r'[^\w\s]', "", train_text)

n = 4

training_data = list(pad_sequence(word_tokenize(train_text), n, 
                                  pad_left=True, 
                                  left_pad_symbol="<s>"))

ngrams = list(everygrams(pad_sequence, max_len=n))
print("Number of ngrams: ", len(ngrams))