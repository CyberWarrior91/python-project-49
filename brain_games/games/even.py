from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_with_answer():
    num = (randint(1, 99))
    if num % 2 == 0:
        right_answer = 'yes'
    if num % 2 != 0:
        right_answer = 'no'
    question = f"Question: {num}"
    return question, right_answer
