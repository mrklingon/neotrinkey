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
    prt("You can go to decks 1, 5, 7, or 13.\n>",REPL)
    a=intpt(["1","6","7","13"])
    if a == "1":
      return
    elif a == "7":
      deck7()
    elif a == "6":
      deck6()
    elif a == "13":
      deck13()
    else:
      prt("You can't go that way.",REPL)


def deck6():
  prt("You are on deck6",REPL)
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
    prt("You are in the Chapel",REPL)
    while True:
        prt("You can open the Bible, Sit in a pew, Kneel or eXit\n>",REPL)
        a = intpt(["b","s","k","x"])
        if a == "x":
          return
        elif a == "b":
            verses= ["The LORD is my shepherd....","I can do all things through Christ...","Thou wilt keep him in pefect peace..."]
            prt(random.choice(verses),REPL)
            compthink()
                
        elif a == "s":
            prt("You sit and meditate. ",REPL)
            compthink()
        elif a == "k":
            prt("You kneel and pray. ",REPL)
            compthink()
        else:
          prt("You can't go that way.",REPL)

def mess():
    prt("You are in the Chapel",REPL)
    while True:
        prt("You can get some Coffee, grab some Food or eXit\n>",REPL)
        a = intpt(["c","f","x"])
        if a == "x":
          return
        elif a == "c":
            coffee= ["a latte","a decaf","a frappucino"]
            prt("you get " + random.choice(coffee),REPL)
            compthink()
            
        elif a == "f":
            food= ["some plo meek soup","a salad","a steak"]
            prt("you get " + random.choice(food),REPL)
            compthink()
        else:
            prt("You can't go that way.",REPL)
            prt("yum!",REPL)

def deck7():
  prt("You are on deck7",REPL)
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

def deck13():
  prt("You are on deck13",REPL)
  while True:
    prt("You can go to the observation lounge or turbolift.\n>",REPL)
    a=intpt(["o","t"])
    if a == "t":
      return
    elif a == "o":
      observation()  
    else:
      prt("You can't go that way.",REPL)
      
def observation():
    prt("look at those stars go by!!!",REPL)
    compthink()
    
bridge()


