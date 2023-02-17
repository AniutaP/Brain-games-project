#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd_cond(a, b):
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


def get_question_and_answer():
    a = randint(-100, 100)
    b = randint(-100, 100)

    question = f'{a} {b}'
    answer = str(gcd_cond(a, b))

    return question, answer
