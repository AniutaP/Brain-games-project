#!/usr/bin/env python3
import prompt
import random
from random import randint
import operator


def calc_start():
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What is the result of the expression?''')
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    i = 1
    while i <= 3:
        calc_a = randint(1, 100)
        calc_b = randint(1, 100)
        oper, function = random.choice(operators)
        print('Question: {} {} {}'.format(calc_a, oper, calc_b))
        player_answer_calc = prompt.integer('Your answer: ')
        game_answer_calc = function(calc_a, calc_b)
        if player_answer_calc == game_answer_calc:
            print('Correct!')
            i += 1
        else:
            print(f''''{player_answer_calc}' is wrong answer ;(.
Correct answer was '{game_answer_calc}'.
Let's try again, {name}!''')
            break
    else:
        print(f'Congratulations, {name}!')
