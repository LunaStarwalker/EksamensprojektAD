from nicegui import ui, app

class Header:
    def __init__(self):
        app.add_static_files('/files', 'files')
        ui.colors(primary='#556b2F', secondary='#FFFFFF')
        with ui.header().classes('items-center'):
            ui.label("The Natural Language Analyser").style("font-size: 20px; font-weight: bold;")

