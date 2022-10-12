
import time
import random
import board
import neopixel
import random 
import touchio
from _pixelbuf import colorwheel

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)


grn = (0,20,0)
red = (20,0,0)
ps = (20,20,0)

dc = (0,0,40)
dtc= (0,40,0)
blank = (0,0,0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

def getTrek():
    trekq = open("trekquotes")
    for i in range(random.randrange(40)):
        quote = trekq.readline()
    print(quote)
    trekq.close()
    return quote


def getGFFA():
    gffaq = open("yoda-quotes")
    for i in range(random.randrange(50)):
        quote = gffaq.readline()
    print(quote)
    gffaq.close()
    return quote


def green():
    
    
    pixels[0] = grn
    pixels[1]=  grn
    pixels[2] = grn
    pixels[3] = grn
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()
def doRed():
    
    
    pixels[0] = red
    pixels[1]=  red
    pixels[2] = red
    pixels[3] = red
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()

def pause():
    
    pixels[0] = ps
    
    pixels.show()
    time.sleep(.05)
    pixels[3] = blank
    pixels.show()

#dot
def dot():
   pixels[0] = blank
   pixels[1]= blank
   pixels[2] = blank
   

   pixels[3] = dtc
   pixels.show()
   time.sleep(.25)
    
   pixels[3] = blank
   pixels.show()
   time.sleep(.25)
    
#dash
def dash():

   pixels[0] = blank
   pixels[1]= blank

   pixels[2] = dc
   pixels[3]= dc
   pixels.show()
   time.sleep(.5)
   
   pixels[2] = blank
   pixels[3]= blank
   time.sleep(.25)
   pixels.show()

def blinkcode(code):
    for chr in code:
        if (chr == "-"):
            dash()
        if (chr =="."):
            dot()
        else:
            pause()
            time.sleep(.25)

V = 0


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


touched = time.monotonic()
Val = 0

while True:

    
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()
    
    time.sleep(.5)
    touched = time.monotonic()


    if Val == 1:
        green()
        txt = getTrek()

        print (txt)
        keyboard_layout.write(txt + "\n")  # Then send string.

    if Val == 2:
        doRed()
        txt = getGFFA()

        print (txt)
        keyboard_layout.write(txt + "\n")  # Then send string.

    Val = 0

