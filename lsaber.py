from morse import *

def kyber(crys):
    pixels.fill(blank)
    pixels[0] = crys
    pixels.show()

lit = False

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
docode("hello") #say hello
crystal = blue

while not Done:
    val = 0

    if touch1.value: 
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 1: #random crystal
        if lit:
            douse()
        crystal = random.choice(colors)
        kyber(crystal)
        lit = False
        
    if val == 2: #ignite/douse
        if lit:
            douse()
            lit=False
        else:
            ignite(crystal)
            lit=True
    time.sleep(.25)