import random
import prompt
from brain_games.scripts.greeting.welcome_user import welcome_user
from math import gcd


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    n = 0
    while n < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        print(f'Question: {num_1} {num_2}')
        answer = prompt.string("Your answer: ")
        if answer == f"{gcd(num_1, num_2)}":
            print('Correct!')
            n += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{gcd(num_1, num_2)}'.")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
