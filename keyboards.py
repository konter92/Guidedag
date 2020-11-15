from aiogram.types import ReplyKeyboardRemove, \
ReplyKeyboardMarkup, KeyboardButton, \
InlineKeyboardMarkup, InlineKeyboardButton

button0 = KeyboardButton("Категории")
button1 = KeyboardButton("Еда")
button2 = KeyboardButton("Развлечения")
button3 = KeyboardButton("Жилье")
button4 = KeyboardButton("Образование")
button5 = KeyboardButton("Прогулки")
button6 = KeyboardButton("Туризм")
button7 = KeyboardButton("Музеи")
button8 = KeyboardButton("Детям")
button9 = KeyboardButton("Бар")
button10 = KeyboardButton("Кинотеатр")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.row(button1, button2, button3)
greet_kb.row(button4, button5, button6)
greet_kb.row(button7, button8, button9)
greet_kb.row(button10)

#клавиатура еды
button_eda1 = KeyboardButton("Ресторан")
button_eda2 = KeyboardButton("Кафе")
eda_kb = ReplyKeyboardMarkup(resize_keyboard=True)
eda_kb.row(button_eda1, button_eda2)
eda_kb.row(button0)

#клавиатура детям
button_children1 = KeyboardButton("детская одежда и обувь")
button_children2 = KeyboardButton("игрушки")
button_children3 = KeyboardButton("детские клубы")
button_children4 = KeyboardButton("детские сады")
button_children5 = KeyboardButton("детские парикхмахерские")
button_children6 = KeyboardButton("развивающие центры")
children_kb = ReplyKeyboardMarkup(resize_keyboard=True)
children_kb.row(button_children1, button_children2, button_children3)
children_kb.row(button_children4, button_children5, button_children6)
children_kb.row(button0)


