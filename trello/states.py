# from telebot.handler_backends import StatesGroup, State
#
#
# class CreateNewTask(StatesGroup):
#     board = State()
#     list = State()
#     name = State()
#     description = State()
#     members = State()
#     labels = State()
#     date = State()

a = {"en": "Airbus A319-100", "ru": "Аэробус A319-100"}
s = 'en'
for i in a:
    if i == s:
        print(a[i])