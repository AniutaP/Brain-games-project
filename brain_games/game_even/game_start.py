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
        player_answer = prompt.string('Your answer: ')
        game_answer = random_number % 2 == 0 and 'yes' or 'no'
        if player_answer == game_answer:
            print('Correct!')
        i += 1
        if player_answer != game_answer:
            print(f'''"{player_answer}" is wrong answer ;(.
Correct answer was "{game_answer}".
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')


def main():
    even_start()


if __name__ == '__main__':
    main()
