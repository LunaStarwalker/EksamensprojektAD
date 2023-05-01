from functionality import Functionality
from nicegui import ui

class Overview:

    def __init__(self, func: Functionality):
        self.f = func
        self.container = ui.column().style("width: 1215px; align-items: center;")
        self.setup()

    def setup(self):
        with self.container:
            ui.label("Overview of text").style(
                "font-size: 30px; font-weight: bold; color: #757575; text-align: center;")
            ui.separator()
            ui.label("Here you can see an overview of the length, readability and sentiment analysis of your text.") \
                .style("font-size: 20px; color: #757575; text-align: justify;")
            with ui.card().tight():
                with ui.card_section():
                    with ui.row():
                        ui.label("Word-count: " + str(self.f.get_word_count()))\
                            .style("font-size: 20px; color: #757575; text-align: justify;")
                        ui.label("Word-count w/o stopwords: " + str(self.f.get_word_count_no_stopwords()))\
                            .style("font-size: 20px; color: #757575; text-align: justify;")
                    with ui.row():
                        ui.label("Line-count: " + str(self.f.get_sent_count())) \
                            .style("margin-top: 20px; font-size: 20px; color: #757575; text-align: justify;")


