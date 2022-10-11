
import time
import random
import board
import neopixel
import random
import touchio
from _pixelbuf import colorwheel

grn = (0,20,0)
red = (20,0,0)
ps = (20,20,0)

dc = (0,0,40)
dtc= (0,40,0)
blank = (0,0,0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)

j316 = "for god so loved the world"
P23 = "the lord is my shepherd"
Phl4 = "i can do all things"
Isaiah263 = "thou wilt keep him in perfect peace"
TTim316 = "all scripture is given by inspiration of god"
Gen11 = "in the beginning god created the heaven and the earth"
TPt = "casting all your care upon him"
I41 = "fear thou not for i am with thee"
Verses = [Phl4, P23, j316, Isaiah263, TTim316,Gen11, TPt, I41 ]

Vname =  ["Phl4", "P23", "j316", "Isaiah263", "TTim316", "Gen11", "1Pt", "I41"]


# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ',':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + '  '
      else:
         my_cipher += ' '
         
   return my_cipher

def green():
    
    
    pixels[0] = grn
    pixels[1]=  grn
    pixels[2] = grn
    pixels[3] = grn
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()
def doRed():
    
    
    pixels[0] = red
    pixels[1]=  red
    pixels[2] = red
    pixels[3] = red
    
    pixels.show()
    time.sleep(.25)

    pixels[0] = blank
    pixels[1]= blank
    pixels[2] = blank
    pixels[3] = blank
    pixels.show()

def pause():
    
    pixels[0] = ps
    
    pixels.show()
    time.sleep(.05)
    pixels[3] = blank
    pixels.show()

#dot
def dot():
   pixels[0] = blank
   pixels[1]= blank
   pixels[2] = blank
   

   pixels[3] = dtc
   pixels.show()
   time.sleep(.25)
    
   pixels[3] = blank
   pixels.show()
   time.sleep(.25)
    
#dash
def dash():

   pixels[0] = blank
   pixels[1]= blank

   pixels[2] = dc
   pixels[3]= dc
   pixels.show()
   time.sleep(.5)
   
   pixels[2] = blank
   pixels[3]= blank
   time.sleep(.25)
   pixels.show()

def blinkcode(code):
    for chr in code:
        if (chr == "-"):
            dash()
        if (chr =="."):
            dot()
        else:
            pause()
            time.sleep(.25)

V = 0


touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


touched = time.monotonic()
Val = 0

while True:

    
    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()
    
    time.sleep(.5)
    touched = time.monotonic()


    if Val == 1:
        green()
        txt = Verses[V]
        V = V +1
        if V > 7:
            V = 0

        print (encryption(txt.upper()))
        blinkcode(encryption(txt.upper()))

    if Val == 2:
        doRed()
        txt = Vname[V]

        print (encryption(txt.upper()))
        blinkcode(encryption(txt.upper()))

    Val = 0