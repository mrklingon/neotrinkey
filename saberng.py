from morse import *

def kyber(crys):
    pixels.fill(blank)
    pixels[0] = crys
    pixels.show()

lit = False

fonts = [blank,red,orange,green,blue]
FONT = ["","May the force be with you","do or do not","there is no try","I can do all things"]
shown = False
fnum = 0
def ignite(crys):
    pixels.fill(blank)
    for i in range(4):
        pixels[i] = crys
        pixels.show()
        time.sleep(.25)
        
def douse():
    for i in range(4):
        pixels[3-i] = blank
        pixels.show()
        time.sleep(.25)


Done  = False

count = 0
compthink() #computer thinking
docode(FONT[4]) #say I can do all things
crystal = blue

while not Done:
    val = 0

    if touch1.value: 
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1: #random crystal
        if lit:
            fnum = fnum+1
            if fnum>4:
                fnum=0
            oldpix = pixels[0]
            pixels[0] = fonts[fnum]
            pixels.show()
            time.sleep(.5)
            pixels[0]=oldpix
            pixels.show()
            shown=False
            
        else:
            crystal = random.choice(colors)
            kyber(crystal)
        
    if val == 2: #ignite/douse
        if lit:
            douse()
            lit=False
        else:
            if not shown:
                docode(FONT[fnum])
                shown=True
            ignite(crystal)
            lit=True
    time.sleep(.25)
