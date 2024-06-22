import time
import random
import neopixel
import board
import touchio
from ncount import *
from prt import * 
REPL = True

grn = (0,20,0)
red = (20,0,0)
blue = (0,0,20)

blank = (0,0,0)

USize = 10
universe = []
newU = []
for i in range(USize*USize):
    universe.append(0)
    newU.append(0)
    
def randU():
    for i in range(USize*USize):
        if random.randrange(100)>60:
            universe[i]=1
        else:
            universe[i]=0
            
def cell(x,y):
    return (y*USize)+x

def xycell(cell):
    y = int(cell/10)
    x = cell - (y*10)
    return [x,y]

def showU():
    prt("==========",REPL)
    for y in range(USize):
        row = ""
        for x in range(USize):
            if universe[cell(x,y)]==1:
                row = row+"*"
            else:
                row = row + " "
        prt(row,REPL)

hood = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]

bar = [40,41,42,43,44,45,46,47,48,49] #bar
glider = [41,42,43,33,22]
rpent = [44,45,35,55,56]
def dopat(pat):
    for i in range(100):
        universe[i] = 0
    for i in pat:
        universe[i] = 1

def nbr(s):
    nc = 0
    for delta in hood:
        [x,y]=xycell(s)
        x=x+delta[0]
        y=y+delta[1]
        if x > 9:
            x=0
        if x < 0:
            x=9
        if y > 9:
            y=0
        if y < 0:
            y=9
        ss = cell(x,y)
        nc = nc + universe[ss]

    return nc

def gen():
    for i in range(USize*USize):
        nc = nbr(i)
        if nc < 2:
            newU[i]=0
        if nc == 2:
            newU[i]=universe[i]
        if nc == 3:
            newU[i]=1
        if nc > 3:
            newU[i]=0
    for i in range(USize*USize):
        universe[i]=newU[i]


def rungens(num):
    showU()
    for i in range (num):
        time.sleep(1)
        gen()
        showU()
    compthink()

compthink()
time.sleep(2)
for p in [bar,glider,rpent]:
    dopat(p)
    showU()
    rungens(10)
randU()
showU()
rungens(10)
compthink()


