import telebot
from telebot import types
import requests
import json


bot = telebot.TeleBot('BOT_TOKEN')
API = 'API_KEY'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        if temp > 5.0:
            bot.reply_to(message, f"Сейчас погода: {temp} ☀️")
        elif temp < 5.0:
            bot.reply_to(message, f"Сейчас погода: {temp} ❄️")
    else:
        bot.reply_to(message, 'Город указан неверно')
bot.polling(none_stop = True)
