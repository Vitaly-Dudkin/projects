# Создайте класс `Player`. Этот класс будет содержать в себе:
# **Поля:**
#
# - имя пользователя,
# - использованные слова пользователя.
#
# **Методы:**
#
# - получение количества использованных слов (возвращает int);
# - добавление слова в использованные слова (ничего не возвращает);
# - проверка использования данного слова до этого (возвращает bool).

class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f'Player(name="{self.name}", used_words={self.used_words})'

    def get_len_used_words(self):
        return len(self.used_words)

    def append_used_word(self, word):
        self.used_words.append(word)

    def check_word(self, word):
        return word in self.used_words

