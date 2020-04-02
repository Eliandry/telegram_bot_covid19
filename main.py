import telebot
bot = telebot.TeleBot('1229612694:AAEM0N0LJfTKf8oM0SSSJJ4ErjtrJYYQedE')
@bot.message_handler(content_types=['text'])
def lala(message):
	bot.send_message(message.chat.id,message.text)
#RUN
bot.polling(none_stop=True)
