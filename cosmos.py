import time
import random
import board
import neopixel
import random
import touchio
from ncount import * 

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8) 
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)

rbow = [blank,red,pink,orange,gold,green,blue]
cosmos = []
cosdiam = 40
vectors = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
dr = 0

xpos = 0
ypos = 0 

def initcosmos():
    for i in range(cosdiam*cosdiam):
        if random.randrange(12) >7 :
            cosmos.append(random.randrange(6)+1)
        else:
            cosmos.append(0)

def recosmos():
    for i in range(cosdiam*cosdiam):
        if random.randrange(12) >7 :
            cosmos[i] = random.randrange(6)+1
        else:
            cosmos[i] = 0

def voyage():
    for i in range(96):
        pix(cosmos[i],cosmos[i+1],cosmos[i+2],cosmos[i+3])
        time.sleep(.25)

def vpic(x,y):
    return cosmos[x%cosdiam + ((y%cosdiam)*cosdiam)]

def showpane(x,y):
    pix(vpic(x,y),vpic(x+1,y),vpic(x+1,y+1),vpic(x,y+1))
        

def pix(p0,p1,p2,p3):
    pixels[0] = rbow[p0]
    pixels[1] = rbow[p1]
    pixels[2] = rbow[p2]
    pixels[3] = rbow[p3]
    pixels.show()
  
def visit():
    for ay in range(cosdiam):
        for ax in range(cosdiam):
            showpane(ax,ay)
            time.sleep(.25)
def move(dr):
    global xpos
    global ypos

    print(str(xpos) + ", " +str(ypos))
    xpos = (xpos + vectors[dr][0]) % cosdiam
    ypos = (ypos + vectors[dr][1]) % cosdiam
    print(str(xpos) + ", " +str(ypos))
    showpane(xpos,ypos)

def chgdir():
    global dr
    dr = (dr+1)%8


initcosmos()

quit = 0 
showpane(0,0)
while quit == 0:
    value = 0
    if touch1.value:
        value += 1
    
    if touch2.value:
        value +=2
        
    if value == 1:
        docolor(green)
        chgdir()
        binnum(dr,green)
        binnum(xpos,blue)
        binnum(ypos,red)
        showpane(xpos,ypos)
        
    if value ==2:
        for m in range(7):
            move(dr)
            time.sleep(.25)
        
    if value ==3:
        binnum(1,green)
        binnum(1,red)
        voyage()
        
    
