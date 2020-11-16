import logging
import os
import keyboards as kb

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ['TOKEN']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#/основные хендлеры
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЯ-твой гид по городу!\nНапиши мне, что бы ты хотел узнать или выбери категорию на клавиатуре", reply_markup=kb.greet_kb)
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("Я могу подсказать тебе по следующим категориям\n/food - здесь список ресторанов и кафе\n/entertainments - здесь список кинотеатров и т.д.\n/housing - здесь список гостиниц\n/education - здесь список образовательных учреждений\n/strolls - здесь список мест куда можно сходить\n/tourism - здесь список мест кудо можно съездить\n/museums - здесь список музеев\n/children - здесь всё для детей\n/bar - здесь список баров\n/cinema - кинотеатр", reply_markup=kb.greet_kb)

@dp.message_handler(lambda message: message.text.lower() == "категории")
async def send_answer(message: types.Message):
    await message.answer("Напиши мне, что бы ты хотел узнать или выбери категорию на клавиатуре",  reply_markup=kb.greet_kb)

#хенделр на театр
@dp.message_handler(commands=['teatr'])
async def send_help(message: types.Message):
    await message.answer("/lezgi_teatr - Музыкально-драматический театр им. Сулеймана Стальского\n/tabasaran_teatr - Табасарнский драматический тетар\n/tatskiy_teatr - татский театр\n",  reply_markup=kb.greet_kb)

@dp.message_handler(lambda message: message.text.lower() == "театр")
async def send_answer(message: types.Message):
    await message.answer("/lezgi_teatr - Музыкально-драматический театр им. Сулеймана Стальского\n/tabasaran_teatr - Табасарнский драматический тетар\n/tatskiy_teatr - татский театр\n",  reply_markup=kb.greet_kb)
#хендлер для Сайт театра

inline_btn_lezgi_teatr = InlineKeyboardButton('Сайт театра', url='http://www.лезги-театр.рф/')
inline_lezgi_teatr = InlineKeyboardMarkup().add(inline_btn_lezgi_teatr)

@dp.message_handler(commands=['lezgi_teatr'])
async def send_answer(message: types.Message):
    await message.answer('Музыкально-драматический театр им. Сулеймана Стальского\nВремя работы: пн-пт с 09.00 до 17.00 перерыв с 13.00 до 14.00 сб с 09.00 до 13.00\nКонтакты: Директор : 4-27-60 \nАдрес: ул. Буйнакского, д. 49Б', reply_markup=inline_lezgi_teatr)

@dp.message_handler(lambda message: message.text.lower() == 'лезгинский театр')
async def send_answer(message: types.Message):
    await message.answer('Музыкально-драматический театр им. Сулеймана Стальского\nВремя работы: пн-пт с 09.00 до 17.00 перерыв с 13.00 до 14.00 сб с 09.00 до 13.00\nКонтакты: Директор : 4-27-60 \nАдрес: ул. Буйнакского, д. 49Б', reply_markup=inline_lezgi_teatr)


#хендлер для Инстаграам театра

inline_btn_tabasaran_teatr = InlineKeyboardButton('Инстаграам театра', url='https://www.instagram.com/tabasaran_teatr/')
inline_tabasaran_teatr = InlineKeyboardMarkup().add(inline_btn_tabasaran_teatr)

@dp.message_handler(commands=['tabasaran_teatr'])
async def send_answer(message: types.Message):
    await message.answer('Табасарнский драматический тетар\nВремя работы: пн-пт с 09.00 до 18.00 перерыв с 13.00 до 14.00\nКонтакты: +78724041141\nАдрес: ул. Пашабекова, д. 15', reply_markup=inline_tabasaran_teatr)

@dp.message_handler(lambda message: message.text.lower() == 'Табасаранский театр')
async def send_answer(message: types.Message):
    await message.answer('Табасарнский драматический тетар\nВремя работы: пн-пт с 09.00 до 18.00 перерыв с 13.00 до 14.00\nКонтакты: +78724041141\nАдрес: ул. Пашабекова, д. 15', reply_markup=inline_tabasaran_teatr)


#хендлер для Инстаграам театра

inline_btn_tatskiy_teatr = InlineKeyboardButton('Инстаграам театра', url='https://www.instagram.com/tatskiy_teatr_/')
inline_tatskiy_teatr = InlineKeyboardMarkup().add(inline_btn_tatskiy_teatr)

@dp.message_handler(commands=['tatskiy_teatr'])
async def send_answer(message: types.Message):
    await message.answer('Татский театр\nВремя работы: пн-пт с 08.00 до 17.00\nКонтакты: +79288074359\nАдрес: ул. Пашабекова, д. 3', reply_markup=inline_tatskiy_teatr)

