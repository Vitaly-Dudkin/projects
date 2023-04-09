import requests
from random import shuffle
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/release/anekdot/month/'
API_KEY = '6108274896:AAHlgplzoZnJ6puFc_QsaMVr1FDfJxfARQs'


def parser(url):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [c.text for c in jokes]


list_of_jokes = parser(URL)
shuffle(list_of_jokes)
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Начать'])
def say_hello(message):
    bot.send_message(message.chat.id, 'Привет! : ')


@bot.message_handler(content_types=['text'])
def get_jokes(message):
    if message.text.lower() in '1233456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите ОДНУ любую цифру')


bot.polling()
