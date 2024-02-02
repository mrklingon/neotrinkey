import time
import random
import neopixel
import board
import touchio
from microcontroller import nvm

period = [24, 62, 100, 188]
planets = ["Mercury", "Venus", "Earth", "Mars"]
pix = [(62, 0, 0), (64,60,7), (0, 62, 0), (36, 0, 37)]
loc = [0, 0 ,0,0]

if nvm[0] != 255:
    for x in range(4):
        loc[x] = nvm[x]
    
counter = [0,0,0,0]
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

def clearplanets(lcx):
    for i in range(4):
        pixels[i] = (0,0,0)
def showplanets(lcx):

    for p in range(4):
        pixels[loc[p]] = pix[p]

def mvplanet(planet):
    pixels[loc[planet]]=(0,0,0)
    loc[planet] = (loc[planet]+1)%4
    pixels[loc[planet]]=pix[planet]
    nvm[planet] = loc[planet]
    
locate = 2 # start at Earth

showplanets(loc)
while True:
    showplanets(loc)

    for p in range(4):
        counter[p] = counter[p]+1
        print (str(planets[p])+":"+str(counter[p])+":"+str(loc[p]))
        if counter[p]>period[p]:
            mvplanet(p)
            counter[p]=0

#    time.sleep(.01)

