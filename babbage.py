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
compthink() #blink some lights to show we started
stack = [0,0,0,0,0,0,0,0]  #bigger than needed
sp = 0

states = [wait,enter,add, subtract, pop]
nstates = ["wait", "enter","add","subtract","pop"] #name of states
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
        print ("val: " + str(nval))

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
        print ("current state: " + nstates[state])
        binnum(state,gold)
        docolor(blank)

    if val == 2 and state == enter:
        inp = enternum()
        stack.insert(0,inp)
        binnum(inp,blue)

    if val == 2 and state == add:
        v1 = stack.pop(0)
        v2 = stack.pop(0)

        ans = (v1 + v2)%16
        print ("adding " + str(v1) +" + "+str(v2) + " = " + str(ans))
        binnum(ans,blue)
        stack.insert(0,ans)


    if val == 2 and state == subtract:
        v1 = stack.pop(0)
        v2 = stack.pop(0)

        ans = v2 - v1
        if ans < 0:
            ans = ans +16 #clock arithmetic

        print ("subtracting " + str(v2) +" - "+str(v1) + " = " + str(ans))
        binnum(ans,blue)
        stack.insert(0,ans)

    if val == 2 and state == pop:
        v1 = stack.pop(0)
        print ("Popping off stack: "+ str(v1))
        binnum(v1,blue)


    time.sleep(.2)

