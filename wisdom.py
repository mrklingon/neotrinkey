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

REPL = False

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

def wisdom(num,filename):
    global REPL
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    cmpthink()
    prt(quote,REPL)
    qs.close()
    return quote

lines = file_len("wisdom.txt")
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
        num = random.randrange(lines)
        quote = wisdom(num,"wisdom.txt")
    time.sleep(.1)

    if Val == 2:
        for q in range(2):
            num = random.randrange(lines)

            quote = wisdom(num,"wisdom.txt")
    Val = 0
    time.sleep(.1)
