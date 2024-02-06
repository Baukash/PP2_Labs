from math import *

#1

degree = int(input('Input degree: '))

print(degree/180*pi)

#2

height = int(input('Input height: '))
b1 = int(input('Input first base: '))
b2 = int(input('Input second base: '))

print((b1+b2)/2*height)

#3

n = int(input('Input number of sides: '))
length = int(input('Input length of a side: '))

print(n*length/2*(1/tan(pi/n))*length/2)

#4

lbase = int(input('Length of base: '))
h = int(input('Height of parallelogram: '))

print(lbase*h)

