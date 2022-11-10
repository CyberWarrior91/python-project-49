from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_with_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    right_answer = str(gcd(num_1, num_2))
    question = f'{num_1} {num_2}'
    return question, right_answer
