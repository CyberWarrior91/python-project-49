import random
import prompt
from brain_games.scripts.greeting.welcome_user import welcome_user


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    n = 0
    while n < 3:
        action = random.choice('+' '-' '*')
        num_1 = random.randint(1, 99)
        num_2 = random.randint(1, 99)
        if action == '+':
            right_answer = num_1 + num_2
        if action == '-':
            right_answer = num_1 - num_2
        if action == '*':
            right_answer = num_1 * num_2
        print(f"Question: {num_1} {action} {num_2}")
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


if __name__ == '__main__':
    main()
