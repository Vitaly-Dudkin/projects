from dataclasses import dataclass


@dataclass
class BasicWord:
    """
    Класс представляет собой слова для игры.
    Свойствами являются исходное слово и список слов,
    составленных из исходного
    """
    word: str
    subwords: list

    def __str__(self) -> str:
        return f"Слово: {self.word}\n" \
               f"Допустимые комбинации: {self.subwords}\n"

    def check_word(self, user_word: str) -> bool:
        """Функция для проверки вхождения ответа игрока в список
        допустимых подслов"""
        return user_word in self.subwords

    def get_count_words(self) -> int:
        """Возвращает количество элементов в списке допустимых подслов"""
        return len(self.subwords)