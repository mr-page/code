from microbit import *
if button_a.is_pressed():
    display.show(Image.YES)
elif button_b.is_pressed():
    display.show(Image.NO)
else:
    display.show(Image.ASLEEP)
