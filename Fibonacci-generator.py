#-------------------------------------------------------------------------------
# Name:        Python-Basics
# Purpose:     Hobby
#
# Author:      Arunanand T A
#
# Created:     21/04/2014
# Licence:     GPL 2.0
#-------------------------------------------------------------------------------

#To demonstrate the generator concept in Python.

import sys #For exiting the program explicitly

def fib_gen():
    first=second=1
    while True:
        yield first #variable 'first' is yielded here. This is what's being returned to the function call and the state of this variable is kept intact even after the call
        first, second = second, first+second #This is where the swapping occurs for the next run

n=input('Enter the limit till which Fibonnacci numbers should be printed ')

if(n<1):
    print ('Invalid entry. Must be greater than 0')
    sys.exit()
f_val=fib_gen()
for num in f_val:
    if num<=n:
        print (num)
    else:
        break
