from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    questions_answers: State = State()
    contacts: State = State()
    question: State = State()
