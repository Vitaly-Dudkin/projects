class Player:
    """Класс представляет собой описание игрока.
    Свойствами являются имя и список отгаданных слов"""

    def __init__(self, user_name: str) -> None:
        self.user_name = user_name
        self.used_words = []

    def __str__(self) -> str:
        return f"Пользователь: {self.user_name}\n" \
               f"Использовал слова: {self.used_words}\n"

    def __repr__(self) -> str:
        return f"Player(user_name='{self.user_name}', " \
               f"used_words={self.used_words})"

    def get_count_words(self) -> int:
        """Возвращает количество элементов в списке отгаданных слов"""
        return len(self.used_words)

    def add_word(self, word: str) -> None:
        """Добавляет слово в список отгаданных"""
        self.used_words.append(word)

    def check_repeat(self, word: str) -> bool:
        """Проверяет, было ли это слово уже отгадано"""
        return word in self.used_words
