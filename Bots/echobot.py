import telebot
# Создаем экземпляр бота (обращение к классу Телебот из модуля телебот) - у нас на компе
bot = telebot.TeleBot("5179473988:AAH3awxJ5X71sT7bJlWsg-Z6fPwo58_Ixes")
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["cat"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)