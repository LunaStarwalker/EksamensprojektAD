import pandas as pd
from nltk.tokenize import word_tokenize
from functionality import Functionality

class Summarizer:

    def __init__(self, f: Functionality):
        self.sentence_score = {}
        self.lines = pd.Series(f.lines)
        self.words_n_freq = f.words_n_freq
        self.lines.apply(self.sent_freq)

    def sent_freq(self, sent: str):
        score = 0
        for s_word in word_tokenize(sent):
            if s_word.lower() in self.words_n_freq.keys():
                score += self.words_n_freq[s_word.lower()]

        self.sentence_score[sent] = score

    def summary(self, n: int) -> str:
        s = pd.DataFrame.from_dict({"Lines": self.sentence_score.keys(),
                                         "Score": self.sentence_score.values()})
        summary = " ".join(s.nlargest(n, "Score")["Lines"])
        return summary

