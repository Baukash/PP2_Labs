#1

n = int(input())
a = (i**2 for i in range(1,n+1))

for i in a:
    print(i)
    
#2
    
n = int(input())
a = (i for i in range(0, n, 2))
for i in a:
    print(i, end = ' ')
    
    
#3
    
n = int(input())

a = (i for i in range(0, n+1) if i%4==0 and i%3==0)

for i in a:
    print(i, end = ' ')
    
#4
    
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
        
a = int(input())
b = int(input())

for i in squares(a, b):
    print(i, end=' ')
    
#5
    
n = int(input())

a = (i for i in range(n, -1, -1))

for i in a:
    print(i, end=' ')