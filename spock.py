import time
import random
import neopixel
import board
import touchio
from prt import *

grn = (0,20,0)
red = (20,0,0)
blue = (0,0,20)
colors=[grn,red,blue]
blank = (0,0,0)

REPL = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


touched = time.monotonic()
Val = 0

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1
def cmpthink():
    for i in range(3):
        for j in range(4):
            pixels[j]=random.choice(colors)
            time.sleep(.1)
    time.sleep(.2)
    pixels.fill(blank)

def wisdom(filename):

    qs = open(filename)
    for i in range(random.randrange(file_len(filename))+1):
        quote = qs.readline()
        quote = quote.rstrip()
    cmpthink()
    qs.close()
    return (quote.rstrip())
cmpthink()
while True:
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    touched = time.monotonic()
    if Val == 1:
        story = wisdom("spock")
        prt (story,REPL)
    if Val == 2:
        story = wisdom("spock")
        prt (story,REPL)

    Val = 0
    if random.randrange(100)>89:
        cmpthink()
