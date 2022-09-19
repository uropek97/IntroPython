from ast import Global


def task1():
    stringa = 'абв бабв гггааа оаокакрпабв бвбвбвбврпгкра бвбвабвбврпгкра дададабв'
    a = stringa.split()
    c = a.copy()
    for item in a:
        if item.find('абв')!=-1:
            c.remove(item)

    b = ''
    for item in c:
        b+=item + ' '

    return b
print(task1())
# player1 = ['Игрок 1', 0]
# player2 = ['Игрок 2', 0]

# def move(player, candies):
#     return candies - player

# def gameCandies(player1, player2, candies = 2021):
#     while candies >= 0:
#         player1[1] = int(input(f'Конфет: {candies}\nХодит {player1[0]}: '))
#         candies = move(player1[1], candies)
#         if(candies)<=0:
#             return 'Победил 1 Игрок.\nКонец'
#         player2[1] = int(input(f'Конфет: {candies}\nХодит {player2[0]}: '))
#         candies = move(player2[1], candies)
#         if(candies)<=0:
#             return 'Победил 2 Игрок.\nКонец'

# print(gameCandies(player1, player2))