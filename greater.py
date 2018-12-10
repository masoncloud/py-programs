#!/usr/bin/python
#greater.py

number =23
guess = int(input('Enter a number: '))
if guess == number:
    print ('You guessed it right buddy !!')
elif(guess < number):
    print ('You are little lower')
else:
    print ('You are a little higher')
print ("Done")
