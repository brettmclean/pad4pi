#!/usr/bin/python

from pad4pi import rpi_gpio
import time

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_4_by_3_keypad() # makes assumptions about keypad layout and GPIO pin numbers

def printKey(key):
	print(key)

keypad.registerKeyPressHandler(printKey)

try:
	print("Press buttons on your keypad. Ctrl+C to exit.")
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("Goodbye")
finally:
	keypad.cleanup()