@dp.message_handler(lambda message: message.text.lower() == 'татский театр')
async def send_answer(message: types.Message):
    await message.answer('Татский театр\nВремя работы: пн-пт с 08.00 до 17.00\nКонтакты: +79288074359\nАдрес: ул. Пашабекова, д. 3', reply_markup=inline_tatskiy_teatr)


# хендлер на еду
@dp.message_handler(commands=['food'])
async def send_help(message: types.Message):
    await message.answer("Выберите куда хотите пойти",  reply_markup=kb.eda_kb)

@dp.message_handler(lambda message: message.text.lower() == "еда")
async def send_answer(message: types.Message):
    await message.answer("Выберите куда хотите пойти",  reply_markup=kb.eda_kb)
    
# хендлер на ресторан
@dp.message_handler(commands=['restoran'])
async def send_help(message: types.Message):
    await message.answer("/oazis - ресторан Оазис. Восточная и Европейская кухня\n/alie_parusa - ресторан Алые Паруса. Восточная и Европейская и Японская кухни. Есть караоке :)\n/hayal - ресторан Hayal. Восточная и Европейская кухни. Музыкальные концерты\n/shahristan - ресторан Шахристан. Восточной и Европейской кухни\n/kosmos - ресторан Космос. Восточная и Европейская кухня\n/fregat - семейный ресторан Фрегат.\n/skazka - ресторан Сказка. Восточная и Европейская кухня. Караоке\n/gulistan - ресторан Гюлестан.\n",  reply_markup=kb.eda_kb)

@dp.message_handler(lambda message: message.text.lower() == "ресторан")
async def send_answer(message: types.Message):
    await message.answer("/oazis - ресторан Оазис. Восточная и Европейская кухня\n/alie_parusa - ресторан Алые Паруса. Восточная и Европейская и Японская кухни. Есть караоке :)\n/hayal - ресторан Hayal. Восточная и Европейская кухни. Музыкальные концерты\n/shahristan - ресторан Шахристан. Восточной и Европейской кухни\n/kosmos - ресторан Космос. Восточная и Европейская кухня\n/fregat - семейный ресторан Фрегат.\n/skazka - ресторан Сказка. Восточная и Европейская кухня. Караоке\n/gulistan - ресторан Гюлестан.\n",  reply_markup=kb.eda_kb)
#хендлер для Инстаграм ресторана Оазис

inline_btn_oazis = InlineKeyboardButton('Инстаграм ресторана Оазис', url='https://www.instagram.com/oazis.derbent/')
inline_oazis = InlineKeyboardMarkup().add(inline_btn_oazis)

@dp.message_handler(commands=['oazis'])
async def send_answer(message: types.Message):
    await message.answer('Оазис\nВремя работы: с 10.00 до 23.00\nКонтакты: 89894495555\nАдрес: ул. Шеболдаева, д. 1', reply_markup=inline_oazis)

@dp.message_handler(lambda message: message.text.lower() == 'оазис')
async def send_answer(message: types.Message):
    await message.answer('Оазис\nВремя работы: с 10.00 до 23.00\nКонтакты: 89894495555\nАдрес: ул. Шеболдаева, д. 1', reply_markup=inline_oazis)


#хендлер для Инстаграм ресторана Алые Паруса

inline_btn_alie_parusa = InlineKeyboardButton('Инстаграм ресторана Алые Паруса', url='https://www.instagram.com/alie_parusa/')
inline_alie_parusa = InlineKeyboardMarkup().add(inline_btn_alie_parusa)

@dp.message_handler(commands=['alie_parusa'])
async def send_answer(message: types.Message):
    await message.answer('Алые Паруса\nВремя работы: до 23.00\nКонтакты: 89637983322\nАдрес: ул. Локомотивная, д. 5', reply_markup=inline_alie_parusa)

@dp.message_handler(lambda message: message.text.lower() == 'алые паруса')
async def send_answer(message: types.Message):
    await message.answer('Алые Паруса\nВремя работы: до 23.00\nКонтакты: 89637983322\nАдрес: ул. Локомотивная, д. 5', reply_markup=inline_alie_parusa)


#хендлер для Инстаграм ресторана Hayal

inline_btn_hayal = InlineKeyboardButton('Инстаграм ресторана Hayal', url='https://www.instagram.com/hayal_restoran_derbent/')
inline_hayal = InlineKeyboardMarkup().add(inline_btn_hayal)

