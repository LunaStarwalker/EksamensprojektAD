from analysis import Analysis
from start import Start_Page
from nicegui import ui

@ui.page('/')
def start():
    Start_Page()


@ui.page('/analysis')
def analysis():
    Analysis()

ui.run(port=4040)