import prompt
from brain_games.cli import welcome_user


def run_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.DESCRIPTION)
    n = 0
    while n < 3:
        question, right_answer = game.get_question_with_answer()
        print(question)
        answer = prompt.string("Your answer: ")
        if f"{answer}" == f"{right_answer}":
            print('Correct!')
            n += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{right_answer}'.")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
