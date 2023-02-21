#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    end = start + step * length
    progression = list(range(start, end, step))

    index_lost_num = randint(0, length - 1)
    lost_num = progression[index_lost_num]
    progression[index_lost_num] = '..'
    change_progression = ' '.join(map(str, progression))

    question = change_progression
    answer = str(lost_num)

    return question, answer
