class MenuItem(object):
    def __init__(self, name, ingredients=None, visible=False):
        self.name = name
        self.ingredients = ingredients
        self.visible = visible
