import time
import random
import neopixel
import board
import touchio
from morse import *
REPL = True
place = [3,0]
score = 0

def ship(loc):
    pixels[loc]=green
    pixels.show()
    time.sleep(.14)

def clear():
    for p in place:
        pixels[p] = blank
    pixels.show

touched = time.monotonic()
Val = 0

def boom():
    global score
    global missles
    global misses
    score = score + 1
    blinknum(score,gold)
    print("Boom!")
    if score == 5:
        print ("Success!!")
        compthink()
        blinknum(1,blank)
        score = 0
        missles = 5 + random.randrange(6)
        misses = 0

missles = 7
misses = 0

while True:

    ship(place[random.randrange(2)])
    
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    if Val == 1:
        missles = missles - 1
        pixels[2]= red
        pixels.show()
        time.sleep(.2)
        if pixels[3] == green:
            boom()
        else:
            print("miss!")
            misses = misses + 1
            blinknum(misses,paleblue)
        pixels[2]=blank
        pixels.show()
    if Val == 2: 
        pixels[1]=red
        pixels.show()
        time.sleep(.2)
        if pixels[0] == green:
            boom()
        else:
            print("miss!")
            misses = misses + 1
            blinknum(misses,paleblue)
        pixels[1]=blank
        pixels.show()
    Val = 0
    if missles <= 0 or misses >= 5:
        print("you lost!")
        blinknum(score,gold)
        score = 0
        misses = 0
        missles = 5 + random.randrange(6)
        
    clear()

