import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import heapq

class Summarizer:

    def __init__(self, file, n):

        with open(file, "r") as f:
            self.data = f.read().replace('\n', ' ')

        self.word_frequency = {}
        self.sentence_score = {}

        self.stop_words = set(stopwords.words("english"))
        self.sentence_tokenized = sent_tokenize(self.data)
        self.cleaned_up = self.clean_up(self.data)
        self.word_tokenized = self.word_tok(self.cleaned_up)

        self.word_freq()
        self.sent_freq()

        self.summary(n)

    def clean_up(self, data):
        text = re.sub("[\W]", " ", data)
        text = re.sub("\s+", " ", text)
        return text

    def sent_tok(self, data):
        temp = re.sub("[^\w.']+", " ", data)
        temp = re.sub("\s+", " ", temp)

        sentence_tokenized = sent_tokenize(temp)
        return sentence_tokenized

    def word_tok(self, data):
        word_tokenized = word_tokenize(data)
        word_tokenized = [word for word in word_tokenized if word not in self.stop_words]
        return word_tokenized

    def word_freq(self):
        for word in self.word_tokenized:
            if word not in self.word_frequency.keys():
                self.word_frequency[word] = 1
            else:
                self.word_frequency[word] += 1

        maximum_frequency = max(self.word_frequency.values())

        for word in self.word_frequency.keys():
            new_frequency = (self.word_frequency[word]/maximum_frequency)
            self.word_frequency[word] = new_frequency

    def sent_freq(self):
        for sent in self.sentence_tokenized:
            for s_word in word_tokenize(sent):
                if s_word in self.word_frequency.keys():
                    if sent not in self.sentence_score.keys():
                        self.sentence_score[sent] = self.word_frequency[s_word]
                    else:
                        self.sentence_score[sent] += self.word_frequency[s_word]

    def summary(self, n):

        k = self.get_key(max(self.sentence_score.values()), self.sentence_score)
        summary = heapq.nlargest(n, self.sentence_score, key=self.sentence_score.get)
        print(" ".join(summary))

    def get_key(self, v, dic):
        for key, val in dic.items():
            if v == val:
                return key


mySummarizer = Summarizer("words.txt", 2)