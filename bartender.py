import time
import sys
import json


from drinks import  drink_list, drink_options

FLOW_RATE = 60./100.0


class Bartender:
    def __init__(self):
        self.running = False

        # load the pump configuration from file
        self.pump_configuration = Bartender.readPumpConfiguration()
        for pump in self.pump_configuration.keys():
            GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)

    @staticmethod
    def readPumpConfiguration():
        return json.load(open('pump_config.json'))

    @staticmethod
    def writePumpConfiguration(configuration):
        with open("pump_config.json", "w") as jsonFile:
            json.dump(configuration, jsonFile)

    def showPumpConfiguration(self):
        for p in sorted(self.pump_configuration.keys()):
            print(self.pump_configuration[p]["name"], self.pump_configuration[p]["value"])

    def changePumpConfiguration(self, name, value):
        for p in sorted(self.pump_configuration.keys()):
            if self.pump_configuration[p]["name"] == name:
                self.pump_configuration[p]["value"] = value
                self.writePumpConfiguration(self.pump_configuration)
                break