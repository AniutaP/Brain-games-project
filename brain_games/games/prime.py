#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    num = randint(0, 100)
    answer_prime = is_prime(num)

    answer = 'yes' if answer_prime is True else 'no'
    question = f'{num}'

    return question, answer
