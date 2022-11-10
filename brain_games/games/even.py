from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_with_answer():
    num = (randint(1, 99))
    right_answer = 'yes' if num % 2 == 0 else 'no'
    question = num
    return question, right_answer
