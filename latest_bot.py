from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = "7941982978:AAFzj8z_fLQo0YFTf4f985Teor3r4nmnaKk"
#real madrid botti tokeni

channel = "@zayavlaustudy"

bot = Bot(token=TOKEN)
dp = Dispatcher()


user_data = {}

@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if message.text == 'Zayavka qoldirish' or message.text == '/start':
        await startapp(message)
    elif user_id not in user_data:
        await startapp(message)
    elif 'name' not in user_data[user_id]:
        await ask_phone (message)
    elif 'phone' not in user_data[user_id]:
        await ask_age( message)
    elif 'age' not in user_data[user_id]:
        await total_info ( message)



@dp.message(Command('start'))
async def startapp (message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    await message.answer(f" Assalomu alaykum ! \nIltimos ismingizni kiriting")


async def ask_phone (message: types.Message):
    user_id = message.from_user.id
    name = message.text
    user_data[user_id]['name']  = name
    button = [
    [types.KeyboardButton(text= 'Raqamni yuborish', request_contact=True)]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard= True, resize_keyboard=True)
    await message.answer(f" Iltimos telefon raqamingizni yuboring", reply_markup=keyboard)


async def ask_age (message: types.Message):
    user_id = message.from_user.id
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    user_data[user_id]['phone'] = phone
    await message.answer(f" Iltimos yoshingizni yuboring")


async def total_info (message: types.Message):
    user_id = message.from_user.id
    age = message.text
    user_data[user_id]['age'] = age
    message_text = (f" Ismingiz: {user_data[user_id]['name']}\n"
                    f"Telefon raqamingiz: {user_data[user_id]['phone']}\n"
                    f"Yoshingiz: {user_data[user_id]['age']}\n"
                    )
    button = [
        [types.KeyboardButton(text='Zayavka qoldirish')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True, resize_keyboard=True)
    await message.answer(f" Zayavka qabul qilindi!\n{message_text}", reply_markup=keyboard)
    await bot.send_message(channel, f" Yangi zayavka! \n{message_text}")
    print(user_data)
    del user_data[user_id]
    print(user_data)


async def main():
    await dp.start_polling(bot)

print("The bot is running")
asyncio.run(main())








