import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import telebot
TOKEN = "5713334456:AAHrZykC9kpmWY1l1IngK7XVDrE9OSawxbw"
MSG = "программировал ли ты сегодня, {}"                                   # Пустое место чтобы вставить имя пользователя

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

value = ""
old_value = ""
# keyboard = types.KeyboardButtonPollType()

# Button1 = types.KeyboardButtonPollType(" ", callback_data = "no"),
# Button2 = types.KeyboardButtonPollType("C", callback_data = "C"),
# Button3 = types.KeyboardButtonPollType("<=", callback_data = "<="),
# Button4 = types.KeyboardButtonPollType("/", callback_data = "/"),
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row( telebot.types.InlineKeyboardButton(" ", callback_data = "no"),
              telebot.types.InlineKeyboardButton("C", callback_data = "C"),
              telebot.types.InlineKeyboardButton("<=", callback_data = "<="),
              telebot.types.InlineKeyboardButton("/", callback_data = "/"))
keyboard.row( telebot.types.InlineKeyboardButton("7", callback_data = "7"),
              telebot.types.InlineKeyboardButton("8", callback_data = "8"),
              telebot.types.InlineKeyboardButton("9", callback_data = "9"),
              telebot.types.InlineKeyboardButton("*", callback_data = "*"))
keyboard.row( telebot.types.InlineKeyboardButton("4", callback_data = "4"),
              telebot.types.InlineKeyboardButton("5", callback_data = "5"),
              telebot.types.InlineKeyboardButton("6", callback_data = "6"),
              telebot.types.InlineKeyboardButton("-", callback_data = "-"))
keyboard.row( telebot.types.InlineKeyboardButton("1", callback_data = "1"),
              telebot.types.InlineKeyboardButton("2", callback_data = "2"),
              telebot.types.InlineKeyboardButton("3", callback_data = "3"),
              telebot.types.InlineKeyboardButton("+", callback_data = "+")) 
keyboard.row( telebot.types.InlineKeyboardButton(" ", callback_data = "no"),
              telebot.types.InlineKeyboardButton("=", callback_data = "="),
              telebot.types.InlineKeyboardButton("0", callback_data = "0"),
              telebot.types.InlineKeyboardButton(".", callback_data = "."))             

@dp.message_handler(commands=['start'])                                    # когда поступает команда start
async def start_handler(message: types.Message):                           # асинхронная библиотека
    user_id = message.from_user.id 
    user_name = message.from_user.first_name                               # получаем ид юзера (из его же сообщения)
    user_full_name = message.from_user.full_name                           # И его имя
    logging.info(f"{user_id=}, {user_full_name=}, {time.asctime()}")       # Записываем в лог ид, имя и текущее время.

    await message.reply(f"Добра, {user_full_name}!")

    for i in range(10):
        time.sleep(10)
        await bot.send_message(user_id, MSG.format(user_name))

@dp.message_handler(commands=['calculater'])                                    
async def start_handler(message: types.Message):  
    global value                       
    user_id = message.from_user.id 
    user_name = message.from_user.first_name                               
    user_full_name = message.from_user.full_name                           
    logging.info(f"{user_id=}, {user_full_name=}, {time.asctime()}")       
    if value == "":
          bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)
    await message.reply(f"Давай подсчитаю,  раз сам не можешь =) {user_full_name}!")
    await bot.send_message(user_id, reply_markup=keyboard)

@dp.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == "no":
        pass
    elif data == "C":
        value = ""
    elif data == "=":
        value = str(eval(value))
    else:
        value += data
    if value != old_value:
        if value == "":
            dp.edit_message_text(chat_id = query.message.chat.id, message_id = query.message.message_id, text = "0", reply_markup=keyboard)
        else:
            dp.edit_message_text(chat_id = query.message.chat.id, message_id = query.message.message_id, text = value, reply_markup=keyboard)
    old_value = value

    




if __name__ == "__main__":                                                  # на питоне name всегда равен main( это типа true мира пайтон, булевое значение)
    executor.start_polling(dp)                                              # запускаем нашего бота в сеть



# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# TOKEN = "5713334456:AAHrZykC9kpmWY1l1IngK7XVDrE9OSawxbw"
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)


# if __name__ == '__main__':
#     executor.start_polling(dp)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(msg: types.Message):
#     await msg.reply_to_message ("Я бот. Приятно познакомиться, {msg.from_user.first_name}")

# @dp.message_handler(content_types=['text'])
# async def get_text_messages(msg: types.Message):
#    if msg.text.lower() == 'привет':
#        await msg.answer('Привет!')
#    else:
#        await msg.answer('Не понимаю, что это значит.')
