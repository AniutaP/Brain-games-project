import prompt
from random import randint


def gcd(a, b):
    if a != 0:
        if a > b:
            small = abs(b)
        else:
            small = abs(a)
        for i in range(1, small + 1):
            if (a % i == 0) and (b % i == 0):
                largest_i = i
        return largest_i
    elif a == 0 and b == 0:
        return 0
    else:
        return abs(b)


def gcd_start():
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Find the greatest common divisor of given numbers.''')
    i = 1
    while i <= 3:
        a = randint(-100, 100)
        b = randint(-100, 100)
        print(f'''Question: {a} {b}''')
        player_answer_gcd = prompt.integer('Your answer: ')
        game_answer_gcd = gcd(a, b)
        if player_answer_gcd == game_answer_gcd:
            print('Correct!')
            i += 1
        else:
            print(f''''{player_answer_gcd}' is wrong answer ;(.
Correct answer was '{game_answer_gcd}'.
Let's try again, {name}!''')
            break
    else:
        print(f'Congratulations, {name}!')
