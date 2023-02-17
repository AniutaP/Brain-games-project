#!/usr/bin/env python3
import random
from random import randint
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    oper, function = random.choice(operators)

    question = '{} {} {}'.format(a, oper, b)
    answer = str(function(a, b))

    return question, answer
