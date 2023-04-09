from utils import load_random_word, lst_of_words
from class_Player import Player


def main():
    print('Введите имя игрока:')
    # создаем ЭК Player,артибуты: 1.имя(обязательный параметр) 2.пустой список(не обязательный параметр)

    user_info = Player(input().capitalize().strip())
    # создаем переменную word_subwords помещаем туда ЭК BasicWord с атрибутами word and subwords
    word_subwords = load_random_word(lst_of_words)
    STOP_WORDS = ['стоп', 'stop']
    # выаодим приветсвие и знакомим пользователя с правилами игры
    print(f'Привет, {user_info.name}\n'
          f'Составьте {len(word_subwords.subwords)} слов из слова {word_subwords.word}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
          f'Поехали, ваше первое слово?')

    # запускаем осоновной цикл
    # цикл работает пока длина пустого списка (артибут ЭК Player) не будет равна списку слов которые можно использовать
    while len(user_info.used_words) != len(word_subwords.subwords):
        # пользователь вводит слово
        word = input().lower().strip()
        # если слово уже в списке оповещаем об этом игрока
        if user_info.check_word(word):
            print("уже использовано")
        # если слово в аррибуте ЭК BasicWord то игрок верно ввел слово
        elif word in word_subwords.subwords:
            # добаляем слово список чтобы его нельзя было больше использовать
            user_info.append_used_word(word)
            print('верно')
        # если слово меньше 3х букв то напоминаем пользователю правила игры
        elif len(word) < 3:
            print('слишком короткое слово')
        # если игрок напишет стоп или stop прерывем игру
        elif word in STOP_WORDS:
            break
        # выводим неверно во всех остальных случаях
        else:
            print('неверно')

    # Выводим статистику по результатам игры
    print(f'Игра завершена, вы угадали {len(user_info.used_words)} слов!')


if __name__ == "__main__":
    main()
