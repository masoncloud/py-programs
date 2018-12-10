#!/usr/bin/python
#functions.py

def sayHello():
    print ("Hello Boss")
number = 30
age = True
while age:
    x = int(input("Whats your age?"))
    if x == number:
        sayHello()
        age = False
    elif x < number:
        print ("You are still a kid and is rejected")
    else:
        print ("I am sorry old man can't authenticate you")
    




