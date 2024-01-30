import math
from random import randint

#1

def ounces(grams):
    print(28.3495231 * grams)

#2

def celc(far):
    print((5 / 9) * (far - 32))
    
#3
    
def solve(numh, numl):
    rabb = (numl-2*numh)/2
    
    chick = numh-rabb
    
    print("Rabbits:", rabb, "Chickens:", chick)
    
solve(35, 94)

#4

def filter_prime(primeList):
    for i in primeList:
        prime = True
        for j in range(2,i):
            if (i%j==0):
                prime = False
        if prime:
           print (i, end=" ")
            
filter_prime([1,2,3,4,5,6,7,8,9,11,12,13,17,22,12])
print()

#5

def toString(List): 
    return ''.join(List) 
  
def permute(a, l, r): 
    if l == r: 
        print(toString(a))  
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r) 
            
            a[l], a[i] = a[i], a[l] 

string = input("Enter word or phrase: ")
n = len(string) 
a = list(string) 
  
   
permute(a, 0, n) 

#6

def rev(string):
    string = string.split(" ")
    
    for i in range(len(string)-1, -1, -1):
        print(string[i], end=" ")

rev('Mama just killed a man')

#7

def has_33(nums):
    is33 = False
    
    for i in range (0, len(nums)):
        if i == len(nums)-1:
            break
        if nums[i]==3 and nums[i+1]==3:
            is33 =True
            break
    
    print(is33)
    
has_33([1, 3, 3])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3])

#8

def spy_game(nums):
    spy = ''
    j=0
    
    for i in range (0, len(nums)):
        if nums[i]==0 and j==0:
            spy+='0';
            j=1
        if nums[i]==0 and j==1:
            spy+='0';
            j=2
        if nums[i]==7 and j==2:
            spy+='7';
            break
    
    if spy=='007':
        print(True)
    else:
        print(False)
    
spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0])

#9

def sphereV(radius):
    print(4/3*math.pi*pow(radius, 3))
    
sphereV(4)

#10

def uniqueList(li1):
    li2=[]
    
    for i in li1:
        if i not in li2:
            li2.append(i)
            
    print(li2)
    
uniqueList([1,1,2,5,7,3,5,6,2])

#11

def palindrome(str):
    str1=''
    str2=''
    
    str1=str
    str2=str[::-1]
    
    if str1==str2:
        print(True)
    else:
        print(False)
        

palindrome('abba')
palindrome('abbc')
palindrome('acbca')

#12

def histogram(ls):
    for i in ls:
        for j in range(0, i):
            print('*', end='')
        print()
        
histogram([4,9,7])

#13

def findNum():
    num = randint(1,20)
    atNum = 1
    name = input("Hello! What is your name? ")
    guessNum = int(input("Well, "+name+", I am thinking of a number between 1 and 20.\nTake a guess. "))

    
    while num!=guessNum:
        if num>guessNum:
            guessNum = int(input( "Your guess is too low.\nTake a guess. "))
        else:
            guessNum = int(input( "Your guess is too high.\nTake a guess. "))
        atNum+=1
            
    print("Good job, "+name+"! You guessed my number in",atNum,"guesses!")
    



findNum()

#14 I'm too lazy for this
          