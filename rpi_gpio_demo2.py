#!/usr/bin/python

from pad4pi import rpi_gpio
import time
import sys

entered_passcode = ""
correct_passcode = "1234"

def cleanup():
    global keypad
    keypad.cleanup()

def correct_passcode_entered():
    print("Passcode accepted. Access granted.")
    cleanup()
    sys.exit()

def incorrect_passcode_entered():
    print("Incorrect passcode. Access denied.")
    cleanup()
    sys.exit()

def digit_entered(key):
    global entered_passcode, correct_passcode

    entered_passcode += str(key)
    print(entered_passcode)

    if len(entered_passcode) == len(correct_passcode):
        if entered_passcode == correct_passcode:
            correct_passcode_entered()
        else:
            incorrect_passcode_entered()

def non_digit_entered(key):
    global entered_passcode

    if key == "*" and len(entered_passcode) > 0:
        entered_passcode = entered_passcode[:-1]
        print(entered_passcode)

def key_pressed(key):
    try:
        int_key = int(key)
        if int_key >= 0 and int_key <= 9:
            digit_entered(key)
    except ValueError:
        non_digit_entered(key)

try:
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_4_by_3_keypad() # makes assumptions about keypad layout and GPIO pin numbers

    keypad.registerKeyPressHandler(key_pressed)

    print("Enter your passcode (hint: {0}).".format(correct_passcode))
    print("Press * to clear previous digit.")

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Goodbye")
finally:
    cleanup()
