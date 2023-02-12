import prompt
from random import randint


def is_prime(a):
    if a > 1 and a % a == 0:
        count = 1
        for i in range(2, a):
            if a % i == 0:
                count += 1
        return False if count >= 2 else True
    else:
        return False


def prime_start():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!'
          f'\nAnswer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i <= 3:
        a = randint(0, 100)
        print(f'Question: {a}')
        player_answer_prime = prompt.string('Your answer: ')
        game_answer_prime = is_prime(a)
        game_answer_prime_final = 'yes' if game_answer_prime == True else 'no'
        if player_answer_prime == game_answer_prime_final:
            print('Correct!')
            i += 1
        else:
            print(f"'{player_answer_prime}' is wrong answer ;(. "
                  f"Correct answer was '{game_answer_prime_final}'."
                  f"\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
