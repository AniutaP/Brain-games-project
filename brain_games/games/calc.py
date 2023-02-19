#!/usr/bin/env python3
import random
from random import randint
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    oper, function = random.choice(operators)

    question = '{} {} {}'.format(num_1, oper, num_2)
    answer = str(function(num_1, num_2))

    return question, answer
