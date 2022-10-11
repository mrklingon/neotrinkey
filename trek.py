import time
import random
import board
import neopixel
import random
import touchio
from ncount import *
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices)
# we're americans :)
layout = KeyboardLayoutUS(kbd)

REPL = True

def prt(text):
    if REPL:
        print(text + "\n")
    else:
        layout.write(text + "\n")
    time.sleep(.25)    

none = 0
mode = none
nav = 1
dock = 2
attack = 3
scan = 4
score = 0

modes = [0,nav,dock,attack,scan]
mnames= ["", "nav", "dock", "attack", "scan"]


def starmap(map):
    enemies = int(map/10)
    stations = map - (enemies*10)
    prt("klingons: "+str(enemies))
    prt("stations: "+str(stations))
    ecount = 0
    statcount = 0
    ship = 0
    prt("score: "+str(score))
    for i in range(10):
        line = ""
        for j in range(10):
            if random.randrange(10)>8:
                if ecount < enemies:
                    ecount = ecount + 1
                    line = line + "K"
                else:
                    if statcount<stations:
                        line = line + "S"
                        statcount = statcount + 1
    
                    else:
                        if ship == 0:
                            line = line + "E"
                            ship = 1
                        else:
                            line = line + "."
            else:
                line = line + "."
        prt(line)
        

def show(node):
    y = int(node/3)
    x = node - (3*y)
    prt("x: " + str(x) + " y: "+str(y))
    
def quad(x,y): #turn x,y into quad index to cosmos
    return (x%3)+(3*(3%y))
power = 100
def mkquad():
    stations = random.randrange(3)
    enemies = random.randrange(5)
    quad = enemies * 10 + stations
    return quad
    
docolor(green)

cosmos = [0,0,0,0,0,0,0,0,0]

#create 3x3cosmos
for i in range(9):
    cosmos[i]=mkquad()


docolor(red)

Done = False

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

ind = 0
pixels.fill((0,0,50))
pixels.show()
docolor(red)
node = 4
x=2
y=2

docolor(green)
new = True
while not Done:
    val = 0
    
    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2
        
    if new:
        starmap(quad(x,y))
        new = False
        
    if val == 1:
        docolor(blue)
        mode = (mode + 1)%5
        prt("mode: " + str(mode) + " " + mnames[mode])
        time.sleep(.25)
        
    if val == 2:
        docolor(green)
        power =  power - 10
        time.sleep(.25)
        if mode == attack:
            prt("zap")
            docolor(red)
            scn = cosmos[node]
            score = score + int(scn/10)
            scn = scn -  (int(scn/10)*10)
            cosmos[node] = scn #enemies gone
            mode = none
        
        if mode == scan:
            docolor(green)
            prt("scan")
            starmap(cosmos[node])
            prt("power: " + str(power))
            mode = none
            
        if mode == dock:
            stations = cosmos[node]&3
            if stations > 0:
                docolor(red)
                docolor(blue)
                docolor(green)
                power = 100
                prt("docked")
            else:
                prt("no stations here!")
            mode = none
        
        if mode == nav:
            docolor(blue)
            node = random.randrange(9)
            prt("warp engaged!")
            show(cosmos[node])

        if power < 0:
            Done = True
    if val == 3:
        Done = True
        
prt("Game over! Score: "+str(score))



