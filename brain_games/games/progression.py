#!/usr/bin/env python3
import random
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    a = str_first_num = randint(1, 20)
    c = progression_step = randint(1, 10)
    str_len = randint(6, 10)
    # граница итерации набора строки:
    b = str_first_num + progression_step * (str_len - 1)

    str_progression = []
    for i in range(a, b, c):
        str_progression.append(i)

    lost_num = random.choice(str_progression)
    index_lost_num = str_progression.index(lost_num)
    str_progression[index_lost_num] = '..'
    change_str_progression = ' '.join(map(str, str_progression))

    question = f'{change_str_progression}'
    answer = str(lost_num)

    return question, answer
