pad4pi
======

An interrupt-based Python 2/3 library for reading matrix_ keypad_ key presses using Raspberry Pi GPIO pins.

.. _matrix: http://www.adafruit.com/products/419
.. _keypad: http://www.adafruit.com/products/1824

.. code-block:: python

	pip install pad4pi

Tested on a Raspberry Pi B+ using a `4x3 matrix keypad`_ but it should work with 4x4 and other sizes.

.. _4x3 matrix keypad: http://www.adafruit.com/products/419

Usage
=====

.. code-block:: python

  from pad4pi import rpi_gpio

  KEYPAD = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      ["*", 0, "#"]
  ]

  ROW_PINS = [4, 14, 15, 17] # BCM numbering
  COL_PINS = [18, 27, 22] # BCM numbering

  factory = rpi_gpio.KeypadFactory()

  # Try factory.create_4_by_3_keypad 
  # and factory.create_4_by_4_keypad for reasonable defaults
  keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

  def printKey(key):
      print(key)

  # printKey will be called each time a keypad button is pressed
  keypad.registerKeyPressHandler(printKey)

When your program exits, call ``keypad.cleanup()`` to ensure the Raspberry Pi's GPIO pins are reset.

License
=======

Licensed under `GNU Lesser General Public License Version 3`_ (LGPL v3).

.. _GNU Lesser General Public License Version 3: https://github.com/brettmclean/pad4pi/blob/master/LICENSE
