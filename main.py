import COVID19Py
import telebot
from telebot import types

covid=COVID19Py.COVID19()
bot=telebot.TeleBot('1229612694:AAEM0N0LJfTKf8oM0SSSJJ4ErjtrJYYQedE')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    markup.add(btn1, btn2, btn3, btn4)
    send=f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id,send,parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final=""
    get_message=message.text.strip().lower()
    if get_message == "россия":
        location=covid.getLocationByCountryCode("RU")
    elif get_message == "украина":
        location=covid.getLocationByCountryCode("UA")
    elif get_message == "сша":
        location=covid.getLocationByCountryCode("US")
    elif get_message == "беларусь":
        location = covid.getLocationByCountryCode("BY")
    elif get_message == "италия":
        location=covid.getLocationByCountryCode("IT")
    else:
        location= covid.getLatest()
        final = f"<u>Данные по всему миру:</u><br><b>Заболевших:" \
                f" </b>{location['confirmed']:,}<br>" \
                f"<b>Сметрей: </b>{location['deaths']:,}"
    if final == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final= f"<u>Данные по стране:</u><br>Население: {location[0]['country_population']:,}<br>" \
                        f"Последнее обновление: {date[0]} {time[0]}<br>Последние данные:<br><b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}<br><b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"
    bot.send_message(message.chat.id, final,parse_mode='html')
bot.polling(none_stop=True)
