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
    score = score + 1
    blinknum(score,gold)
    print("Boom!")
    if score == 5:
        print ("Success!!")
        compthink()
        blinknum(1,blank)
        score = 0
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
        pixels[2]= red
        pixels.show()
        time.sleep(.2)
        if pixels[3] == green:
            boom()
        else:
            print("miss!")
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
        pixels[1]=blank
        pixels.show()
    Val = 0
    clear()

