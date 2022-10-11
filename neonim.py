import time
import random
import board
import neopixel
import random
import touchio
from ncount import * 

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

brain = [1,2,1,2,1,2,1,1,2,1] #computer moves

def dohum():
    pixels[0] = blue
    pixels[1] = green 
    pixels[2] = blue
    pixels[3] = green
    pixels.show()
    time.sleep(.5)
    docolor(blank)
    
def docomp():
    pixels[0] = red
    pixels[1] = gold
    pixels[2] = blue
    pixels[3] = orange
    pixels.show()
    time.sleep(.5)
    docolor(blank)


dohum()
time.sleep(.5)
docomp()
time.sleep(.5)

blinknum(5,blue)

for z in range(11):
    binnum(z,green)
    
time.sleep(.75)
docolor(blank)

computer = 1
human = 2

states = [computer, human]


while True:
    touched = time.monotonic()
    Val = 0

    state = states[random.randrange(2)]
    total = 0
    if state == human:
        dohum()
        print ("human first")
    else:
        docomp()
        print ("computer first")
        
    while total < 10:

        if state == computer: #computer turn
            
            binnum(total,orange)
            docolor(blank)
            docomp()
            move = brain[total]
            print ("computer move:"+str(move))
            binnum(move,green)
            
            total = total + move
            binnum(total,orange)
            state = human
            
            if total == 10: #computer win
                docomp()
                print("computer won")
                binnum(total,green)
                
                
        else: #humnan turn
            move = 0
            Val = 0
            
            if touch1.value:

                Val = Val +1
                touched = time.monotonic()
            if touch2.value:
                Val = Val +2
                touched = time.monotonic()
                   
            if Val == 1: #move 1
                move = 1
                dohum()
                binnum(move,blue)
                total = total + move
                print ("human move:"+str(move))
                binnum(total,orange)
                state = computer
            
            if Val == 2: #move 1
                move = 2
                dohum()
                binnum(move,blue)
                total = total + move
                print ("human move:"+str(move))
                binnum(total,orange)
                state = computer
            if total == 10: #human win    
                dohum()
                binnum(total,blue)
                print("human won")
                
    time.sleep(5)
    print ("restart")
        
