import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

class Functionality:

    def __init__(self, file):

        self.string_data = self.read_string(file)

        self.df_words = pd.DataFrame({"Words": self.clean_words(self.string_data).split()})
        self.df_lines = pd.Series(self.read_lines(self.clean_lines(self.string_data)))

        self.df_words["Frequency"] = self.df_words["Words"].map(self.df_words["Words"].value_counts(normalize=True))

        print(self.df_words)
        print(self.df_lines)


    def read_string(self, file):
        with open(file, "r") as f:
            data = f.read().replace('\n', ' ')

        return data

    def read_lines(self, file):
        data = sent_tokenize(file)

        return data

    def clean_words(self, data):
        text = re.sub("[\W]", " ", data)
        text = re.sub("\s+", " ", text)
        return text

    def clean_lines(self, data):
        text = re.sub("[^\w.']+", " ", data)
        text = re.sub("\s+", " ", text)
        return text


myb = Functionality("words.txt")
