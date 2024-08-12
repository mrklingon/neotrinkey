import time
import random
import board
import neopixel
import random
import touchio
from ncount import * 

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

wait = 0
enter = 1
add = 2
subtract = 3
pop = 4

stack = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sp = 0

states = [wait,enter,add, subtract, pop]

state = wait

def enternum():
    quit = False
    nval = 0
    while not quit:
        value = 0
        binnum(nval,green)
        if touch1.value:
            value = value + 1 
        if touch2.value:
            value = value + 2
            
        if value == 1:
            quit = True
            
        if value == 2:
            nval = (nval + 1) % 16

    return nval

Done = False

while not Done:
    val = 0
    if touch1.value:
        val = val + 1
    if touch2.value:
        val = val + 2
    
    if val == 1:
        state = state + 1
        if state > pop:
            state = wait
        
        binnum(state,gold)
        docolor(blank)
    
    if val == 2 and state == enter:
        inp = enternum()
        stack[sp] = inp
        sp = sp + 1
        state = wait

    if val == 3:
        Done = True
        
            
        
        