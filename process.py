from functionality import Functionality
from nicegui import ui

class Overview:

    def __init__(self, func: Functionality):
        self.f = func
        self.container = ui.column().style("width: 1215px; align-items: center;")
        self.time = self.f.get_word_count() / 200
        self.setup()
        with ui.column().style("width: 1215px; align-items: center; margin-top: 30px;"):
            ui.label("Input your reading speed for a more accurate estimate of reading time.")\
                .style("font-size: 20px; color: #757575; text-align: justify; align: center;")
            self.reading_speed = ui.number(label='Words per min', value=200, format='%.0f')\
                    .style("width: 100px; align: center;")
        self.reading_speed.on('update:model-value', lambda x: self.new_time(x["args"]))

    def setup(self):
        self.container.clear()
        with self.container:
            ui.label("Overview of text").style(
                "font-size: 30px; font-weight: bold; color: #757575; text-align: center;")
            ui.separator()
            ui.label("Here you can see an overview of the length and readability of your text.") \
                .style("font-size: 20px; color: #757575; text-align: justify;")
            with ui.card().tight():
                with ui.card_section():
                    ui.label("Word-count: " + str(self.f.get_word_count()))\
                        .style("font-size: 20px; color: #757575; text-align: justify;")
                    ui.label("Word-count w/o stopwords: " + str(self.f.get_word_count_no_stopwords()))\
                        .style("margin-top: 20px; font-size: 20px; color: #757575; text-align: justify;")
                    ui.label("Line-count: " + str(self.f.get_sent_count()))\
                        .style("margin-top: 20px; font-size: 20px; color: #757575; text-align: justify;")
                    ui.label("Lix score: " + str(int(self.f.get_lixtal())))\
                        .style("margin-top: 20px; font-size: 20px; color: #757575; text-align: justify;")
                    ui.label("Estimated reading time: " + str(int(self.time)) + " minute(s)")\
                        .style("margin-top: 20px; font-size: 20px; color: #757575; text-align: justify;")

    def new_time(self, speed):
        try:
            self.time = self.f.get_word_count() / int(speed)
            self.setup()
        except:
            pass

