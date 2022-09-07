# #14
import re


def sum(num):
    result = 0

    while num > 0:
        result += num%10
        num = int(num/10)

    return result

def task14():
    number = input('input number(float): ')


    x = number.split('.') 

    integer = int(x[0])
    if x.__len__() > 1:
        fract = int(x[1])


    result = sum(integer)
    if x.__len__() > 1:
        result += sum(fract)

    print(f'sum of digits {number}: {result}')
    
    return result

task14()


# #15
def task15():
    N = int(input('input number(int > 1): '))

    numbers = [1]
    i = 1
    while i < N: 
        numbers.append(numbers[i-1]*(i+1))
        i += 1

    print(numbers)
    
    return numbers

task15()


# #18
from random import randint

def algoritmmix(startlist):    
    newlist = startlist.copy()
    i = 0
    amount = newlist.__len__()

    while i < amount-1:
        random = randint(i+1, amount-1)
        temp1 = newlist[random]
        temp2 = newlist[i]
        newlist[i] = temp1
        newlist[random] = temp2
        i += 1

    print(newlist)        

    return newlist

def task18():

     startlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     algoritmmix(startlist)
     
task18()

## #8

#def  task8():
#    print('8 task')

#    X = int(input('X-coordinate: '))
#    Y = int(input('Y-coordinate: '))

#    if X==0 and Y==0:
#        print('point in the center of the coordinates')
#    elif X==0:
#        print('a point on the X-axis')
#    elif Y==0:
#        print('a point on the Y-axis')
#    elif X > 0 and Y > 0:
#        print('point in 1 coordinate quarter')
#    elif X < 0 and Y > 0:
#        print('point in 2 coordinate quarter')
#    elif X < 0 and Y < 0:
#        print('point in 3 coordinate quarter')
#    elif X > 0 and Y < 0:
#        print('point in 4 coordinate quarter')

#    return

#task8()

## #9
#def task9():

#    print('9 task')

#    quarter = int(input('enter a number of quarter: '))

#    if quarter == 1:
#        print(f'point can have coodinates: X > 0 Y > 0')
#    elif quarter == 2:
#        print(f'point can have coodinates: X < 0 Y > 0')
#    elif quarter == 3:
#        print(f'point can have coodinates: X < 0 Y < 0')
#    elif quarter == 4:
#        print(f'point can have coodinates: X > 0 Y < 0')

#    return

#task9()

# #10
#def points():
#    coordinates = ["X", "Y"]
#    point =[]
#    for i in range(coordinates.__len__()):
#        point.append(float(input(f'enter {coordinates[i]}: ')))
    
#    return point

#def task10():
#    print('10 task')

#    print('first point')
#    firstpoint = points()
#    print('===============')
#    print('second point')
#    secondpoint = points()
#    print('===============')

#    distance = ((firstpoint[0] - secondpoint[0])**2 + (firstpoint[1] - secondpoint[1])**2)**0.5

#    print(f'distance {distance}')

#    return

#task10()

# #1

#a = int(input('enter first number: '))
#b = int(input('enter second number: '))
#if b == a*a:
#    print(f'number {b} is square {a}')
#else:
#    print(f'number {b} isnt square {a}')

# #2 

#a = float(input('enter 1 number: '))
#b = float(input('enter 2 number: '))  
#c = float(input('enter 3 number: ')) 
#d = float(input('enter 4 number: ')) 
#e = float(input('enter 5 number: ')) 

#maxim = a;
#if maxim < b:
#    maxim = b
#if maxim < c:
#    maxim = c
#if maxim < d:
#    maxim = d
#if maxim < e:
#    maxim = e
#print(maxim)
##���
#listnumb = [a, b, c, d, e];
#print(max(listnumb))

# #3 

#a = int(input('enter a number: '))
#i = -a
#while i != a+1:
#    print(i)
#    i+=1

# #4 

#a = float(input('enter a number: '))
#b = a*10
#c = int(b)
#print(c%10)

# #5 

#a = int(input('enter a number: '))
#b = a%5==0 and (a%10==0 or a%15==0)
#c = not a%30==0
#if b and c:
#    print(f'number {a} is a multiple of 5, 10 or 15, and not a multiple of a 30')
#else:
#    print('conditions not met')

# #6 

#workdays = ['mondey', 'tuesday', 'wednesday', 'thursday', 'friday']
#weekends = ['saturday', 'sunday']
#a = int(input('Enter number of the week: '))
#if a <=5:
#    print(f'{workdays[a-1]}')
#else:
#    print(f'{weekends[a-6]}')

# #7 

#values = ['X', 'Y', 'Z']
#a = []
#for i in range(values.__len__()):
#    a.append(input(f'Enter value {values}: '))

#firstpart = not(a[0] or a[1] or a[2])
#secondpart = not a[0] or not a[1] or not a[2]

#print(firstpart == secondpart)

# #11

#numbers = [1]
#n = 0
#while n < 1:
#    n = int(input('input number(number must be more than 1): '))

#i = 1;
#while i < n:
#    numbers.append(numbers[i-1]*-3)
#    i+=1

#print(numbers)

# #12
#dictionary = dict()

#n = -1
#while n < 0:
#    n = int(input('input number(number must be more than 0): '))

#i = 1
#while i <= n:
#    dictionary[i] = 3*i+1
#    i+=1

#print(dictionary)

# #13
#search = input('input search string: ')
#found = input('input found string: ')

#index = 0
#count = 0
#while index != -1:
#    index = search.find(found)
#    if index >=0:
#        count += 1
#    search = search[index+1:]

#print(count)


# #16 

#n = int(input('enter a number: '))
#count = 0
#result = 0.0
#numbList = []
#while count is not n+1:
#    numbList.append(1 + (1/count))
#    result+=numbList[count-1]**count
#    count+=1
#print(result)


