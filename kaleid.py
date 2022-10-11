import time
import board
import random
import touchio
import neopixel

from ncount import *


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

white = (20,20,20)
purple = (20,0,30)

colors = [pink,gold,blue,orange,green,red,paleblue,white,purple]


def kleid(cycles):
    for i in range(cycles):
        pixels[random.randrange(4)] = random.choice(colors)
        pixels.show()
        time.sleep(.15)

def kounter(color):
    for i in range(16):
        binnum(i,color)
        time.sleep(.15)

kleid(10)
blinknum(1,blue)
while True:
    val = 0
    
    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1:
        kleid(10+random.randrange(30))

    if val == 2:
        kounter(random.choice(colors))

    time.sleep(.25)
