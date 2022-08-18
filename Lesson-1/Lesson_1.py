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
