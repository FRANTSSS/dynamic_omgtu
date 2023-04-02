from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext

from ioc_container import ioc
from ..states import UserStates
from ..text_message import *
from service import (
    UserService,
    UserServiceError
)

dp = ioc.get_instance(Dispatcher)
service = ioc.get_instance(UserService)


@dp.message_handler(state='*', commands=['start', 'restart'])
async def process_start_command(message: types.Message, state: FSMContext):
    await message.reply(GREETING_PATIENT, reply=False)
    await message.reply(PATIENT_MENU, reply=False)
    await UserStates.wait_log.set()


@dp.message_handler(state=UserStates.wait_log)
async def get_cap_e(message: types.Message, state: FSMContext):
    if str(message.text).strip() == "1":
        results = await service.get_my_notes(message.from_user.id)
        if len(results) == 0:
            await message.reply(NOT_FOUND_NOTES, reply=False)
            await message.reply(PATIENT_MENU, reply=False)
        else:
            await message.reply(MISSING_NOTE, reply=False)
            for result in results:
                await message.reply(str(result), reply=False)
    elif str(message.text).strip() == "2":
        results = await service.get_free_notes()
        if len(results) == 0:
            await message.reply(NOT_FOUND_NOTES, reply=False)
            await message.reply(PATIENT_MENU, reply=False)
        else:
            await message.reply(MISSING_NOTE, reply=False)
            for result in results:
                await message.reply(str(result), reply=False)
            await state.update_data(temporary_notes=results)
            await UserStates.wait_add_note.set()
    else:
        await message.reply(ERROR_MENU, reply=False)
        await message.reply(PATIENT_MENU, reply=False)


@dp.message_handler(state=UserStates.wait_get_note)
async def add_user_notes(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    temporary_notes = user_data.get("temporary_notes")
    result_number = int(str(message.text).strip())
    if 0 < result_number <= len(temporary_notes):
        note = temporary_notes[result_number-1]
        try:
            await service.add_my_note(message.from_user.id, note)
            await message.reply(SUCCESS_OPER, reply=False)
            await message.reply(PATIENT_MENU, reply=False)
        except UserServiceError:
            await message.reply(NOT_FOUND_NOTES, reply=False)
            await message.reply(PATIENT_MENU, reply=False)
    else:
        await message.reply(ERROR_MENU, reply=False)
        await message.reply(PATIENT_MENU, reply=False)
    await UserStates.wait_log.set()
