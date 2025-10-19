import telebot
import requests
from telebot import types

token = "7941982978:AAFzj8z_fLQo0YFTf4f985Teor3r4nmnaKk"
API = " "
bot = telebot.TeleBot(token)
#

@bot.message_handlers(commands= ["start"])
def start (message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("GBP", callback_data="GBP"),
               types.InlineKeyboardButton("USD", callback_data="USD"),
               types.InlineKeyboardButton("RUB", callback_data="RUB"))
    bot.send_message(message.chat.id, "Choose your currency", reply_markup=markup)


@bot.callback_query_handlers(func=lambda call:True)
def callback_query(call):
    querystring = {"from": call.data, "to": "UZS", "amount": "1"}

    headers = {
        "X-RapidApi-Key":
        "X-RapidApi-Host"
    }
    response = requests.get(API, headers = headers, params= querystring)
    if response.status_code == 200:
        data = response.json()
        print(data)  # to check the results
        conversion_result = data.get("result")
        if conversion_result:
            bot.send_message(call.message.chat.id, f"Conversion result:{conversion_result}")
        else:
            bot.send_message(call.message.chat.id, f" Could not retrieve conversion result")

    else:
        bot.send_message(call.message.chat.id, f" Failed to confirm conversion. pls try again later.")


bot.polling()









