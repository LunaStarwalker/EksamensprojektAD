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
            ui.button("Save plot", on_click=self.save)

    def gen_plot(self, t: str):
        match t:
            case "Empty":
                self.card.clear()
            case "Frequency":
                self.gen_frequency_plot()
            case "Word-Cloud":
                self.gen_word_cloud()

    def gen_frequency_plot(self):
        self.card.clear()
        self.f.df_no_stopwords.nlargest(10, "Frequency").plot(kind="bar", x="Words", y="Frequency",
                                                              xlabel="Words", ylabel="Frequency")
        plt.subplots_adjust(bottom=0.3)
        plt.savefig("files/frequency.png")
        with self.card.style("width: 700px;"):
            ui.image("files/frequency.png")
            with ui.card_section():
                ui.label("Frequency Plot")



    def gen_word_cloud(self):
        self.card.clear()
        wordcloud = WordCloud(collocations=False, background_color='black', max_words=130, min_font_size=10) \
            .generate(self.f.string_data)
        wordcloud.to_file("files/wordcloud.png")
        with self.card.style("width: 700px;"):
            ui.image("files/wordcloud.png")
            with ui.card_section():
                ui.label("Word Cloud")

    def save(self):
        ui.notify("Saved successfully in files folder")
