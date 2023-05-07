import nltk

from functionality import Functionality
from nicegui import ui
import pandas as pd

class Morph:

    def __init__(self, func: Functionality):
        self.f = func
        self.container = ui.column().style("width: 1215px; align-items: center;")
        self.tagged = self.tag_to_dict()
        self.tagged.apply(self.get_rows)

        with self.container:
            ui.label("Morphology").style(
                "font-size: 30px; font-weight: bold; color: #757575; text-align: center;")
            ui.separator()
            ui.label("Word tagging can help you determine the different word classes used in your text.") \
                .style("font-size: 20px; color: #757575; text-align: justify;")
            columns = [
                {'name': 'name', 'label': 'Words', 'field': 'name', 'required': True, 'align': 'left'},
                {'name': 'age', 'label': 'Tag', 'field': 'age', 'sortable': True},
            ]
            rows = ""

    def tag_to_dict(self):

        temp = nltk.pos_tag(self.f.df_words)
        d = []

        for el in temp:
            d.append(el[1])

        tag = pd.DataFrame({"Words": self.f.df_words, "Tag": d})
        return tag

    def get_rows(self, n):

        print(type(n[0]))
