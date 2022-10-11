import random
import touchio
import board
import time
from words import *

import neopixel

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


touched = time.monotonic()

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

red = (20,0,0)
green = (0,20,0)

blue = (0,0,20)

blank = (0,0,0)

colors = [red,green,blue]

def dcode():
    codew = ""
    for i in range(6):
        codew = codew + " " + dwords[random.randrange(len(dwords))]
    return (codew)

pixels[0] = blank
pixels[1] = blank
pixels[2] = blank
pixels[3] = blank
pixels.show()

def doColor (color):
    pixels[0] = blank
    pixels[1] = blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()
    
    for i in range(4):
        pixels[i] = color
        pixels.show()
        time.sleep(.2)
    time.sleep(.5)        
    pixels[0] = blank
    pixels[1] = blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()
    

def doMix ():
    pixels[0] = red
    pixels[1] = green
    pixels[2] = blue
    pixels[3] = red
    pixels.show()
    
    time.sleep(.5)        
    pixels[0] = blank
    pixels[1] = blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()

doColor(red)
doColor(green)
doColor(blue)

code = "not yet"

while True:
    
    Val = 0
    
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:
        Val = 1
        touched = time.monotonic()


    if touch2.value:
        Val = 2
        touched = time.monotonic()


    if Val == 1:
        doColor(colors[random.randrange(3)])
        code = dcode()
        print (code)
        keyboard_layout.write(code + "\n")  # Then send string.

    if Val == 2:
        doMix()
        print (code)
        keyboard_layout.write(code + "\n")  # Then send string.
