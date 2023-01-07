from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

hello = types.KeyboardButton('Привет')
photo = types.KeyboardButton('Отправить фото')

start.add(hello, photo)

photo = types.ReplyKeyboardMarkup(resize_keyboard=True)
photo.add(KeyboardButton('Да'))
photo.add(KeyboardButton('Нет'))
