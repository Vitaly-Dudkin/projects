import requests
from random import choice
from class_BasicWord import BasicWord

URL_TO_JSON = 'https://api.npoint.io/ee7d84b19cfec455515a'


def load_words(url):
    data = requests.get(url).json()
    return data


lst_of_words = load_words(URL_TO_JSON)


def load_random_word(lst_words):
    dict_words = choice(lst_words)
    word, subwords = dict_words.values()
    words = BasicWord(word.upper(), subwords)
    return words

# Напишите функцию `load_random_word()` в файле `utils`, которая:
# - получит список слов с внешнего ресурса,
# - выберет случайное слово,
# - создаст экземпляр класса `BasicWord`,
# - вернет этот экземпляр.
