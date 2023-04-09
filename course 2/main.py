from utils import load_file, build_statistics
import random
if __name__ == '__main__':
    PATH_TO_JSON_FILE = 'questions.json'
    questions = load_file(PATH_TO_JSON_FILE)

    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input('Ваш ответ')
        question.user_answer = user_answer
        print(question.build_feedback())

    print(build_statistics(questions))
