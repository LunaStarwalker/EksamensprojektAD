from nicegui import ui, events
from header import Header

class Start_Page:

    def __init__(self):
        self.container = ui.column().style("float: center; margin: auto; width: 700px; align-items: center;")
        self.setup()


    def setup(self):
        Header()
        with self.container:
            ui.label("Welcome to The Natural Language Analyser").style("font-size: 40px; font-weight: bold; color: #757575; text-align: center;")
            ui.label("With this natural language processing toolkit, "
                     "understanding the inner mechanics and composition of any text becomes as easy as clicking a button. "
                     "Our tool gives you easy access to word and sentence tokenization, lemmatization and stemming, "
                     "as well as extensive frequency plots, readability and sentiment analyses and even a summarizer tool "
                     "to help with quick comprehension of any text.")\
                .style("font-size: 20px; color: #757575; text-align: justify;")
            ui.label("Simply start by uploading your text below and begin your natural language processing journey.")\
                .style("font-size: 20px; color: #757575; text-align: justify;")
            ui.separator()
            ui.upload(auto_upload=True, on_upload=self.handle_upload).style("margin-top: 50px;")
            ui.label("Uploaded files must be .txt format").style("font-size: 15px; font-weight: bold; color: #757575; text-align: left;")

    def handle_upload(self, event: events.UploadEventArguments):
        with event.content as f:
            t = f.read()
            with open("files/data.txt", 'w') as x:
                x.write(t.decode('utf-8'))

        ui.open("/analysis")
