import re

a = ['abba', 'dsdsbabbba', 'bfdsaababababab', 'a_ffsafasagbdfbfdbh', 'bfSdsb', 'gfsdgsabbbgfdhdbbb']

#1

for i in a:
    x = re.search('b*a' , i)
    print(x)
    
#2
    
for i in a:
    x = re.search('b{2,3}a' , i)
    print(x)
    
#3

for i in a:
    x = re.findall(r'\b[a-z]+_[a-z]+\b', i)
    print(x)
    
#4
    
for i in a:
    x = re.findall(r'\b[a-z]+[A-Z][a-z]*',i)
    print(x)
    
#5
    
for i in a:
    x = re.search('.+a.*b$', i)
    print(x)
    
#6

for i in a:
    x = re.sub("[\s\.\,]", ":", i)
    print(x)

#7

for i in a:
    x = re.split(r'_', i)
    print(x)

#8

for i in a:
    x = re.split('[A-Z]', i)
    print(x)
        
#9

for i in a:
    x = re.findall(r'[A-Z][a-z]*', i)
    answer = ' '.join(x)
    print(answer)

#10

for i in a:
    first_word = re.search('^[a-z]+', i)
    x = re.findall('[A-Z][a-z]*', i)
    
    if first_word is not None:
        x.insert(0, first_word.group())
    answer = '_'.join([j.lower() for j in x])
    
    print(answer)
