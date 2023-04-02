from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext

from lab2.ioc_container import ioc
from ..states import UserStates
from ..text_message import *
from lab2.service import UserService

dp = ioc.get_instance(Dispatcher)
service = ioc.get_instance(UserService)


GREETING_PATIENT = 'Привет, я бот онлайн-записей в БУЗОО "ГКФБ №1"'
PATIENT_MENU = "Выберите действия:\n1. Получить все свои записи\n2. Записаться к врачу"
MISSING_NOTE = "Доступные записи:"
MY_NOTE = "Вы записаны:"
ERROR_MENU = "Ошибка меню, повторите попытку"


@dp.message_handler(state='*', commands=['start', 'restart'])
async def process_start_command(message: types.Message, state: FSMContext):
    await message.reply(GREETING_PATIENT, reply=False)
    await message.reply(PATIENT_MENU, reply=False)

    await UserStates.wait_log.set()


@dp.message_handler(state=UserStates.wait_log)
async def get_cap_e(message: types.Message, state: FSMContext):
    if str(message.text).strip() == "1":
        result = service.get_my_notes(message.from_user.id)
        await message.reply(MISSING_NOTE, reply=False)
        await message.reply(result, reply=False)
    elif str(message.text).strip() == "2":

        await UserStates.wait_add_note.set()
    else:
        await message.reply(ERROR_MENU, reply=False)
        await message.reply(PATIENT_MENU, reply=False)


@dp.message_handler(state=UserStates.wait_get_note)
async def get_user_notes(message: types.Message, state: FSMContext):
    pass
