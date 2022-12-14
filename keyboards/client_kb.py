from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = KeyboardButton("/start")
help_button = KeyboardButton("/mem")
quiz_button = KeyboardButton("/quiz")
location_button = KeyboardButton("Share location", request_location=True)
info_button = KeyboardButton("Share info", request_contact=True)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(start_button, help_button, quiz_button)
start_markup.add(location_button, info_button)

cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(cancel_button)
