import time
import random
import board
import neopixel
import random
import touchio



touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

white = 1
red = 2

def pixdef(color, intense):
    intense = (intense % 10) * (25)
    
    
    if color == white:
        return (intense,intense,intense)
    if color == red:
        return (intense,0,0)
    
    
def flight(color,intense):
    for i in range(4):
        pixels[i] = pixdef(color,intense)
        
    pixels.show()
bright = .1
color = white

flight(color,bright)

while True:
    Val = 0
    if touch1.value:
        Val = Val + 1
    if touch2.value:
        Val = Val + 2

        
    if Val == 1:
        bright = bright - 1
        if bright < .1:
            bright = .1
        time.sleep(.25)
            
                    
    if Val == 2:
        bright = bright + 1
        if bright > 9.1:
            bright = 9.1
        time.sleep(.25)    
    if Val == 3:
        bright = .1
        if color == white:
            color = red
        else:
            color = white
        time.sleep(.25)    
    flight(color,bright)
    
    
    