import json


def load_students():
    """
    Загружает список студентов из файла
    :return: список словарей с данными студентов
    """
    with open('questions.json', encoding='utf-8') as students_file:
        data = json.load(students_file)
        return data


def load_professions():
    """
    Загружает список профессий из файла
    :return: список словарей с данными професий
    """
    with open('professions.json', encoding='utf-8') as professions_file:
        data = json.load(professions_file)
        return data


def get_student_by_pk(data, pk):
    """
    Распаковывает список словарей с данными студента по его pk
    :return: словарь с данными студента
    """
    for student_info in data:
        if student_info['pk'] == pk:
            return student_info


def get_profession_by_title(data, title):
    """
    Распаковывает список словарей с данными профессий по его pk
    :return: словарь с данными професии
    """
    for profession in data:
        if profession['title'] == title:
            return profession


def check_fitness(student, profession):
    """
    Получает информацию о выбранном студенте студенте и выбранной профессии
    :return: словарь в котором хранится подходящие и не достающие навыки студента
    относительно професии и его пригодность к этой профессии
    """

    my_dict = dict()
    my_dict["has"] = set(student['skills']) & set(profession['skills'])
    my_dict["lacks"] = set(profession['skills']) - set(student['skills'])
    my_dict["percent"] = int((len(my_dict["has"]) / len(profession['skills'])) * 100)
    return my_dict
