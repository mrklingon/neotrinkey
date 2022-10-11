import time
import random
import board
import neopixel
import random
import touchio
from ncount import * 

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

ship = (25,0,40)

pos = 0

orbit = [1,2,4,8]
planet = 3

plnt = ["sun","mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto"]

def showship(place):
    binnum(orbit[place],ship)
    
    
    
while True:
    Val = 0
    showship(pos)
    time.sleep(planet/10.0)
    pos = (pos + 1)% 4
    
    if touch1.value:
        Val = Val + 1
        
    if touch2.value:
        Val = Val + 2
        
    if Val == 2:
        docolor(blue)
        planet = planet + 1
        if planet > 9:
            planet = 9
        print("planet :" + plnt[planet])
    if Val == 1:
        docolor(gold)
        planet = planet -1 
        if planet < 1:
            planet = 1
        print("planet :" + plnt[planet])
    if Val == 3:
        docolor(green)
        if (planet <4):
            planet = 1
        else:
            planet = 9
            
        print("BOOM! planet :" + plnt[planet])
    