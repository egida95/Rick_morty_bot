import telebot
from config import TOKEN
from location import get_location_name, parse_data

from main import button, menu
from characters import get_character_names, get_character_text
from episods import get_names,get_episode_names

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите кнопку",reply_markup=menu())

@bot.message_handler(content_types=['text'])
def r(message):
    if message.chat.type == "private":
        if message.text == "Персонажи":
            markup = button(get_character_names())
            bot.send_message(message.chat.id, "Выберите полового партнера",reply_markup=markup)

        elif message.text in get_character_names():
            bot.send_message(message.chat.id, get_character_text(message.text))
        
        elif message.text == 'Локации':
            markup = button(get_location_name())
            bot.send_message(message.chat.id,'Выбирите локацию',reply_markup=markup)
            
        elif message.text in get_location_name():
            bot.send_message(message.chat.id, parse_data(message.text))
        
            
        elif message.text == 'Эпизоды':
            markup = button(get_names()) 
            bot.send_message(message.chat.id, 'Выбирите серии',reply_markup=markup)
            
        elif message.text in get_names():
            bot.send_message(message.chat.id, get_episode_names(message.text))
        
            
        elif message.text == "|||":
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


bot.polling(none_stop=True)
