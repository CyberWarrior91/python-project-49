import random
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_question_with_answer():
    operations = (('+', operator.add), ('-', operator.sub), ('*', operator.mul))
    operator_name, operator_method = random.choice(operations)
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    question = f"{num_1} {operator_name} {num_2}"
    right_answer = str(operator_method(num_1, num_2))
    return question, right_answer
