import asyncio
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
import keyboard
import logging

storage = MemoryStorage()
bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(filename='log.txt', filemode='a',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


class Me_info(StatesGroup):
    S1 = State()
    S2 = State()
    S3 = State()


@dp.message_handler(text_contains='Отправить фото', state=None)
async def enter_me_info(message: types.Message):
    await message.answer("Перетените свое фото на экран")
    await Me_info.S1.set()  # начинает ждать наш ответ, задав состояние Q1


@dp.message_handler(content_types=['photo'], state=Me_info.S1)
async def answer_for_state_S1(message: types.Message, state: FSMContext):
    answer = message.photo[-1].file_id
    await state.update_data(answer1=answer)
    await message.answer("Ваше фото получено")
    await Me_info.S2.set()
    await message.answer("Отправте подпись к фотографии")


@dp.message_handler(state=Me_info.S2)
async def answer_for_state_S2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Подпись получена")
    await Me_info.S3.set()
    await bot.send_message(message.chat.id, "Желаете ли сохранить фото", reply_markup=keyboard.photo, parse_mode='Markdown')


@dp.message_handler(state=Me_info.S3)
async def answer_for_state_S3(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        data = await state.get_data()
        # достаем значение по ключу answer1
        answer1 = data.get("answer1")
        # достаем значение по ключу answer2
        answer2 = data.get("answer2")
        await bot.download_file_by_id(answer1, destination=f'D:\Пайтон\pythonProject practic\Photo\{answer2}.jpg')
        await message.answer("Фото сохранено")
    else:
        await message.answer("Фото не сохранено")
    await state.finish()


@dp.message_handler(Command('start'), start=None)
async def welcome(message):
    await bot.send_message(message.chat.id, text='бот работает', reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(text_contains='Привет')
async def cmd_test1(message: types.Message):
    await message.answer(f'Привет!!! {message.chat.username}')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
