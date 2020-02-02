import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())


'''import math
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from bartender import Bartender

class Menu():
    def __init__(self, master):
        self.master = master
        self.bartender = Bartender()
        self.drinks = self.bartender.filterDrinks()

        master.title("Bartender")
        master.resizable(0, 0)

        self.buttons = []
        self.numOfButton = 0

        for d in self.drinks:
            if d.visible == True:
                self.numOfButton += 1
                self.buttons.append(Button(master, text=d.name, command= lambda ing=d.ingredients: self.bartender.makeDrink(ing)))

        self.numOfRow = math.floor(math.sqrt(self.numOfButton))
        self.countButtons = 0

        for b in self.buttons:
            b.grid(row=int(self.countButtons / self.numOfRow), column=int(self.countButtons % self.numOfRow))
            self.countButtons += 1

        self.closeButton = Button(master, text='Close', command=lambda: self.quit(self.master))
        self.closeButton.grid(row=int((self.countButtons / 3)+1), column=1)

    def quit(self, master):
        self.bartender.quit()
        master.quit()

root = Tk()
menu = Menu(root)
root.mainloop()
'''
