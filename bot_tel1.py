import random
import telebot
from telebot import types
bot = telebot.TeleBot("token from BotFather")
first=0
max_step= 28 
players = ['Первый игрок','Второй игрок']
sweets =221
step=0

def rand():
    f = random.randint(0, 1)
    return f 
def init():
    global first
    first=rand()
init()    
@bot.message_handler(content_types=['text'])

def start(message):
    global players 
    global first
    global step   
    if message.text == '/start':
         bot.send_message(message.from_user.id,f'Начинает {players[first % 2]}, заберите конфеты (от 1 до 28) ')
         bot.register_next_step_handler(message,game)

    elif message.text == '/help':        
        bot.send_message(message.from_user.id,'\
                   Создайте программу для игры с конфетами человек против человека.\
                   Условие задачи: На столе лежит 221 конфета.Играют два игрока делая ход друг после друга.')                 
        bot.send_message(message.from_user.id,\
                    'Первый ход определяется жеребьёвкой.\
                    За один ход можно забрать не более чем 28 конфет.')   
    else:
        bot.send_message(message.from_user.id, 'Напиши /start для начала игры или /help для прочтения правил')

def start2(message):
    global players 
    global first
    global step        
    bot.send_message(message.from_user.id,f'Играет {players[first % 2]}, заберите конфеты (от 1 до 28) ')
    bot.register_next_step_handler(message,game)                 
        
def game (message):
    global first
    global step
    global sweets
            
    step= abs(int(message.text))
    if step>max_step:
        bot.send_message(message.from_user.id,f'Ошибка, {players[first % 2]} заберите конфеты (от 1 до 28)' ) 
        bot.register_next_step_handler(message,game)   
    else:
        if sweets<step:
            bot.send_message(message.from_user.id,f'Ошибка, не более {sweets} конфет' )
            bot.send_message(message.from_user.id,f'{players[first % 2]} заберите конфеты (от 1 до 28)' )  
            bot.register_next_step_handler(message,game) 
        else:   
                sweets = sweets - step        
                if sweets > 0:
                    bot.send_message(message.from_user.id,f'Осталось конфет:  {sweets}' )            
                    first+=1 
                    start2(message)                                               
                else:
                    bot.send_message(message.from_user.id,f'Игра окончена, {players[first % 2-1]} победитель' )     
     
bot.polling(none_stop=True, interval=0)

