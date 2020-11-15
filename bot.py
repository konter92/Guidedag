import logging
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

# хендлер на еду
@dp.message_handler(commands=['food'])
async def send_help(message: types.Message):
    await message.answer("Здесь будет список еды",  reply_markup=kb.eda_kb)

@dp.message_handler(lambda message: message.text.lower() == "еда")
async def send_answer(message: types.Message):
    await message.answer("Здесь будет список еды",  reply_markup=kb.eda_kb)

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
    await message.answer("/Belidzhi - паб фирменного пива пивоварни <Belidzhi>")

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
