import telebot
import requests
from telebot import types

bot = telebot.TeleBot("5179473988:AAH3awxJ5X71sT7bJlWsg-Z6fPwo58_Ixes")
# Команда start
"""@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#one_time_keyboard=True
    item1 = types.KeyboardButton("Ru")
    item2 = types.KeyboardButton("Eng")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Выбери язык, на котором ты хотел бы получить оскорбления', reply_markup=markup)
    #bot.edit_message_reply_markup(reply_markup=None)"""
@bot.message_handler(commands=['start'])
def lang(m, res=False):
        # Добавляем кнопку
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3=types.KeyboardButton("Оскорбиться")
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: Оскорбиться для генерации унижений в твою честь',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle(message):
    if message.text.strip() == 'Оскорбиться':
        #отправить запрос сайту с оскорблениями https://evilinsult.com/generate_insult.php?lang=en&type=json
        #получить ответ от сайта get
        res = requests.get('https://evilinsult.com/generate_insult.php?lang=ru&type=json')
        #Открыть json и забрать оттуда поле  с названием insult res.json()["insult"]
        #отправить ответ от сайта в тг бота
        bot.send_message(message.chat.id, res.json()["insult"])
    else:
        bot.send_message(message.chat.id,'Нажми: Оскорбиться для генерации унижений в твою честь')


bot.polling(none_stop=True, interval=0)




