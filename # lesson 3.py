from re import A
from turtle import position
from unicodedata import decimal


def task1(mylist):    
    i = 0
    result = 0

    while i < len(mylist):
        if i%2 != 0:
            result+=mylist[i]
        i+=1

    print (result)
    return result

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
task1(mylist)

def task2(mylist):
    i = 0
    newlist = []

    while i < len(mylist)/2:
        newlist.append(mylist[i]*mylist[-(i+1)])
        i+=1

    
    print(newlist)
    return newlist
task2(mylist)

def task3(mylist):
    min = 1
    max = 0
    i = 0
    while i < len(mylist):
        a = mylist[i]%1
        if a<min:
            min = a
        i+=1
    i = 0
    while i < len(mylist):
        a = mylist[i]%1
        if a>max:
            max = a
        i+=1
    
    result = max-min
    print (result)
    return result

myfloatlist = [1.1, 10.2, 3, 4.4, 5.55]
task3(myfloatlist)

def task4(numb):
    numbCopy = numb
    mylist = []
    isodd = True

    if numbCopy%2 != 0:
        numbCopy = numbCopy - 1
        isodd = True
    else:
        isodd = False

    degree = 1
    while numbCopy!=0:
        if numbCopy > 2**degree:
            degree+=1
        elif numbCopy < 2**degree:
            numbCopy -= 2**(degree-1)
            mylist.append(degree-1)
            degree = 1
        elif numbCopy == 2**degree:
            numbCopy -= 2**degree
            mylist.append(degree)

    a = 0  
    decstr = ''
    if isodd:
        decstr+='1'
    else:
        decstr+='0'
    
    i = 0
    position = 0
    while i<len(mylist):        
        a = mylist[-i-1]
        while a-1 > position:
            decstr+='0'
            position+=1
        decstr+='1'
        position = a
        i+=1
    newstr = decstr[::-1]
    print (newstr)
    return newstr

decnumbstr = task4(999999)
decnumbstr1 = task4(9999)
decnumbstr2 = task4(99)


def fibonacci(numb):
    if numb == 0:
        return 0
    elif numb == 1 or numb == 2:
        return 1
    else:
        return fibonacci(numb-1)+fibonacci(numb-2)


def task5(numb):
    newNumb = numb
    listnumbers = []

    while newNumb!=0:
        a = fibonacci(newNumb)
        listnumbers.append(-a)
        newNumb-=1
    newListnumbers = listnumbers.copy()
    newListnumbers.append(0)
    while newNumb!=numb:
        newListnumbers.append(-listnumbers[-newNumb-1])
        newNumb+=1

    print(newListnumbers)
    return newListnumbers

task5(15)
        

