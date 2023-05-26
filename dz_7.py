
# Задача 1. Создайте пользовательский аналог метода map().
def z_1():
  def map_func(func, n):
    return (func(x) for x in n)
  def func(n):
    return n * 2
  list = (1, 3, 4, 5, 6, 7)
  print(map(func, list))
  print(map_func(func, list))
# z_1()
#------------------------------------------------------
#Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
def z_2():
  def our_format(func):
    def decorator(a):
        our_format = int(input('Введите количество: '))
        for _ in range(our_format):
          func(a)
    return decorator
  @our_format
  def main(a):
    request = int(input('Введите число: '))
    print(a*request)
  main(10)
# z_2()
# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных # ходов.5
import telebot
from random import randint
def z_3():
  bot = telebot.TeleBot('')
  comp_number = randint(1, 1000)
  count = 1
  count += 1
  @bot.message_handler(commands=['игра'])
  def send_welcome(message):
    bot.reply_to(
      message, 'Давай поиграем в игру "угадай число": Введите число от 1 до 1000')
  @bot.message_handler(content_types=['text', comp_number])
  def mini_game(message):
    us_number = int(message.text)
    if us_number != comp_number:
      if us_number < comp_number:
        us_number = bot.reply_to(
          message, 'Загаданное число больше, попробуйте ещё раз')
    elif us_number > comp_number:
      us_number = bot.reply_to(
        message, 'Загаданное число меньше, попробуйте ещё раз')
    elif us_number == comp_number:
      bot.reply_to(message, f'Поздравляем!!!! Вы угадали с {count} попытки')
  bot.polling()
