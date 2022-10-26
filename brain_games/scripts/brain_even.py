from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3:
        num = (randint(1, 99))
        print(f'Question: {num}' )
        answer = prompt.string('Your answer: ')
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print('Correct!')
            n += 1
        if num % 2 == 0 and answer != 'yes':
            print(f'"{answer}" is wrong answer ;(. Correct answer was "yes".')
            break
        if num % 2 != 0 and answer != 'no':
            print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
            break
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':    
    main()