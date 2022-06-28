import random

import microbit
from microbit import *

# Imports go at the top
while True:
    while True:
        if button_a.get_presses():
            for x in range(5):
                for y in range(5):
                    for z in range(10):
                        display.set_pixel(x, y, z)
            break  # break out of the inner loop
        if button_b.get_presses():
            display.scroll('never give you up', wait=False, loop=True)
            if button_a.is_pressed():
                break  # break out of the outer loop
        display.clear()
    if button_a.is_pressed():
        if button_b.is_pressed():
            microbit.panic(random.randint(0, 255))
