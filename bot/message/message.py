from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot_text.bot_text import *
from buttons.buttons import *
from aiogram.types import ReplyKeyboardRemove
from requests.requests import Requests
from states.states import Form

message_router = Router(name=__name__)
request = Requests()


@message_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    await message.answer(await commandstart_text(first_name), reply_markup=await language_button(),
                         parse_mode='markdown')
    await request.check_student_or_add(user_id)


@message_router.message(lambda message: message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇺🇸 English"])
async def select_language_handler(message: Message, state: FSMContext) -> None:
    chat_id = message.from_user.id
    response = await language_text(message.text)
    await request.add_student_language(chat_id, response[1])
    await message.answer(f"{response[0]}", parse_mode='markdown', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.full_name)


@message_router.message(Form.full_name)
async def process_name(message: Message, state: FSMContext) -> None:
    user_id = message.chat.id
    get_language = await request.get_user_language(user_id)
    language = get_language.get('language')
    if len(message.text.split(' ')) == 2:
        await state.update_data(full_name=message.text)
        await state.set_state(Form.student_course)
    else:
        pass
