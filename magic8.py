import time
import random
import neopixel
import board
import touchio


pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)


#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
colors = [pink, gold, blue, orange,green,red]

think = [[orange,blue,orange,blue],[blue,orange,blue,orange]]



def blinknum(num,color):
    for i in range(num):
        pixels.fill(color)
        time.sleep(.25)
    pixels.fill(blank)

def compthink():
        for t in range (2):
            for i in range(4):
                pixels[i] = think[t][i]
            time.sleep(.2)

responses = [
       "Yes, definitely.",
       "As I see it, yes.",
       "Reply hazy, try again.",
       "Cannot predict now.",
       "Do not count on it.",
       "My sources say no.",
       "Outlook not so good.",
       "Very doubtful."
   ]
rcolor = [green,green,gold,gold,gold,red,red]
# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
  # code
while True:
    val = 0
    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2

    if val == 0:
        compthink()
    else:
        x = random.randrange(7)
        print("Magic 8 Ball says:" + responses[x])
        blinknum(4,rcolor[x])
        pixels.fill(rcolor[x])
        val = 0
        while val == 0:
            if touch1.value:
                val = val + 1

            if touch2.value:
                val = val + 2

        time.sleep(2)


