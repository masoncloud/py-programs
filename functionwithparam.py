#!/usr/bin/python
#functionwithparam.py

def printMax(a,b):
    if a > b:
        print ( a, "is maximum")
    else:
        print ( b, "is maximum")

x = int(input('x:'))
y = int(input('y:'))
printMax(x,y)
