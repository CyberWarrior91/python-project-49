import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_with_answer():
    action = random.choice('+' '-' '*')
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    if action == '+':
        right_answer = num_1 + num_2
    if action == '-':
        right_answer = num_1 - num_2
    if action == '*':
        right_answer = num_1 * num_2
    question = f"Question: {num_1} {action} {num_2}"
    return question, right_answer
