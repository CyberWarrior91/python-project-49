import random
import prompt
from brain_games.scripts.greeting.welcome_user import welcome_user


def isprime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def brain_prime():
    n = 0
    while n < 3:
        rand_num = random.randint(1, 99)
        print(f"Question: {rand_num}")
        answer = prompt.string("Answer: ")
        if isprime(rand_num) is True and answer == 'yes' or\
           isprime(rand_num) is False and answer == 'no':
            print('Correct!')
            n += 1
        elif isprime(rand_num) is True and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            break
    return n


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = brain_prime()
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
