import matplotlib.pyplot as plt
from wordcloud import WordCloud

class Word_Cloud:

    def __init__(self, data, color="white"):
        self.word_cloud = WordCloud(collocations=False, background_color=color).generate(data)
        self.show()

    def show(self):
        plt.imshow(self.word_cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()