from random import randint


DESCRIPTION = "What number is missing in the progression?"


def get_question_with_answer():
    start = randint(1, 50)
    step = randint(2, 7)
    length = randint(5, 10)
    progression = list(range(start, start + step * length, step))
    random_index = randint(0, len(progression) - 1)
    right_answer = str(progression[random_index])
    progression[random_index] = '..'
    seq = ' '.join(map(str, progression))
    question = f"{seq}"
    return question, right_answer
