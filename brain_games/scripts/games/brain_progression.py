import random
import prompt
from brain_games.scripts.greeting.welcome_user import welcome_user


def main():
    name = welcome_user()
    n = 0
    print("What number is missing in the progression?")
    while n < 3:
        base_num = random.randint(1, 50)
        step = random.randint(2, 7)
        str_length = random.randint(5, 10)
        range1 = list(range(base_num, base_num + step * str_length, step))
        random_index = random.randint(0, len(range1) - 1)
        miss_num = range1[random_index]
        range1[random_index] = '..'
        seq = ""
        for elem in range1:
            seq += f'{str(elem)} '
        print(f"Question: {seq}")
        answer = prompt.string('Your answer: ')
        if answer == f'{miss_num}':
            print('Correct!')
            n += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{miss_num}'.")
            break
    if n == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
