import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re

class Functionality:

    def __init__(self):

        self.string_data = self.read_string("files/data.txt")
        self.stop_words = stopwords.words("english")

        self.np_words = np.array(self.clean_words(self.string_data).split())
        self.df_no_stopwords = self.clean_stop_words(self.np_words)
        self.lines = self.read_lines(self.string_data)

        self.df_no_stopwords["Frequency"] = self.df_no_stopwords["Words"]\
            .map(self.df_no_stopwords["Words"].value_counts(normalize=True))

        self.df_no_stopwords.drop_duplicates(subset="Words", inplace=True, ignore_index=True)
        self.words_n_freq = dict(zip(self.df_no_stopwords.Words, self.df_no_stopwords.Frequency))


    def read_string(self, file: str) -> str:
        with open(file, 'r') as f:
            data = f.read().replace('\n', ' ')
        return data

    def read_lines(self, file: str) -> list[str]:
        data = sent_tokenize(file)
        return data

    def clean_words(self, data: str) -> str:
        text = re.sub(r"\W", " ", data)
        text = re.sub(r"\s+", " ", text)
        return text.lower()

    def clean_stop_words(self, data: np.ndarray) -> pd.DataFrame:
        temp = [word for word in data if word not in self.stop_words]
        new = pd.DataFrame({"Words": temp})

        return new

    def get_word_count(self) -> int:
        return self.np_words.size

    def get_sent_count(self) -> int:
        return len(self.lines)

    def get_word_count_no_stopwords(self) -> int:
        return self.df_no_stopwords.size

    def get_lixtal(self) -> float:
        long_words = []
        for word in self.np_words:
            if len(word) > 6:
                long_words.append(word)
        long_word_amount = len(long_words)

        lixtal = self.get_word_count() / self.get_sent_count() + (long_word_amount * 100 / self.get_word_count())
        return lixtal


