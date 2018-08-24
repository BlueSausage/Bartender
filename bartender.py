import time
import sys
import json
import itertools

from drinks import drink_list, drink_options
from menu import MenuItem

FLOW_RATE = 60./100.0


class Bartender:
    def __init__(self):
        self.running = False


        # load the pump configuration from file
        self.pump_configuration = Bartender.readPumpConfiguration()

    @staticmethod
    def readPumpConfiguration():
        return json.load(open('pump_config.json'))

    @staticmethod
    def writePumpConfiguration(configuration):
        with open('pump_config.json', 'w') as jsonFile:
            json.dump(configuration, jsonFile)


    def showPumpConfiguration(self):
        for p in sorted(self.pump_configuration.keys()):
            print(self.pump_configuration[p]['name'], self.pump_configuration[p]['value'])

    def changePumpConfiguration(self, name, newValue):
        for p in sorted(self.pump_configuration.keys()):
            if self.pump_configuration[p]['name'] == name:
                self.pump_configuration[p]['value'] = newValue
                self.writePumpConfiguration(self.pump_configuration)
                break

    def filterDrinks(self):
        """
                Removes any drinks that can't be handled by the pump configuration
        """
        drinks = []
        for d in drink_list:
            drinks.append(MenuItem(d['name'], d['ingredients'].keys(), False))

        n = 0
        k = 0
        ingredients = 0
        while n < len(drinks):
            while k < len(list(drinks.__getitem__(n).attributes)):
                for p in sorted(self.pump_configuration):
                    if self.pump_configuration[p]['value'] is not None:
                        if list(drinks.__getitem__(n).attributes).__getitem__(k) == self.pump_configuration[p]['value']:
                            ingredients += 1
                k += 1
            if len(list(drinks.__getitem__(n).attributes)) == ingredients:
                drinks.__getitem__(n).visible = True
            ingredients = 0
            k = 0
            n += 1

        j = 0
        while j < len(drinks):
            if drinks.__getitem__(j).visible is True:
                print(drinks.__getitem__(j).name)
            j += 1


if __name__ == '__main__':
    bartender = Bartender()
    bartender.filterDrinks()
