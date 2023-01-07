from morse import *
from prt import *

docode("trek")
REPL = True


def intpt(chars): #return one of a list
    Done = False
    blinknum(1,blue)
    ind = 0 #char to return
    prt(chars[ind]+"!",REPL)      

    while not Done:
        Val = 0
        if touch1.value:
            Val = Val + 1
        if touch2.value:
            Val = Val + 2

            
        if Val == 1:
            ind = ind +1
            if ind == len(chars):
                ind = 0
                blinknum(1,gold)
            blinknum(ind,green)
            prt(chars[ind]+"!",REPL)      
                        
        if Val == 2:
            Done = True
        time.sleep(.2)
        
    return (chars[ind])

def bridge():
  while True:
    prt("You are on the bridge.",REPL)
    prt("You can go out on the turbolift.\n>",REPL)
    a = intpt(["t"])
    if a == "t":
      turbo()
    else:
      prt("You can't go that way.",REPL)


def turbo():
  prt("You are in the turbolift",REPL)
  while True:
    prt("You can go to decks 1, 5, or 6.\n>",REPL)
    a=intpt(["1","5","6"])
    if a == "1":
      return
    elif a == "5":
      deck5()
    elif a == "6":
      deck6()
    else:
      prt("You can't go that way.",REPL)


def deck5():
  prt("You are on deck5",REPL)
  while True:
    prt("You can go to the mess, the chapel or the turbolift.\n>",REPL)
    a = intpt(["m","c","t"])
    if a == "t":
      return
    elif a == "c":
      chapel()
    elif a == "m":
      mess()
    else:
      prt("You can't go that way.",REPL)

def chapel():
    prt("nice chapel",REPL)

def mess():
    prt("yum!",REPL)

def deck6():
  prt("You are on deck6",REPL)
  while True:
    prt("You can go to Sickbay or seCurity or the turbolift.\n>",REPL)
    a=intpt(["s","c","t"])
    if a == "t":
      return
    elif a == "c":
      security()  
    elif a == "s":
      sickbay()   
    else:
      prt("You can't go that way.",REPL)
      
def security():
    prt("I feel safer already!",REPL)
    
def sickbay():
    prt("I feel better already!",REPL)
    
bridge()
