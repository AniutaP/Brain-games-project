import prompt
import random
from random import randint, choice


def progression_start():
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What number is missing in the progression?''')
    i = 1
    while i <= 3:
        str_first_num = randint(1, 20)
        a = str_first_num
        progression_step = randint(1, 10)
        c = progression_step
        str_len = randint(6, 10)
        end_iter = str_first_num + progression_step * (str_len - 1)
        b = end_iter
        str_progression = ' '.join(str(i) for i in range(a, b, c))
        str_progression_ls = str_progression.split()
        lost_num = random.choice(str_progression_ls)
        change_str_progression = [_.replace(lost_num, '..') for _ in str_progression_ls]
        change_str_progression_ls_str = ' '.join(change_str_progression)
        print(f'''Question: {change_str_progression_ls_str}''')
        player_answer_progression = prompt.string('Your answer: ')
        game_answer_progression = lost_num
        if player_answer_progression == game_answer_progression:
            print('Correct!')
            i += 1
        else:
            print(f''''{player_answer_progression}' is wrong answer ;(.
Correct answer was '{game_answer_progression}'.
Let's try again, {name}!''')
            break
    else:
        print(f'Congratulations, {name}!')
