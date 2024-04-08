import neopixel
import random
import board
import touchio
import time
#deck info from https://memory-alpha.fandom.com/wiki/Constitution_class_decks
#dests info from https://exoplanets.nasa.gov/news/1378/top-10-star-trek-destinations-chosen-by-nasa-scientists/
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

from prt import *
REPL = True
prt("Trek",REPL)
from wise import *


#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
paleblue = (0,0,1)
white = (20,20,20)
purple = (20,0,30)


colors = [pink,gold,blue,orange,green,red,paleblue,white,purple]

def docolor(color): #show a color  briefly
    for i in range(4):
        pixels[i] = color


    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank

    pixels.show()


def blinknum(num,color): #count out a number in a color
    for i in range(num):
        docolor(color)
        time.sleep(.1)


def compthink(): #blink out all the colors when computer "thinking"
    for i in range(random.randrange(3,5)):
        blinknum(1,random.choice(colors))



for i in range(file_len("decks")):
    dk = str(i+1)+": "+wisdom(i,"decks")
    dk = dk.rstrip()
    prt(dk,REPL)

def PickDest():
    dest = wisdom(random.randrange(file_len("dests")),"dests").rstrip()
    ETA = random.randrange(3,8)
    return (dest,ETA)


Deck = 0 # start at bridge
(dest,ETA) = PickDest()

prt (("Ship destination is: " +dest) ,REPL)
while True:
    prt (("You are on deck: "+ str(Deck + 1)+ " " + wisdom(Deck,"decks")).rstrip(),REPL)
    compthink()
    val = 0
    while val ==0:
        val = 0
        if touch1.value:
            val = val+1
        if touch2.value:
            val = val+2
    ETA = ETA - 1
    if ETA <= 0:
        prt("Arrived at "+dest,REPL)
        (dest,ETA)=PickDest()
        prt (("Ship new destination is: " +dest) ,REPL)


    if val == 1:
        Deck = Deck - 1
        if Deck < 0:
            Deck = 0
    if val == 2:
        Deck = Deck + 1
        if Deck > 22:
            Deck = 22
    if val == 3:
        Deck = random.randrange(file_len("decks"))
    time.sleep(.25)
