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
        expression = f'{num_1} {action} {num_2}'
        print(f"Question:  {expression}")
        answer = prompt.string("Your answer: ")
        if action == "+" and answer == f"{num_1 + num_2}":
            print('Correct!')
            n += 1
        elif action == "+" and answer != f"{num_1 + num_2}":
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f"'{num_1 + num_2}'.")
            break
        elif action == '-' and answer == f"{num_1 - num_2}":
            print('Correct!')
            n += 1
        elif action == "-" and answer != f"{num_1 - num_2}":
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{num_1 - num_2}'.")
            break
        elif action == '*' and answer == f"{num_1 * num_2}":
            print('Correct!')
            n += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{num_1 * num_2}'.")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
