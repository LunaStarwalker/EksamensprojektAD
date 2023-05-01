from nicegui import ui
from header import Header
from process import Overview
from morph import Morph
from summary import Summary
from plots import Plots
from functionality import Functionality

class Analysis:

    def __init__(self):
        self.f = Functionality()
        self.setup()

    def setup(self):
        Header()
        with ui.tabs() as tabs:
            ui.tab('Overview')
            ui.tab('Morphology')
            ui.tab('Summarizer')
            ui.tab('Plots')

        with ui.tab_panels(tabs, value='Overview'):
            with ui.tab_panel('Overview'):
                Overview(self.f)
            """with ui.tab_panel('Morphology'):
                Morph(self.f)"""
            with ui.tab_panel('Summarizer'):
                Summary(self.f)
            with ui.tab_panel('Plots'):
                Plots(self.f)

