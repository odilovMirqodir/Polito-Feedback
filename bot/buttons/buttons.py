from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def language_button():
    uz_button = KeyboardButton(text="🇺🇿 O'zbekcha")
    ru_button = KeyboardButton(text="🇷🇺 Русский")
    eng_button = KeyboardButton(text="🇺🇸 English")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [uz_button],
            [ru_button],
            [eng_button]
        ],
        resize_keyboard=True
    )

    return keyboard
