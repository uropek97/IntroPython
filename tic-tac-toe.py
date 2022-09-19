from asyncio import SendfileNotAvailableError
from random import randint


firstStr =  '_|_|_'
secondStr = '_|_|_'
thirdStr =  '_|_|_'

o = 'O͇'
x = 'X͇'
xo = [x,o]
string = 2
column = 2
liststr = [firstStr, secondStr, thirdStr]

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
        currentStr = currentStr[:column]+x+currentStr[column+1:]
        liststr[string-1] = currentStr
        correct = True

print(f'{liststr[0]}\n{liststr[1]}\n{liststr[2]}')

def check_cond(liststr, symb):
    a = 0
    #сделать проверку на выиграшь с помощью функций map, filter или zip
