import time
import random
import neopixel
import board
import touchio
from ncount import *


blank = (0,0,0)

white = (10,10,10)
red = (10,0,0)
green = (0,10,0)
blue = (0,0,10)

def blink(color,sec):
    pixels.fill(color)
    time.sleep(sec)
    pixels.fill(blank)

def hourN(secs):
    h = int(secs/3600)
    return h

def minN(secs):
    min = int((secs - (hourN(secs)*3600))/60)
    return min
    
hour = int(input("hour:? "))
minute = int(input("minute?: "))

seconds =  ((hour*60)+minute)*60

moment = int(time.monotonic())

print (hour,minute)

while True:
    s = seconds +(int(time.monotonic())-moment)
    print(hourN(s))
    blinknum(hourN(s),orange)
    print(minN(s))
    blinknum(minN(s),red)
    print (time.monotonic())
    blink(red,1)
    print (time.monotonic())
    blink(green,10)
    print (time.monotonic())
    blink(blue,30)
