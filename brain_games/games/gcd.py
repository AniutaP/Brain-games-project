#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1, num_2):
    if (num_2 == 0):
        return abs(num_1)
    else:
        return abs(get_gcd(num_2, num_1 % num_2))


def get_question_and_answer():
    num_1 = randint(-100, 100)
    num_2 = randint(-100, 100)

    question = f'{num_1} {num_2}'
    answer = str(get_gcd(num_1, num_2))

    return question, answer
