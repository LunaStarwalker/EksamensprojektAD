import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer

text = "Ringworm is a fungal infection that causes a red circular patch to develop on your skin. " \
       "It is a contagious condition that even your pets can transmit to you. " \
       "Ringworm may cause itching and swelling, and possibly even scarring. " \
       "If you have a ringworm scar, then there are several things that may help to treat it."

sentence_w_tokenized = word_tokenize(text)

print(sentence_w_tokenized)