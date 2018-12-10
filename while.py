#!/usr/bin/python
#while.py

number = 23
running = True
while running :
    guess = int(input("Enter an integer, "))
    if guess == number:
        print ("You guessed it right buddy")
        running = False
    elif guess < number:
        print ("You are little lower")
    else:
        print ("You are little higher")
else:
        print("While loop is done")
print ("Done boss")
