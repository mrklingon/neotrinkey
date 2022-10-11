
import time
import random
import board
import neopixel
import random
import touchio


from morse import *

repl = False
prt = True

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
tree =(0,51,8)


setting = ["grass", "forest", "desert", "sea", "castle"]
setcolor = [green, tree, orange, blue, gold]

def flcolor(color):
    pixels.fill(color)
    pixels.show()


def docolor(color):
    for i in range(4):
        pixels[i] = color

    
    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank
   
    pixels.show()    


cosmos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(33):
    cosmos[i] = random.randrange(1,5)
    
def msg(text):
    if repl:
        if prt:
            print(text)
        else:
            docode(text)
    else:
        typemsg(text[0])
        blinkcode(encryption(text[0].upper()))
node = 1

def curnode():
    global node
    return(node)

def leftnode():
    global node
    nd = node
    node = node * 2
    if node > 32:
        node = nd
    return (node)

def rtnode():
    global node
    nd = node
    node = (1+ (node * 2))
    if node > 32:
        node = nd
    return (node)

def upnode():
    global node
    nd = node
    node = int(node/2)
    if node < 1:
        node = 1
    return (node)

def shownode(node):
    msg(setting[cosmos[node]])
    docolor(setcolor[cosmos[node]])
    
shownode(node)

while True:
    oldnode = node
    Val = 0
    if touch1.value:
        Val = Val + 1

    if touch2.value:
        Val = Val + 2
        
    if Val == 1:
        leftnode()
    if Val == 2:
        rtnode()
    if Val == 3:
        upnode()
    
    if node < 1:
        node = 1
    if node > 32:
        node = 1

    if node != oldnode:
        msg(setting[cosmos[node]])
        shownode(node)
    else:
        flcolor(setcolor[cosmos[node]])    
