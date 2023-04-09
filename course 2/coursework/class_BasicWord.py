# Создайте класс `BasicWord` в отдельном файле.
# Этот класс будет содержать в себе:
#
# **Поля:**
#
# - исходное слово,
# - набор допустимых подслов.
#
# **Методы:**
#
# - проверку введенного слова в списке допустимых подслов (вернет bool),
# - подсчет количества подслов (вернет int).
#
# Не забудьте определить метод  `__repr__`
#
# **При инициализации** экземпляру задаются:
# **исходное слово** и набор **допустимых слов,** составленных из исходного. ****


class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'BasicWord(word="{self.word}", subwords={self.subwords} '

    def check_word(self, word):
        return word in self.subwords

    def get_len_subwords(self):
        return len(self.subwords)
