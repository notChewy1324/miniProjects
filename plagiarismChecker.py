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
    
train_data_json = re.sub(r"\[.*\]|\{.*\}", "", str(train_data_json))
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
height = int(len(testing_data)/width)
print(f"Width: {width}, Height: {height}")

a = np.zeros(width*height)
a[:len(scores_np)] = scores_np
diff = len(a) - len(scores_np)

a = gaussian_filter(a, sigma=1.0)

a = a.reshape(-1, width) # reshape to fit rectangle

# format labels
labels = [" ".join(testing_data[i:i+width]) for i in range(n-1, len(testing_data), width)]
labels_individual = [x.split() for x in labels]
labels_individual[-1] += [""]*diff
labels = [f"{x:60.60}" for x in labels]

# create heatmap
fig = go.Figure(data=go.Heatmap(
                z=a, x0=0, dx=1,
                y=labels, zmin=0, zmax=1,
                customdata=labels_individual,
                hovertemplate='%{customdata} <br><b>Score:%{z:.3f}<extra></extra>',
                colorscale="burg"))
fig.update_layout({"height":height*28, "width":1000, "font":{"family":"Courier New"}})
fig['layout']['yaxis']['autorange'] = "reversed"
fig.show()