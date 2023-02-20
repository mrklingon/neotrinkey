import time
import random
Nulls = [
    "Hmmm....",
    "Tell me something interesting.",
    "Ah.",
    "Well, well, well.",
    "Oh."]

Questions = [
    "What do you do?",    
    "Where am I right now?",
    "Do you have any problems?",
    "When do you feel happy?",
    "Are you having a good day?",
    "What will tomorrow bring?"]

Affirmations = [
    "I'm happy you came by today.",
    "You are a fun person - I hope you know that.",
    "You are good at typing!",
    "I think you can do almost anything you put your mind to!"]
    
Comments = [
    "Today is a beautiful day.",
    "This is a nice computer - I like it here.",
    "I am really, really smart - I hope I can help you.",
    "Some times I make up prime numbers just for fun.",
    "I'm getting a little tired."]

name = input("Hello, what is your name? >> ")
print ("Thanks for coming by, "+ name +"!")

done = False

while not done:
    time.sleep(1)

    choice = random.randrange(10)

    if choice < 3:
        resp =  (Comments[random.randrange(len(Comments))])

    if choice >= 3 and choice <= 5:
        resp = (Nulls[random.randrange(len(Nulls))])

    if choice > 5 and choice <= 6:
        resp = (Questions[random.randrange(len(Questions))])

    if choice > 6:
        resp = (Affirmations[random.randrange(len(Affirmations))])

    print (resp)
    
    answer = input(">> ")
    
    if answer == "quit":
        done = True

