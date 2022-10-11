
import time
import random
import board
import neopixel
import random
import touchio


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

#Define colors
pink = (42, 40, 42)
gold = (50, 40, 5)
blue = (5, 25, 25)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)

#define states
live = 0  #slowly eats, loses happiness
food = 1  #feed state
play = 2  #play state

states = [live, food, play]

state = live

hunger = 100
played = 100

allcolors = [red,grn,blue,gold,pink,orange,blank]

#health is average of happiness and hunger
def health(fd,py):
    return ((fd + py) /2)

#display current state
def showState(fd,py):
    pixels[0] = (0,fd/2,0)
    pixels[1] = (0,0,py/2)
    pixels[2] = (0,health(fd,py)/2,health(fd,py)/2)
    pixels[3] = (0,health(fd,py)/2,health(fd,py)/2)
    pixels.show()

#show color
def docolor(color):
    for i in range(4):
        pixels[i] = color
    
    
    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank
   
    pixels.show()    



scolor = [pink, green, blue]

def health(fd,py):
    return ((fd + py) /2)

def showState(fd,py):
    pixels[0] = (0,fd/2,0)
    pixels[1] = (0,0,py/2)
    pixels[2] = (0,health(fd,py)/2,health(fd,py)/2)
    pixels[3] = (0,health(fd,py)/2,health(fd,py)/2)
    pixels.show()

def docolor(color):
    for i in range(4):
        pixels[i] = color
    
    
    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank
   
    pixels.show()    
                    

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

touched = time.monotonic()
Val = 0

for clr in allcolors:
    docolor(clr)

while True:

    while health(hunger,played)>0:
        if time.monotonic() - touched < 0.15:
            continue
        if touch1.value:

            Val = Val +1
            touched = time.monotonic()
        if touch2.value:
            Val = Val +2
            touched = time.monotonic()
        
        if Val == 1:
            state = state + 1
            if state > play:
                state = live
            
            docolor(scolor[state])
            touched = time.monotonic()
            Val = 0 



        if Val == 2:
            docolor(scolor[state])
            touched = time.monotonic()
            if state == food:
                hunger = hunger + 1 + random.randrange(20)
            if state == play:
                played = played + 1 + random.randrange(20)
            Val = 0
    
        if state == live:
            showState(hunger,played)
            played = played - random.randrange(5)
            hunger = hunger - random.randrange(5)
            print ("health " + str(health(hunger,played)))
            time.sleep(.5)

### all done
        
    for clr in allcolors:
        docolor(clr)
    
    waiting = 1
    while waiting == 1:
        if touch1.value or touch2.value:
            waiting = 0
            hunger = 50 + random.randrange(100)
            played = 50 + random.randrange(100)
            
    for clr in allcolors:
        docolor(clr)