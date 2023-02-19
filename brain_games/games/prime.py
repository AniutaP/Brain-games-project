#!/usr/bin/env python3
from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        for i in range(2, math.sqrt(num)):
            if num % i == 0:
                return False
        return True
    return False


def get_question_and_answer():
    num = randint(0, 100)
    answer_prime = is_prime(num)

    answer = 'yes' if answer_prime is True else 'no'
    question = f'{num}'

    return question, answer
