from asyncio import SendfileNotAvailableError
from functools import reduce
from random import randint
from tkinter.tix import Tree


firstStr =  '_|_|_'
secondStr = '_|_|_'
thirdStr =  '_|_|_'
liststr = [firstStr, secondStr, thirdStr]

def move(liststr, symb):
    correct = False
    while not correct:
        string = int(input('Строка:'))
        if string < 1 or string > 3:
            continue
        column = int(input('Колонна:'))
        if column < 1 or column > 3:
            continue
        currentStr = liststr[string-1]
        if column == 1:
            column = 0
        elif column == 3:
            column = 4
        if currentStr[column] == '_':
            currentStr = currentStr[:column]+symb+currentStr[column+1:]
            liststr[string-1] = currentStr
            correct = True
    print(f'{liststr[0]}\n{liststr[1]}\n{liststr[2]}')



def check_win(liststr, symb):
    a = list(zip(liststr[0], liststr[1], liststr[2]))
    checkcolumn = symb*3
    a1 = reduce(lambda a,b: a+b, a[0])
    if a1 == checkcolumn:
        return True
    a2 = reduce(lambda a,b: a+b, a[2])
    if a2 == checkcolumn:
        return True
    a3 = reduce(lambda a,b: a+b, a[4])
    if a3 == checkcolumn:
        return True

    str1 = a1[0]+a2[0]+a3[0]
    if str1 == checkcolumn:
        return True
    str2 = a1[1]+a2[1]+a3[1]
    if str2 == checkcolumn:
        return True
    str3 = a1[2]+a2[2]+a3[2]
    if str3 == checkcolumn:
        return True

    diag1 = a1[0]+a2[1]+a3[2]
    if diag1 == checkcolumn:
        return True
    diag2 = a1[2]+a2[1]+a3[0]
    if diag2 == checkcolumn:
        return True

    return False

def check_end(liststr, symb = '_'):
    a = list(zip(liststr[0], liststr[1], liststr[2]))
    if symb not in a[0]:
        if symb not in a[2]:
            if symb not in a[4]:
                return True
    return False

def tic_tac_toe_game(liststr, symb1 = 'X', symb2 = 'O'):
    print(f'{liststr[0]}\n{liststr[1]}\n{liststr[2]}')

    while True:
        move(liststr, symb1)
        if check_win(liststr, symb1):
            print(f'Победитель: Игорок 1({symb1})')
            return
        if check_end(liststr):
            print('Ничья')
            return
        move(liststr, symb2)
        if check_win(liststr, symb2):
            print(f'Победитель: Игорок 2({symb2})')
            return        

tic_tac_toe_game(liststr)

