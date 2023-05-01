from functionality import Functionality

class Morph:

    def __init__(self, func: Functionality):
        self.f = func
        self.container = ui.column().style("width: 1215px; align-items: center;")
        self.summarizer = Summarizer(self.f)

        with self.container:
            ui.label("Summary Generator").style(
                "font-size: 30px; font-weight: bold; color: #757575; text-align: center;")
            ui.separator()
            ui.label("A summary can help you understand the central points of a longer text fast and easy.") \
                .style("font-size: 20px; color: #757575; text-align: justify;")
            rec = 0.12 * self.f.get_sent_count()
            ui.label("Choose the number of lines you want your summary to be. "
                     "For your text, the recommended number of lines is " + str(int(rec)) + ".") \
                .style("font-size: 20px; color: #757575; text-align: justify;")
            number = ui.number(label='No. of lines', format='%.0f',
                               validation={"Value is too small.": lambda value: value > 0,
                                           "Not enough lines in original text.": lambda value: value < len(
                                               self.f.lines)}) \
                .style("margin-top: 30px;")
            number.on('update:model-value', lambda x: self.summarize(int(x["args"])))
            with ui.card().tight().style("padding: 20px"):
                with ui.card_section():
                    self.sum = ui.label(self.summarizer.s).style("width: 700px;")

            ui.button("Save as file", on_click=self.save)