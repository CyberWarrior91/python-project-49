from random import randint


DESCRIPTION = "What number is missing in the progression?"


def get_question_with_answer():
    base_num = randint(1, 50)
    step = randint(2, 7)
    str_length = randint(5, 10)
    range1 = list(range(base_num, base_num + step * str_length, step))
    random_index = randint(0, len(range1) - 1)
    miss_num = range1[random_index]
    range1[random_index] = '..'
    seq = ""
    for elem in range1:
        seq += f'{str(elem)} '
    question = f"Question: {seq}"
    right_answer = miss_num
    return question, right_answer
