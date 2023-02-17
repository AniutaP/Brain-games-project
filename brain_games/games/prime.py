#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    if a > 1 and a % a == 0:
        count = 1
        for i in range(2, a):
            if a % i == 0:
                count += 1
        return False if count >= 2 else True
    else:
        return False


def get_question_and_answer():
    a = randint(0, 100)
    answer_prime = is_prime(a)

    answer = 'yes' if answer_prime is True else 'no'
    question = f'{a}'

    return question, answer
