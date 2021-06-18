import telebot
from telebot import types
TOKEN = '1666933310:AAGfU27Hi_mEycQakq2-pAONgxf5Gj8e2JU'

WEATHER_TOKEN = 'f7a04291e22bc3131eda333eb5a1b026'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start", 'calc', 'help', 'cartoons', 'красивыедевушкисмотреть','weather','films', 'find', 'profile'])
def start_bot(message):
    if message.text.lower() == '/start':
        keyboard = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Шутеичка',callback_data='joke')
        google = types.InlineKeyboardButton('Гугле', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        question = types.InlineKeyboardButton('Вопрос!', callback_data='question')
        keyboard.add(question)
        keyboard.add(btn)
        keyboard.add(google)
        bot.send_message(message.chat.id, 'Привет!\nЯ новый бот!\n \nВот список моих комманд:\n/help Помощь \n/calc  Калькулятор \n/weather Погода \n/find Поиск \n/films Фильмы \n/profile Профиль \n/красивыедевушкисмотреть')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'Вы в разделе Помощь')
    elif message.text.lower() == '/cartoons':
        bot.send_message(message.chat.id, 'Здесь можно посмотерть мультики!')
    elif message.text.lower() == '/красивыедевушкисмотреть':
        bot.send_message(message.chat.id, 'Приятного просмотра!: https://youtu.be/dQw4w9WgXcQ ')
    elif message.text.lower() == '/weather':
        bot.send_message(message.chat.id, 'Вы в разделе Погоды')
        bot.send_message(message.chat.id, 'Введите название города:')
    elif message.text.lower() == '/films':
        bot.send_message(message.chat.id, 'Здесь можно легко и быстро посмотреть фильмы в том жанре, который вам нужен')
    elif message.text.lower() == '/find':
        bot.send_message(message.chat.id, 'Поиск по разделу бота')
    elif message.text.lower() == '/profile':
        bot.send_message(message.chat.id, 'Ваш профиль')
        bot.send_message(message.chat.id, 'Ой, кажется я не знаю твоего имени, не мог бы ты ввести его? \nВведите имя:')
        bot.register_next_step_handler(message, enter_name)
    elif message.text.lower() == '/calc':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сумма')
        btn2 = types.KeyboardButton('Минус')
        keyboard.add(btn1)
        keyboard.add(btn2)
        
        bot.send_message(message.chat.id,
                         'Калькулятор! Выберите действие',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, calc_choose)
   
# выбор действия калькулятора
def calc_choose(message):
    if message.text.lower() == 'сумма':
        bot.send_message(message.chat.id, 'Вы выбрали сумма.' )
        bot.send_message(message.chat.id, 'Введите числа через пробел')
        bot.register_next_step_handler(message, calc_result_sum)
        
    if message.text.lower() == 'минус':
        bot.send_message(message.chat.id, "Вы выбрали вычитание.")
        bot.send_message(message.chat.id, "Введите числа через пробел")
        bot.register_next_step_handler(message, calc_result_minus)
        
def calc_result_sum(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    
    bot.send_message(message.chat.id, f"Результат {num1 + num2}")
        
def calc_result_minus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    
    bot.send_message(message.chat.id, f"Результат {num1 - num2}")  
        
        
        
@bot.message_handler(content_type=['text'])
def enter_name(message):
    name  = message.text
    bot.send_message(message.chat.id, f'Приятно познакомиться, {name}!')
    bot.send_message(message.chat.id, 'А сколько тебе лет?')
    
    
@bot.callback_query_handler(func=lambda x: x.data == 'joke')
def joke_fn(message):
    bot.send_message(message.from_user.id, '— Что это: жёлтое и не умеет плавать? \n — Школьный автобус, полный детей.')
    

# ПОГОДА
def weather_menu(message):
    city = message.text
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}'
    r = requests.get(API_URL)
    print(r.text)
    
    
@bot.callback_query_handler(func=lambda x: x.data == 'question')
def question_btn(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Две тонны',callback_data='ans1')
    btn2 = types.InlineKeyboardButton('Один слон', callback_data='ans2')
    btn3 = types.InlineKeyboardButton('Четыре тонн', callback_data='ans3')
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    bot.send_message(message.from_user.id, 'Вопрос: \nCколько весит язык синего кита?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: x.data == 'ans1')
def answer1(message):
    bot.send_message(message.chat.id, 'Неверный ответ!')
    
    
    
bot.polling()  















