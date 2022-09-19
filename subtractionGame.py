from random import randint

rules = 'Перед вами 2021 конфета. Каждый игрок по очеред берёт N конфет.\nМаксимум можно взять 28 конфет. Побеждает тот, кто заберёт последнюю конфету. Удачи!'
wrong = 'Неверный ход. Вы можете взять от 1 до 28 конфет.'

player1 = ['Петя', 0]
player2 = ['Вася', 0]
bot = 'Бот'

def moveplayer(player, candies, step = 28):
    correct = False
    print(f'Конфет: {candies}')
    while not correct:
        player[1] = int(input(f'Ходит {player[0]}: '))
        if player[1]<1 or player[1]>step:
            print(wrong)
            correct = False
        else:
            correct = True
    return candies - player[1]

def gameprocess(player1, player2, move1, move2, candies = 2021):
    can_play = True
    winner = 'nobody'
    while can_play:
        candies = move1(player1, candies)
        if(candies <= 0):
            winner = player1[0]
            return winner

        candies = move2(player2, candies)
        if(candies <= 0):
            winner = player2[0]
            return winner

def game(player1, player2, move1, move2):
    print(rules)
    winner = gameprocess(player1, player2, move1, move2)

    return f'Победитель {winner}!\nПоздравляем!\nКонец игры.'

def moveBotEasy(bot, candies, max = 28):
    print(f'Конфет: {candies}')
    step = randint(1,max)
    print(f'Ходит {bot}: {step}')
    return candies - step

def moveBotHard(bot, candies, max = 28):
    print(f'Конфет: {candies}')
    
    a = list(filter(lambda item: item%(max+1)==0, range(candies-max, candies+1)))
    if candies - a[0] > 1 and candies - a[0] < max:
        step = candies - a[0]

    else:
        step = randint(1,max)

    print(f'Ходит {bot}: {step}')
    return candies - step

print(game(player1, player2, moveplayer, moveplayer))
print(game(player1, bot, moveplayer, moveBotEasy))
print(game(player1, bot, moveplayer, moveBotHard))