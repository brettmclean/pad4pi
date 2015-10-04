#!/usr/bin/python

import RPi.GPIO as GPIO
import time

DEFAULT_KEY_DELAY = 300

class KeypadFactory():

	def create_keypad(self, keypad=None, row_pins=None, col_pins=None, key_delay=DEFAULT_KEY_DELAY):

		if keypad is None:
			keypad = [
				[1,2,3],
				[4,5,6],
				[7,8,9],
				["*",0,"#"]
			]

		if row_pins is None:
			row_pins = [4,14,15,17]

		if col_pins is None:
			col_pins = [18,27,22]

		return Keypad(keypad, row_pins, col_pins, key_delay)

	def create_4_by_3_keypad(self):

		KEYPAD = [
			[1,2,3],
			[4,5,6],
			[7,8,9],
			["*",0,"#"]
		]

		ROW_PINS = [4,14,15,17]
		COL_PINS = [18,27,22]

		return self.create_keypad(KEYPAD, ROW_PINS, COL_PINS)

	def create_4_by_4_keypad(self):

		KEYPAD = [
			[1,2,3,"A"],
			[4,5,6,"B"],
			[7,8,9,"C"],
			["*",0,"#","D"]
		]

		ROW_PINS = [4,14,15,17]
		COL_PINS = [18,27,22,23]

		return self.create_keypad(KEYPAD, ROW_PINS, COL_PINS)

class Keypad():
	def __init__(self, keypad, row_pins, col_pins, key_delay=DEFAULT_KEY_DELAY):
		self._handlers = []

		self._keypad = keypad
		self._row_pins = row_pins
		self._col_pins = col_pins
		self._key_delay = key_delay

		self._last_key_press_time = 0

		GPIO.setmode(GPIO.BCM)

		self._setRowsAsInput()
		self._setColumnsAsOutput()

	def registerKeyPressHandler(self, handler):
		self._handlers.append(handler)

	def unregisterKeyPressHandler(self, handler):
		self._handlers.remove(handler)

	def clearKeyPressHandlers(self):
		self._handlers = []

	def _onKeyPress(self, channel):
		currTime = self.getTimeInMillis()
		if currTime < self._last_key_press_time + self._key_delay:
			return

		keyPressed = self.getKey()
		if keyPressed is not None:
			for handler in self._handlers:
				handler(keyPressed)
			self._last_key_press_time = currTime

	def _setRowsAsInput(self):
		# Set all rows as input
		for i in range(len(self._row_pins)):
			GPIO.setup(self._row_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.add_event_detect(self._row_pins[i], GPIO.FALLING, callback=self._onKeyPress, bouncetime=self._key_delay)

	def _setColumnsAsOutput(self):
		# Set all columns as output low
		for j in range(len(self._col_pins)):
			GPIO.setup(self._col_pins[j], GPIO.OUT)
			GPIO.output(self._col_pins[j], GPIO.LOW)

	def getKey(self):

		keyVal = None

		# Scan rows for pressed key
		rowVal = None
		for i in range(len(self._row_pins)):
			tmpRead = GPIO.input(self._row_pins[i])
			if tmpRead == 0:
				rowVal = i
				break

		# Scan columns for pressed key
		colVal = None
		if rowVal is not None:
			for i in range(len(self._col_pins)):
				GPIO.output(self._col_pins[i], GPIO.HIGH)
				if GPIO.input(self._row_pins[rowVal]) == GPIO.HIGH:
					colVal = i
				GPIO.output(self._col_pins[i], GPIO.LOW)

		# Determine pressed key, if any
		if colVal is not None:
			keyVal = self._keypad[rowVal][colVal]

		return keyVal

	def cleanup(self):
		GPIO.cleanup()

	def getTimeInMillis(self):
		return time.time() * 1000
