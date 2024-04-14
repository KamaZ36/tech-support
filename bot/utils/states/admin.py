from aiogram.fsm.state import State, StatesGroup


class Admin(StatesGroup):
    admin_panel: State = State()


class AddNewQuestion(StatesGroup):
    waiting_question: State = State()
    waiting_answer: State = State()


class DeleteQuestion(StatesGroup):
    waiting_question_id: State = State()


class EditContacts(StatesGroup):
    waiting_contact_title: State = State()
