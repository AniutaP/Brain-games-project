#!/usr/bin/env python3
from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(6, 10)
    end = start + step * length
    progression = list(range(start, end, step))

    lost_num = choice(progression)
    index_lost_num = progression.index(lost_num)
    progression[index_lost_num] = '..'
    change_progression = ' '.join(map(str, progression))

    question = f'{change_progression}'
    answer = str(lost_num)

    return question, answer
