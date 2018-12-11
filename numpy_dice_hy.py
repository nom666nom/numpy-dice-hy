#!/usr/bin/env python

#Simple Dice Rolling Script Using Numpy

#Importing Modules
import numpy as np

#Getting User Input for dice
print('Enter the number of dice you would like to roll. Max is 20.')
dicenumber = input('Number of dice:') 

if dicenumber > 20:
    print "You took the blue pill, try again"
    print "Max Number of Dice Allowed is 20"
    exit()
if dicenumber < 0:
    print "Negative dice, really?"
    exit()

print('Enter the number of sides.  Max is 20.')
dicesides = input('Number of sides:')

if dicesides > 20:
    print "You took the blue pill, try again"
    print "Max Number of Sides Allowed is 20"
    exit()
if dicesides < 0:
    print "Negative sides, really?"
    exit()
#The dimension command.  The +1 is needed to ensure the appropriate range creation.
a = np.arange(1,dicesides + 1)

#creating a blank matrix based on dice number and sides
matrix = np.empty((dicenumber,dicesides), int)
for i in range(0, dicenumber):
    matrix[i] = a

#print(matrix)
#Arrays and rows start at 0, need the dice count to start at 1.
dicenumber2 = 1
for i in range(0, dicenumber):
    dice = np.random.choice(matrix[i])
    print "Dice #:%s rolled a %s" % (dicenumber2,dice)
    dicenumber2 = dicenumber2 + 1
