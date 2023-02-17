#!/usr/bin/env python3
import prompt


def run_game(game):
    print('Welcome to the Brain Games!')

    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')

    print(game.DESCRIPTION)
    rounds_count = 3
    for round_number in range(0, rounds_count):
        question, correct_answer = game.get_question_and_answer()

        print(f"Question: {question}")
        player_answer = prompt.string("Your answer: ")

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {user_name}!")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
