import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1229612694:AAEM0N0LJfTKf8oM0SSSJJ4ErjtrJYYQedE')

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('Во всём мире')
	btn2 = types.KeyboardButton('Украина')
	btn3 = types.KeyboardButton('Россия')
	btn4 = types.KeyboardButton('Беларусь')
	markup.add(btn1, btn2, btn3, btn4)

	send_message = f"Привет {message.from_user.first_name}!/n Чтобы узнать данные про коронавируса напишите " \
		f"название страны, например: США, Украина, Россия и так далее"
	bot.send_message(message.chat.id, send_message, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "украина":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "беларусь":
		location = covid19.getLocationByCountryCode("BY")
	elif get_message_bot == "казакхстан":
		location = covid19.getLocationByCountryCode("KZ")
	elif get_message_bot == "италия":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "франция":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "германия":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "япония":
		location = covid19.getLocationByCountryCode("JP")
	else:
		location = covid19.getLatest()
	final_message = f"Данные по всему миру:\n Заболевших:{location['confirmed']:,}Сметрей:{location['deaths']}"

	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"Данные по стране: \n Население: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\n Последние данные:\n" \
				f"Заболевших:{location[0]['latest']['confirmed']:,}\n Сметрей: " \
				f"{location[0]['latest']['deaths']:,}"

	bot.send_message(message.chat.id, final_message)


bot.polling(none_stop=True)
