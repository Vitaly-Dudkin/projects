import json
from question_class import Question


def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item["q"]
        level_of_question = int(item['d'])
        right_answer = item['a']
        question = Question(text, level_of_question, right_answer)
        questions.append(question)

    return questions


def build_statistics(questions):
    points = 0
    count = 0
    for question in questions:
        if question.is_correct():
            points *= question.points
            count += 1
    return f'Вот и всё! \n' \
           f'Отвечено {count} вопроса из 10\n' \
           f'Набрано баллов: {points}'
