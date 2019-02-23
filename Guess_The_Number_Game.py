# Question 3, Guess The Number of Code Review Questions - Cycle 17
# By Justine Robert Igune
# Making The Guess the Number Game
import unittest
from unittest import TestCase


import random
import sys

low = 5
high = 50
guesslimit = 10



print(' ________  __      __  __ __  __      __  __     __   __  __  _____   ____  _____     _______           ___  ___  ____ ') 
print('|__    __||  |    |  ||   __||_ \    |  ||  |   |  | |  \/  ||__  /\ |  __||   ) )   /\  ____)   /\    |   \/   ||  __|')
print('   |  |   |  |____|  ||  |_  | \  \  |  ||  |   |  | | \  / ||__/  | | |_  |  )  )  |  /   _    /  \   |  \   / || |__ ')
print('   |  |   |   ____   ||   _| |  \  \ |  ||  |   |  | | |\/| ||__ ><  |  _| | |\ )   | |___| |  / /\ \  | | \ /  ||  __|')
print('   |  |   |  |    |  ||  |__ |   \  \   ||  |__ |  | | |  | ||__\  | | |__ | | \ \  |   _ | | / ____ \ | |    | || |__ ')
print('   |__|   |__|    |__||_____||__|  \__\_/\________ / |_|  |_||____ / |____||_|  \/  |_____|_|/_/    \__\_|    |_||____| ')
print('')
print('')
print('')

#Prompts the guest to enter his/her name
print('Hello There, I am The_Guess_Number_Game, What do I call your name?')
name = input()
print('Hi ' + name + ',')

print ('Welcome to the guessing game!')
print("Guess a number between {0} and {1}".format(low, high))
print("You have {0} guesses to get the right number".format(guesslimit))


generateNumb = 0
number = random.randint(low, high)



try:
	while generateNumb < guesslimit:
		try:
			guess = int(input('What\'s your guess? '))
		except ValueError:
			print("Couldn\'t convert input to Integer")
			continue
	
		if guess < low or guess > high:
			print("Value out of range ({0} - {1})".format(low, high))
		else:
			generateNumb += 1
			
			if guess < number:
				print("That was too low")
		
			if guess > number:
				print("That was too high")
		
			if guess == number:
				break
	
except KeyboardInterrupt:
	print("\n  ^C detected, terminating...")
	sys.exit()

except EOFError:
	print("\n  ^D detected, terminating...")
	sys.exit()

if guess == number:
	print("Correct, you guessed the right number in {0} trials!".format(generateNumb))
else:
	print("I am Sorry! The number is actually {0}".format(number))



