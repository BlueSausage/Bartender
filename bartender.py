import time
import sys
import json
import threading
import RPi.GPIO as GPIO

from drinks import drink_list, drink_options
from menuItem import MenuItem

GPIO.setmode(GPIO.BCM)

FLOW_RATE = 60./100.0

class Bartender:
    def __init__(self):
        # load the pump configuration from file
        self.pump_configuration = Bartender.readPumpConfiguration()
        for pump in self.pump_configuration.keys():
            GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)

    @staticmethod
    def readPumpConfiguration():
        return json.load(open('pump_config.json'))

    @staticmethod
    def writePumpConfiguration(configuration):
        with open('pump_config.json', 'w') as jsonFile:
            json.dump(configuration, jsonFile)

    def changePumpConfiguration(self, name, newValue):
        for p in sorted(self.pump_configuration.keys()):
            if self.pump_configuration[p]['name'] == name:
                self.pump_configuration[p]['value'] = newValue
                self.writePumpConfiguration(self.pump_configuration)
                break

    def filterDrinks(self):
        """
                Removes any drinks that can't be handled by the current pump configuration
        """
        drinks = []
        for d in drink_list:
            drinks.append(MenuItem(d['name'], d['ingredients'], False))

        n = 0
        k = 0
        ingredients = 0
        while n < len(drinks):
            while k < len(list(drinks.__getitem__(n).ingredients)):
                for p in sorted(self.pump_configuration):
                    if self.pump_configuration[p]['value'] is not None:
                        if list(drinks.__getitem__(n).ingredients).__getitem__(k) == self.pump_configuration[p]['value']:
                            ingredients += 1
                k += 1
            if len(list(drinks.__getitem__(n).ingredients)) == ingredients:
                drinks.__getitem__(n).visible = True
            ingredients = 0
            k = 0
            n += 1

        return drinks

    def makeDrink(self, ingredients):
        pumpThreads = []
        for ing in ingredients.keys():
            for p in self.pump_configuration.keys():
                if ing == self.pump_configuration[p]['value']:
                    waitTime = ingredients[ing] * FLOW_RATE
                    pump_thread = threading.Thread(target=self.pourDrink, args=(self.pump_configuration[p]['pin'], waitTime))
                    pumpThreads.append(pump_thread)
        #Start the pump threads
        for threads in pumpThreads:
            threads.start()
        #Wait for threads to finish
        for threads in pumpThreads:
            threads.join()
        time.sleep(1)

    def pourDrink(self, pin, pourTime):
        print("The pin " + str(pin) + " pours " + str(pourTime))
        GPIO.output(pin, GPIO.LOW)
        time.sleep(pourTime)
        GPIO.output(pin, GPIO.HIGH)

    def clean(self):
        cleanTime = 20
        pumpThreads = []
        for p in self.pump_configuration.keys():
            if self.pump_configuration[p]['value'] is not None:
                pump_thread = threading.Thread(target=self.pourDrink, args=(self.pump_configuration[p]['pin'], cleanTime))
                pumpThreads.append(pump_thread)

        for thread in pumpThreads:
            thread.start()

        for thread in pumpThreads:
            thread.join()

        time.sleep(2)

    def quit(self):
        GPIO.cleanup()
