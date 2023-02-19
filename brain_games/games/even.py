#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    random_number = randint(1, 100)
    question = random_number
    answer = 'yes' if random_number % 2 == 0 else 'no'

    return question, answer
