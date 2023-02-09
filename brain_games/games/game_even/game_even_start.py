#!/usr/bin/env python3
import prompt
from random import randint


def even_start():
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no"''')
    i = 1
    while i <= 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        player_answer_even = prompt.string('Your answer: ')
        game_answer_even = random_number % 2 == 0 and 'yes' or 'no'
        if player_answer_even == game_answer_even:
            print('Correct!')
            i += 1
        else:
            print(f''''{player_answer_even}' is wrong answer ;(.
Correct answer was '{game_answer_even}'.
Let's try again, {name}!''')
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    even_start()


if __name__ == '__main__':
    main()
