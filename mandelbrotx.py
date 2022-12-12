# Renders the Mandelbrot Set in ASCII art. This version of the code
# runs with Python 3.
# Claire C.C., 2016
# With special thanks to Pi Delport for her help with optimizing.

ITOCHAR = {5:'@', 4:'O', 3:'*', 2:'.', 1:'`', 0:' '}

import time
from complex import *
from ncount import *
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import touchio

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

REPL = True

def prt(text):
    if REPL:
        print(text + "\n")
    else:
        keyboard_layout.write(text + "\n")
    time.sleep(.25)


colors = [pink, gold, blue, orange, green,red]
import random

def mandelbrotTest(c):
    ''''Tests to see if a point is is the mandelbrot set, and assigns it
    a character based on how quickly it escaped, if at all.'''

    Z = c
    i = 0

    while absC(Z) <= 2:
        if i > 500:
            break
        Z = plsC(c,sqrC(Z))
        i += 1

    return ITOCHAR[i // 100]




C = 73
R = 50
X = C - 1 if C % 2 == 0 else C    # Resolution. Should be an odd number.
Y = R - 1 if R % 2 == 0 else R

xMid = X // 2  # This represents the axes on a complex plane.
yMid = Y // 2

dx = 2 / xMid  # How much each cell represents in the context
dy = 2 / yMid  # of the complex plane.

Wait = True

blinknum(3,green)

while Wait:
    Val = 0

    if touch1.value:
        Val = Val + 1


    if touch2.value:
        Val = Val + 2

    if Val == 1:
        blinknum(4,red)

    if Val == 2:
        blinknum(4,green)
        Wait = False


for cd in range(4):
    binnum(cd,random.choice(colors))
    time.sleep(1)



for row in range(Y):
    binnum(row,random.choice(colors))
    rwt = ""
    for col in range(X):
        x, y = (-2 + dx * col), (2 - dy * row)
        c = [x, y]
        rwt = rwt + mandelbrotTest(c)
        prt(rwt)


