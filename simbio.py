import time
import random
import neopixel
import board
import touchio
# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
#Define colors
pink = (20,5,5)
gold = (25, 20, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
white = (20,20,20)
violet = (20,0,20)

colors = [red,orange,pink,blank,green,blue,violet]
#set up pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

Psym = ["@","o","."," ","'",":","#"]
cosmos = []
c1 = []
c2 = []

for i in range(301):
    cosmos.append(0)
    c1.append(0)
    c2.append(0)

def create():
    global cosmos
    for x in range(300):
        cosmos[x] = random.randrange(-3,3)



def display():
    for i in range(4):
        cell = i + 40
        pixels[i] = colors[cosmos[cell]+3]

def pcosmos():
    global cosmos
    pic = ""

    for i in range(10,70):
        pic = pic + Psym[3+cosmos[i]]

    print (pic)


def checkWorld():
    global cosmos

    for i in (cosmos):
        if i != 0:
            return True

    return False

def doGen():
    global cosmos, c1, c2

    for i in range(300):
        c1[i]=0
        c2[i]=0

    for i in range(300):
        v = cosmos[i]
        if (v+i)>=0 and (v+i)<= 300:
            c1[v+i] = v
            n=v+i
            if cosmos[n] != 0:
                if (n+v) >=0 and (n+v)<=300:
                    c2[n+v] = cosmos[n]
    for i in range(300):
        cosmos[i]=0
    for i in range(300):
        if (c1[i]!=0):
            cosmos[i]= c1[i]

    for   i in range(300):
        if (c2[i]!=0):
            cosmos[i]= c2[i]

create()
droid = False
pcosmos
display
touched = time.monotonic()

while True:
    Val = 0
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    display()
    if Val == 1:
        if droid:
            droid=False
        else:
            droid = True
#       print(cosmos)
        pcosmos()


    if Val == 2:
        create()
        #print(cosmos)
        pcosmos()


    if checkWorld() == False:
        pixels.fill(white)
        time.sleep(2)
        create()
    if droid:
        doGen()
        #print(cosmos)
        pcosmos()
        time.sleep(.1)

    time.sleep(.2)
