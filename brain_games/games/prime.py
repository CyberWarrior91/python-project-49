from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isprime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def get_question_with_answer():
    rand_num = randint(1, 99)
    if isprime(rand_num) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f"Question: {rand_num}"
    return question, right_answer
