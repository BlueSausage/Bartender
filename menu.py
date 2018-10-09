import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from bartender import Bartender

class MenuItem(object):
    def __init__(self, name, ingredients=None, visible=False):
        self.name = name
        self.ingredients = ingredients
        self.visible = visible

class Menu(App):
    def __init__(self):
        self.bartender = Bartender()

    def build(self):
        layout = GridLayout(cols=3)
        for p in sorted(self.bartender.pump_configuration.keys()):
            if(self.bartender.pump_configuration[p]['value'] is not None):
                layout.add_widget(Button(text=self.bartender.pump_configuration[p]['value']))
