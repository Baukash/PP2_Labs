import os

#1

def list_directories(path):
    directories = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
    return directories

def list_files(path):
    files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]
    return files

def list_all(path):
    all_contents = os.listdir(path)
    return all_contents

path = input("Input your path: ")

directories_list = list_directories(path)
print("Directories:", directories_list)

files_list = list_files(path)
print("Files:", files_list)

all_contents_list = list_all(path)
print("All Directories and Files:", all_contents_list)

#2

def checkAll(path):
    if os.path.exists(path):
        print("This file exists")
    else:
        print('This file does not exist')
        
    if os.access(path, os.R_OK):
        print('You have access to read this file')
    else:
        print('You do not have access to read this file')
    
    if os.access(path, os.W_OK):
        print('You have access to write in this file')
    else:
        print('You do not have access tp write in this file')
        
    if os.access(path, os.X_OK):
        print('You have access to execute this file')
    else:
        print('You do not have access to execute this file')
    
path = input('Input your path: ')

checkAll(path)

#3

def exDir(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        
        print(f'{path} exists, its filename - {filename} and directory - {directory}')
    else:
        print(f'{path} does not exist')
        
path = input("Input path: ")
exDir(path)

#4

def numLine(f):
    file = open(f, 'r')
    j=0
    for i in file:
        j+=1
        
    print(j)
    
    file.close()
    
numLine('file.txt')

#5

def writeInFile(f, l):
    file = open(f, 'a')
    for i in l:
        file.write(i)
        
    file.close()
    
    file = open(f, 'r')
    print(file.read())
    file.close()
writeInFile('file.txt', ['sfsdgsd', 'hello, world', 'My name is Dauren', 'I am KBTU student'])

#6

def createFile():
    for i in range(0, 26):
        f = open(f'{chr(65+i)}.txt', 'x')
        
createFile()

#7

def copyContent(f1, f2):
    file1 = open(f1, 'r')
    file2 = open(f2, 'w')
    
    file2.write(file1.read())
    
    file1.close()
    file2.close()
    
    file2 = open(f2, 'r')
    print(file2.read())
    
copyContent('file.txt', 'file2.txt')

#8

def deleteFile(path):
    if os.path.exists(path) and os.access(path, os.X_OK):
        os.remove(path)
    else:
        print("This path does not exists or permission to delete this file is denied")
        
path = input("Input path: ")
deleteFile(path)