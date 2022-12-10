from morse import *

def kyber(crys):
    pixels.fill(blank)
    pixels[0] = crys
    pixels.show()
    
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

    if val == 1: #advance through messages touching "1"
        crystal = random.choice(colors)
        kyber(crystal)

        
    if val == 2: #display message in Morse when touching "2"
        pixels.fill(crystal)
        pixels.show()
    time.sleep(.25)