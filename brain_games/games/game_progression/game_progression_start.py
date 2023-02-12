import prompt
import random
from random import randint


def progression_start():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!'
          f'\nWhat number is missing in the progression?')
    index = 1
    while index <= 3:
        str_first_num = randint(1, 20)
        a = str_first_num
        progression_step = randint(1, 10)
        c = progression_step
        str_len = randint(6, 10)
        end_iter = str_first_num + progression_step * (str_len - 1)
        b = end_iter
        str_progression = []
        for i in range(a, b, c):
            str_progression.append(i)
        lost_num = random.choice(str_progression)
        index_lost_num = str_progression.index(lost_num)
        str_progression[index_lost_num] = '..'
        change_str_progression = ' '.join(map(str, str_progression))
        print(f'Question: {change_str_progression}')
        player_answer_progression = prompt.string('Your answer: ')
        game_answer_progression = str(lost_num)
        if player_answer_progression == game_answer_progression:
            print('Correct!')
            index += 1
        else:
            print(f"'{player_answer_progression}' is wrong answer ;(. "
                  f"Correct answer was '{game_answer_progression}'."
                  f"\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
