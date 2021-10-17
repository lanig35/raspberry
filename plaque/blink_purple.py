#!/usr/bin/env python

import blinkt
import time
import numpy

COLOR_LIST = [[0, 127, 255], [0, 0, 255], [
    127, 0, 255], [255, 0, 255], [255, 0, 127]]
BRIGHTNESS_RANGE = numpy.arange(0, 0.5, 0.03)

blinkt.set_clear_on_exit()


def set_brightness(pixel, r, g, b, brightRange):
    for brightness in brightRange:
        blinkt.set_pixel(pixel, r, g, b, brightness)
        blinkt.show()
        time.sleep(0.01)


try:
    while True:
        for color in COLOR_LIST:
            for pixel in range(blinkt.NUM_PIXELS):
                set_brightness(
                    pixel, color[0], color[1], color[2], BRIGHTNESS_RANGE)
            for pixel in reversed(range(blinkt.NUM_PIXELS)):
                set_brightness(
                    pixel, color[0], color[1], color[2], reversed(BRIGHTNESS_RANGE))
except KeyboardInterrupt:
    pass
