from analysis import Analysis
from start import Start_Page
from nicegui import ui


if __name__ in {"__main__", "__mp_main__"}:

    @ui.page('/')
    def start():
        Start_Page()


    @ui.page('/analysis')
    def analysis():
        Analysis()

    ui.run(port=4040)





