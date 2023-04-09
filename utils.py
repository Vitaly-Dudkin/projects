import requests
from random import choice
from basicword import BasicWord


def load_random_word(link: str):
    """
    Возвращает объект класса BasicWord со свойствами, получаемыми
    из файла JSON, расположенного по внешней ссылке
    :param link: ссылка на файл
    """
    web_json = requests.get(link).json()
    field_1, field_2 = choice(web_json).values()
    return BasicWord(field_1, field_2)


def get_ending(count: int, word: str) -> str:
    """
    Возвращает слово с грамматически корректным
    для введенного количества окончанием
    :param count: количество
    :param word: слово для изменения окончания
    """
    exceptions = ["11", "12", "13", "14"]
    remain = str(count % 100)

    if remain[-1] == "1" and remain not in exceptions:
        return word + "о"
    elif remain[-1] in ["2", "3", "4"] and remain not in exceptions:
        return word + "а"

    return word