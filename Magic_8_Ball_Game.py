# By Justine Robert Igune
# Making a Magic 8 ball Game

import unittest
from unittest import TestCase

import random
import time

    

#Sequence for random choice
Magic8Ball_answers = ['It is certain', 'It is decidedly so', 'Without a doubt',
           'Yes – definitely', 'You may rely on it', 'As I see it, yes',
           'Most likely', 'It looks good', 'Yes Signs point to yes',
           'Question not clear', 'try again', 'Ask again later', 'Better not tell you now',
           'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no',
           'My sources say no', 'It looks not so good', 'Very doubtful']

print('    __      __  __        __  __          _____ _____ _____    ___         ')  
print('   |  |    |  ||  |      |  \/  |   /\   / ____|_   _/ ____|  / _ \    _   ')
print('   |  |____|   |  |      | \  / |  /  \ | |  __  | || |      | (_) |  |_|  ')
print('   |   ____    |  |      | |\/| | / /\ \| | |_ | | || |       > _ <    _   ')
print('   |  |    |  ||  |  _   | |  | |/ ____ \ |__| |_| || |____  | (_) |  |_|  ')
print('   |__|    |__||__| /_/  |_|  |_/_/    \_\_____|_____\_____|  \___/        ')
print('')
print('')
print('')


print('Hello There, I am the Magic 8 Ball, What is your name?')
name = input()
print('Hello ' + name + ',')


#Delay output for 0.5 second each
print("Processing...")
time.sleep(0.5)
print("Wait...")
time.sleep(0.5)
print("Wait...")
time.sleep(0.5)
print("Wait...")
time.sleep(0.5)
print()


#Generate a random integer/response
response = random.randint(0,20)

def Magic8Ball():
    print('Feel free to ask your question or Seek an advice please.')
    input()
    print("In Progress...")
    time.sleep(3)
    print (Magic8Ball_answers[random.randint(0, len(Magic8Ball_answers)-1)] )#Generate a random integer/response
    print('I hope that helped you!')
    Replay()
    

def Replay():
    print ('Do you have another question or still seek advice? [Y/N] ')
    reply = input()
    print("In Progress...")
    time.sleep(3)
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        print("Bye bye, See you again...")
        exit(0)
    else:
        print('I apologise, I did not understand what you meant. Please try again.')
        Replay()


#To import name 'Magic_8_Ball_Game' from 'Magic_8_Ball_Game		
Magic8Ball()