@dp.message_handler(commands=['hayal'])
async def send_answer(message: types.Message):
    await message.answer('Hayal\nВремя работы: с 11.00 до 23.00\nКонтакты: 89637934912\nАдрес: ул. 3-го Интернационала, д. 4а', reply_markup=inline_hayal)

@dp.message_handler(lambda message: message.text.lower() == 'хаял')
async def send_answer(message: types.Message):
    await message.answer('Hayal\nВремя работы: с 11.00 до 23.00\nКонтакты: 89637934912\nАдрес: ул. 3-го Интернационала, д. 4а', reply_markup=inline_hayal)


#хендлер для Инстаграм ресторана Шахристан

inline_btn_shahristan = InlineKeyboardButton('Инстаграм ресторана Шахристан', url='https://www.instagram.com/shahristan_derbent_/')
inline_shahristan = InlineKeyboardMarkup().add(inline_btn_shahristan)

@dp.message_handler(commands=['shahristan'])
async def send_answer(message: types.Message):
    await message.answer('Шахристан\nВремя работы: с 10.00 до 22.30\nКонтакты: 89689922226\nАдрес: ул. Гейдара Алиева, д. 15', reply_markup=inline_shahristan)

@dp.message_handler(lambda message: message.text.lower() == 'шахристан')
async def send_answer(message: types.Message):
    await message.answer('Шахристан\nВремя работы: с 10.00 до 22.30\nКонтакты: 89689922226\nАдрес: ул. Гейдара Алиева, д. 15', reply_markup=inline_shahristan)


#хендлер для Инстаграм ресторана Космос

inline_btn_kosmos = InlineKeyboardButton('Инстаграм ресторана Космос', url='https://www.instagram.com/kosmos_derbent/')
inline_kosmos = InlineKeyboardMarkup().add(inline_btn_kosmos)

@dp.message_handler(commands=['kosmos'])
async def send_answer(message: types.Message):
    await message.answer('Космос\nВремя работы: до 23.00\nКонтакты: 89285770404\nАдрес: ул. Чапаева, д. 23а', reply_markup=inline_kosmos)

@dp.message_handler(lambda message: message.text.lower() == 'космос')
async def send_answer(message: types.Message):
    await message.answer('Космос\nВремя работы: до 23.00\nКонтакты: 89285770404\nАдрес: ул. Чапаева, д. 23а', reply_markup=inline_kosmos)


#хендлер для Инстаграм ресторана Фрегат

inline_btn_fregat = InlineKeyboardButton('Инстаграм ресторана Фрегат', url='https://www.instagram.com/derbent_fregat/')
inline_fregat = InlineKeyboardMarkup().add(inline_btn_fregat)

@dp.message_handler(commands=['fregat'])
async def send_answer(message: types.Message):
    await message.answer('Фрегат\nВремя работы: до 23.00\nКонтакты: 89280549091\nАдрес: ул. Красная Заря, д. 4', reply_markup=inline_fregat)

@dp.message_handler(lambda message: message.text.lower() == 'фрегат')
async def send_answer(message: types.Message):
    await message.answer('Фрегат\nВремя работы: до 23.00\nКонтакты: 89280549091\nАдрес: ул. Красная Заря, д. 4', reply_markup=inline_fregat)


#хендлер для Инстаграм ресторана Сказка

inline_btn_skazka = InlineKeyboardButton('Инстаграм ресторана Сказка', url='https://www.instagram.com/skazka_derbent345/')
inline_skazka = InlineKeyboardMarkup().add(inline_btn_skazka)

@dp.message_handler(commands=['skazka'])
async def send_answer(message: types.Message):
    await message.answer('Сказка\nВремя работы: c 11.00 до 23.00\nКонтакты: 89286772733\nАдрес: ул. 345-ДСД, д. 1', reply_markup=inline_skazka)

@dp.message_handler(lambda message: message.text.lower() == 'сказка')
async def send_answer(message: types.Message):
    await message.answer('Сказка\nВремя работы: c 11.00 до 23.00\nКонтакты: 89286772733\nАдрес: ул. 345-ДСД, д. 1', reply_markup=inline_skazka)


#хендлер для Инстаграм ресторана Гюлистан

inline_btn_gulistan = InlineKeyboardButton('Инстаграм ресторана Гюлистан', url='https://www.instagram.com/gulistan_derbent/')
inline_gulistan = InlineKeyboardMarkup().add(inline_btn_gulistan)

