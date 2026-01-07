
import pandas as pd
import re

data = pd.read_csv("hate_speech.csv")

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    return text

data['cleaned_tweet'] = data['tweet'].apply(preprocess)
data.to_csv("processed_hate_speech.csv", index=False)

print("Preprocessing completed")
