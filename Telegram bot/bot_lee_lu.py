import telebot
from telebot import types

bot = telebot.TeleBot("5406426367:AAGSxv0X9HCHOMdhtjRdFop2aTsb3hj3L6E")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"<b>Мяу - мяу</b>, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"И тебе Мяу, {message.from_user.first_name}", parse_mode="html")
    elif message.text.lower() == "id":
        bot.send_message(message.chat.id, f"Твой Id {message.from_user.id}", parse_mode="html")
    else:
        bot.send_message(message.chat.id, f"Я тебя не понимаю Мяу, {message.from_user.first_name}", parse_mode="html")


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, f"Мяу, крутая фотка, {message.from_user.first_name}", parse_mode="html")


@bot.message_handler(content_types=["website"])
def get_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.youtube.com/"))
    bot.send_message(message.chat.id, f"Мяу, перейдите на сайт, {message.from_user.first_name}", parse_mode=markup)


@bot.message_handler(content_types=["help"])
def get_website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Ютуб")
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, f"Мяу, перейдите на сайт, {message.from_user.first_name}", parse_mode=markup)


bot.polling(none_stop=True)
