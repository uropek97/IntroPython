from fileinput import close
from random import randint


def issimple(numb):
    if(numb == 1 or numb == 2):
        return True
    i = 2
    while i < numb:
        if numb%i==0:
            return False
        i+=1
    return True

def task1(numb):
    multiplierslist = []
    i = 2
    while i <= numb:
        if issimple(i):
            while numb%i == 0:
                multiplierslist.append(i)
                numb//=i
        i+=1
    
    return multiplierslist

#print(task1(100))

def task2(numbList): #изначально написал код для любого листа
    newList = numbList.copy()
    endlist = []
    while len(newList)!=0:
        item = newList[0]
        newList.remove(item)
        a = 0
        while item in newList: 
                newList.remove(item)
                a+=1
        if a==0:
            endlist.append(item)

    return(endlist)


mylist = [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10]
#print(task2(mylist))

def formPolymonial(k):
    rdm = randint(1,4)
    polynomial = ''

    if rdm == 1:
        rdm = randint(1, 101)
        polynomial += f'{rdm}*x^{k}'
    elif rdm == 2:
        rdm = randint(1,101)
        polynomial += f'{rdm}*x^{k} + '
        rdm = randint(1,101)
        polynomial += f'{rdm}*x'
    else:
        rdm = randint(1,101)
        polynomial += f'{rdm}*x^{k} + '
        rdm = randint(1,101)
        polynomial += f'{rdm}*x + '
        rdm = randint(1,101)
        polynomial += f'{rdm}'

    return polynomial

def task3(file, k):
    f = open(file, 'a')
    f.write(f'{formPolymonial(k)}\n')
    f.close()

for i in range (2, 101):
     task3('polynomials1.txt', i)

for i in range (2, 101):
    task3('polynomials2.txt', i)


def parsPol(stringPol:str):
    listnumb = []

    a = stringPol.split('+')    
    b = a[0].strip().split('*')
    c = b[1].split('^')
    listnumb.append(int(b[0]))
    listnumb.append(int(c[1]))

    if(len(a)>1):
        d = a[1].split('*')
        listnumb.append(int(d[0]))

    if(len(a)==3):
        listnumb.append(int(a[2]))
    
    return listnumb


def sumpol(polyn1:list, polyn2:list):
    polynSum = []
    if polyn1[1] == polyn2[1]:
        polynSum.append(polyn1[0] + polyn2[0])
        polynSum.append(polyn1[1])
    else:
        return polynSum

    if len(polyn1) > 2 and len(polyn2) > 2:
        polynSum.append(polyn1[2] + polyn2[2])
    else:
        if len(polyn1)==3:
            polynSum.append(polyn1[2])
        elif len(polyn1)==4:
            polynSum.append(polyn1[3])
        
        if len(polyn2)==3:
            polynSum.append(polyn2[2])
        elif len(polyn2)==4:
            polynSum.append(polyn2[3])

    if len(polyn1)==4 and len(polyn2)==4:
        polynSum.append(polyn1[3] + polyn2[3])
    else:
        if len(polyn1)==4:
            polynSum.append(polyn1[3])

        if len(polyn2)==4:
            polynSum.append(polyn2[3])

    return polynSum

def printPol(listPol:list):
    strPol = f'{listPol[0]}*x^{listPol[1]}'

    if len(listPol)>2:
        strPol += f' + {listPol[2]}*x'

    if len(listPol)==4:
        strPol += f' + {listPol[3]}'

    return strPol

namefile1 = 'polynomials1.txt'
namefile2 = 'polynomials2.txt'


def task4(namefile1, namefile2):
    polynomialslist1 = []
    with open(namefile1, 'r') as file1:
        for line in file1:
            polynomial = parsPol(line)
            polynomialslist1.append(polynomial)

    polynomialslist2 = []
    with open(namefile2, 'r') as file2:
        for line in file2:
            polynomial = parsPol(line)
            polynomialslist2.append(polynomial)

    sumpolynomialslist = []
    #складываем те что возможно в разных листах
    for item in polynomialslist1:
        i = 0
        while i < len(polynomialslist2):
            item2 = polynomialslist2[i]
            if item[1] == item2[1]:
                sumpolynomialslist.append(sumpol(item, item2))
            i+=1
        
    with open('polynomialsSum', 'w') as file3:
        for line in sumpolynomialslist:
            if len(line) != 0: 
                file3.write(printPol(line) + '\n')


task4(namefile1, namefile2)