"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#PROXY = {
#    'proxy_url': 'socks5://t1.learn.python.ru:1080',
#    'urllib3_proxy_kwargs': {
#        'username': 'learn',
#        'password': 'python'
#    }
#}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def name_the_constellation(update, context):
    user_text = update.message.text
    user_planet = user_text.split()[1]
    user_planet = user_planet.capitalize()
    print(user_planet)

    planet_sol = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if user_planet not in planet_sol:
      Err_planet = 'Ошибка ввода'
      print(Err_planet)
      update.message.reply_text(Err_planet)

    today = date.today()
    today = today.strftime('%d/%m/%Y')

    if user_planet == 'Mercury':
      planet = ephem.Mercury(today)
    
    if user_planet == 'Venus':
      planet = ephem.Venus(today)
    
    if user_planet == 'Mars':
      planet = ephem.Mars(today)

    if user_planet == 'Jupiter':
      planet = ephem.Jupiter(today)

    if user_planet == 'Saturn':
      planet = ephem.Saturn(today)
    
    if user_planet == 'Uranus':
      planet = ephem.Uranus(today)

    if user_planet == 'Neptune':
      planet = ephem.Neptune(today)

    constellation = ephem.constellation(planet)
    print(constellation)
    update.message.reply_text(constellation)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", name_the_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
