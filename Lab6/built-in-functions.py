from functools import *
import time
import math

#1

def multList(numbers):
    result = reduce(lambda x,y: x*y, numbers)
    print(result)
    
multList([4,2,56,8,2,2])

#2

def lowUpCase(st):
    isl=isu=0
    for i in range(0, len(st)):
        if st[i].islower():
            isl+=1
        else:
            isu+=1
            
    print(f'Upper case: {isu} Lower Case: {isl}')
    
lowUpCase('clmvlvsfASikAksfkv')

#3

def isPal(st):
    if st==st[::-1]:
        print('Yes, it is palindrome')
    else:
        print('No, it is not palindrome')

        
isPal('abbba')

#4

def rootAfter(number, mill):
    time.sleep(mill/1000)
    print(math.sqrt(number))
    
number = int(input())
mill = int(input())

rootAfter(number, mill)
print(f'Root of {number} after {mill} milliseconds is {math.sqrt(number)}')

#5

def allTrue(tup):
    return all(tup)

tup = (True, True, True)

if allTrue(tup):
    print(True)
else:
    print(False)
    
    
    