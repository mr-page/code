import speech

# Imports go at the top
while True:
    while True:
        if button_a.get_presses():
            for x in range(5):
                for y in range(5):
                    for z in range(10):
                        display.set_pixel(x,y,z)
            break
        if button_b.get_presses():
            speech.say('never give you up')
            speech.say('never give you up')
            speech.say('never give you up')
            speech.say('never give you up')
            break
        display.clear()
