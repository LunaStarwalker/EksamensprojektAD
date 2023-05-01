from functionality import Functionality
from nicegui import ui
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class Plots:

    def __init__(self, f: Functionality):
        self.f = f
        with ui.column().style("width: 1215px; align-items: center;"):
            ui.label("Generate Plots").style(
                "font-size: 30px; font-weight: bold; color: #757575; text-align: center;")
            ui.separator()
            ui.label("Choose which plot you want generated from the menu below.") \
                .style("font-size: 20px; color: #757575; text-align: justify;")
            select = ui.select(["Empty", "Frequency", "Word-Cloud"], value="Empty")
            select.on('update:model-value', lambda x: self.gen_plot(x["args"]['label']))
            self.card = ui.card().tight().style("padding: 20px")
            ui.button("Save plot", on_click=self.save())

    def gen_plot(self, t):
        match t:
            case "Empty":
                self.card.clear()
            case "Frequency":
                self.gen_frequency_plot()
            case "Word-Cloud":
                self.gen_word_cloud()

    def gen_frequency_plot(self):
        self.card.clear()
        with self.card:
            with ui.pyplot(figsize=(3, 2)).style("fill: #ffffff00;"):
                word_cloud = WordCloud(collocations=False, background_color='black').generate(self.f.string_data)
                plt.imshow(word_cloud, interpolation='bilinear')
                plt.axis("off")


    def gen_word_cloud(self):
        self.card.clear()
        with self.card:
            with ui.pyplot(figsize=(9, 6)).style("fill: #ffffff00;"):
                word_cloud = WordCloud(collocations=False, background_color='black', max_words=130, min_font_size=10)\
                    .generate(self.f.string_data)

                plt.imshow(word_cloud, interpolation='bilinear')
                plt.axis("off")
                with ui.card_section():
                    ui.label("Word Cloud")

    def save(self):
        pass