@dp.message_handler(commands=['gulistan'])
async def send_answer(message: types.Message):
    await message.answer('Гюлистан\nВремя работы: с 10.30 до 23.00\nКонтакты: 89288377755; 89282988855\nАдрес: ул. Сальмана, д. 68', reply_markup=inline_gulistan)

@dp.message_handler(lambda message: message.text.lower() == 'гюлестан')
async def send_answer(message: types.Message):
    await message.answer('Гюлистан\nВремя работы: с 10.30 до 23.00\nКонтакты: 89288377755; 89282988855\nАдрес: ул. Сальмана, д. 68', reply_markup=inline_gulistan)








# хендлер на развлечения
@dp.message_handler(commands=['entertainments'])
async def send_help(message: types.Message):
    await message.answer("Здесь будет список развлечения")

@dp.message_handler(lambda message: message.text.lower() == "развлечения")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список развелечения")

# хендлер на жильё
@dp.message_handler(commands=['housing'])
async def send_help(message: types.Message):
    await message.answer("Здесь будет список жилья")

@dp.message_handler(lambda message: message.text.lower() == "жилье")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список жилья")

# хендлер на образование
@dp.message_handler(commands=['education'])
async def send_help(message: types.Message):
    await message.answer("Здесь будет список образования")

@dp.message_handler(lambda message: message.text.lower() == "образование")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список образования")

# хендлер на прогулки
@dp.message_handler(commands=['strolls'])
async def send_help(message: types.Message):
    await message.answer("Здесь будет список прогулки")

@dp.message_handler(lambda message: message.text.lower() == "прогулки")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список прогулки")

# хендлер на туризм
@dp.message_handler(commands=['tourism'])
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список туризма")

@dp.message_handler(lambda message: message.text.lower() == "туризм")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список туризма")

# хендлер на музеи
@dp.message_handler(commands=['museums'])
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список музеев")

@dp.message_handler(lambda message: message.text.lower() == "музеи")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список музей")

# хендлер на дети
@dp.message_handler(commands=['children'])
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список для детей", reply_markup=kb.children_kb)

@dp.message_handler(lambda message: message.text.lower() == "детям")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список для детей", reply_markup=kb.children_kb)

@dp.message_handler(lambda message: message.text.lower() == "детская одежда и обувь")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список одежды и обуви для детей", reply_markup=kb.children_kb)

# хендлер на бары
@dp.message_handler(commands=['bar'])
async def send_answer(message: types.Message):
    await message.answer("/Belidzhi - паб фирменного пива пивоварни <Belidzhi>\n")

@dp.message_handler(lambda message: message.text.lower() == "бар")
async def send_answer(message: types.Message):
    await message.answer("/Belidzhi - паб фирменного пива пивоварни <Belidzhi>")


inline_btn_belidzhi = InlineKeyboardButton('Инстаграмм Белиджи', url='https://www.instagram.com/belidzhi.pub/')
inline_belidzhi = InlineKeyboardMarkup().add(inline_btn_belidzhi)

@dp.message_handler(commands=['Belidzhi'])
async def send_answer(message: types.Message):
    await message.answer("Паб Belidzhi\nВремя работы: с 12:00 до 24:00\nКонтакты: +79640000574\nАдрес: ул. Горького, д. 39", reply_markup=inline_belidzhi)

@dp.message_handler(lambda message: message.text.lower() == "бар белиджи")
async def send_answer(message: types.Message):
    await message.answer("Паб Belidzhi\nВремя работы: с 12:00 до 24:00\nКонтакты: +79640000574\nАдрес: ул. Горького, д. 39", reply_markup=inline_belidzhi)

# хендлер на кинотеатры
inline_btn_hayal_cinema = InlineKeyboardButton('Инстаграмм кинотеатра Hayal', url='https://www.instagram.com/hayal_cinema/')
inline_hayal_cinema = InlineKeyboardMarkup().add(inline_btn_hayal_cinema)

@dp.message_handler(commands=['cinema'])
async def send_answer(message: types.Message):
    await message.answer("Кинотеатр Hayal\nКонтакты: +79678088855\nАдрес: ул. Пашабекова, д. 4а", reply_markup=inline_hayal_cinema)

@dp.message_handler(lambda message: message.text.lower() == "кинотеатр")
async def send_answer(message: types.Message):
    await message.answer("Кинотеатр Hayal\nКонтакты: +79678088855\nАдрес: ул. Пашабекова, д. 4а", reply_markup=inline_hayal_cinema)

#хенделр на неизвестную команду
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("К сожалению данной категории нет, либо Ваш запрос введен не корректно. Для получения списка команд введите /help", reply_markup=kb.greet_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
