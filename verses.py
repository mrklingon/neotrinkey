
import time
import random
import board
import neopixel
import random
import touchio
from _pixelbuf import colorwheel


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
            time.sleep(.25)

V = 0
while True:
    txt = Verses[V]
    V = V +1
    if V > 7:
        V = 0

    print (encryption(txt.upper()))
    blinkcode(encryption(txt.upper()))

