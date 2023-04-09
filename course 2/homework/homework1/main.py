from utils import *


def main():
    """
    Создаем главную функцию main
    """
    # просим пользовалтеля ввести номер студента
    print('Введите номер студента:')
    pk_students = int(input())
    # проверяем на наличие номера студента в списке
    if 0 < pk_students < 5:
        # распаковываем список словарей из файла и находим информацию о студенте по номеру
        student_data = get_student_by_pk(load_students(), pk_students)
        # находим имя студента и помещаем в переменную student_name
        student_name = student_data['full_name']
        # находим навыки студента и помещаем в переменную student_skill
        student_skill = student_data['skills']
        print(f'Студент {student_name}')
        print('Знает', *student_skill)
    else:
        print('У нас нет такой специальности')
        return
    # просим пользователя ввести название профессии
    profession = input(f'Выберите специальность для оценки студента {student_name}\n').strip().capitalize()
    # находим информацию о професии закидивыем ее в переменную student_profession
    student_profession = get_profession_by_title(load_professions(), profession)
    # если профессия есть в списке то выводим пригодность студента к этой профессии
    if student_profession:
        # создаем переменную has_skills кладем туда кореллирующие навыки студента и необходимые для профессии
        has_skills = check_fitness(student_data, student_profession)['has']
        # создаем переменную lacks_skills кладем туда недостающие навыки у студента для выбранной профессии
        lacks_skills = check_fitness(student_data, student_profession)['lacks']
        # cоздаем переменную percent пригодность студента для выбранной профессии
        percent = check_fitness(student_data, student_profession)['percent']
        print(f'Пригодность {percent}')
        print(student_name, 'знает', *has_skills)
        print(student_name, 'не знает', *lacks_skills)
    else:
        print('У нас нет такой специальности')


if __name__ == "__main__":
    main()
