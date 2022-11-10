import prompt
from brain_games.cli import welcome_user


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    rounds = 1, 2, 3
    for num in rounds:
        question, right_answer = game.get_question_with_answer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
