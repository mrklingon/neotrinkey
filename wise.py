import time
import random

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def wisdom(num,filename):
    global REPL
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    qs.close()
    return quote
