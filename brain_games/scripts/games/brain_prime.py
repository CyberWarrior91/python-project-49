import random
import prompt
from brain_games.scripts.greeting.welcome_user import welcome_user
import sympy


def main():
    name = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    n = 0
    while n < 3:
        rand_num = random.randint(1, 99)
        print(f'Question: {rand_num}')
        answer = prompt.string("Answer: ")
        if sympy.isprime(rand_num) is True and answer == 'yes' or\
           sympy.isprime(rand_num) is False and answer == 'no':
            print('Correct!')
            n += 1
        elif sympy.isprime(rand_num) is True and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
