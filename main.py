import telebot  # подключаем библиотеку Telebot

bot = telebot.TeleBot("1839577526:AAH4b0aBNxlHDR7kF2kTl_X7J0xHem2BXXc") # подключаем Token бота


@bot.message_handler(commands=['start'])  # бот отвечает на команды
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, я Аналитик.")

@bot.message_handler(commands=['help'])  # бот відповідає на команди
def send_welcome(message):
	bot.send_message(message.chat.id, "Команди📃\n\n /weather - Погода 🌤 \n /analitik - Аналитика чата📈 \n \n  Мои создатели🤓: \nПідвисоцький Назарій (@IQemc2) \nПінчук Аркадій (@arkad1y_5)" )

@bot.message_handler(func=lambda message: True)    # ехо
def echo_all(message):
	if message.text == 'Привет бот': # если смс "привет", то вывод следующий:
		bot.reply_to(message, 'Привет, создатель')
	elif message.text == 'Как дела?':
		bot.reply_to(message, 'Бывало и покруче')


bot.polling() # чтобы бот не завершал работу
# 23.05.2021 12:16 перевёл на русский и поправил немного код по PEP8
