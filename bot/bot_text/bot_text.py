async def commandstart_text(first_name):
    return f"*Assalomu aleykum {first_name}\nTillardan birini tanlang:\n\n" \
           f"Привет, {first_name}! Выберите один из языков:\n\n" \
           f"Hello, {first_name}! Choose one of the languages:\n\n*"


async def language_text(message: str) -> str:
    if message == "🇺🇿 O'zbekcha":
        language = "uz"
        response = "*Ism Familyangizni kiriting\nNamuna: Aziz Azizov*"
    elif message == "🇷🇺 Русский":
        language = "ru"
        response = "*Введите свое имя и фамилию\nПример: Азиз Азизов*"
    elif message == "🇺🇸 English":
        language = "en"
        response = "*Enter your first and last name\nExample: Aziz Azizov*"
    return response, language
