import kivy

from kivy.app import App
from kivy.uix.label import Label

class MenuItem(object):
    def __init__(self, name, ingredients=None, visible=False):
        self.name = name
        self.ingredients = ingredients
        self.visible = visible

class Menu(App):
    def build(self):
        return Label(text='Bartender')
