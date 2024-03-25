import neopixel
import random
import board
import touchio
import time
#deck info from https://memory-alpha.fandom.com/wiki/Constitution_class_decks

# set up touch for input
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


#set up pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

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
        time.sleep(.25)


def compthink(): #blink out all the colors when computer "thinking"
    for clr in colors:
        blinknum(1,clr)



for i in range(file_len("decks")):
    dk = str(i+1)+": "+wisdom(i,"decks")
    prt(dk,REPL)
    time.sleep(.25)

Deck = 0 # start at bridge

while True:
    prt ("You are on deck: "+ str(Deck + 1)+ " " + wisdom(Deck,"decks"),REPL)
    compthink()
    val = 0
    while val ==0:
        val = 0
        if touch1.value:
            val = val+1
        if touch2.value:
            val = val+2

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
