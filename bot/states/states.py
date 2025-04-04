from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    full_name = State()
    student_course = State()
