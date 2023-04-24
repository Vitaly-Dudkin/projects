class Question:
    POINT_PER_ANSWER = 10

    def __init__(self, question=False, level_of_question=None, right_answer=None):
        self.question = question
        self.level_of_question = level_of_question
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.points = Question.POINT_PER_ANSWER * self.level_of_question

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.right_answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос {self.question}: \n' \
               f'Сложность {self.level_of_question}/5'

    def build_feedback(self):
        if self.is_correct():
            return f'Ответ верный получено {self.points} ,баллов'
        return f'Ответ не верный, верный ответ - {self.right_answer}'
