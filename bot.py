import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('7388672963:AAEcxCeYpHO50zw03-H-YS28RVX'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, ' o yo yo. 148-3 to the 3 to the 6 to the 9, representing the ABQ, what up, biatch?!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'All digital products and in game currency in one place expect girlfriend 😁')    

@bot.message_handler(content_types=['In game currency', 'Digital products', 'Social app services', 'Premium Services'])
def file_sent(message
        bot.send_message(message.MLBBDiamond, shot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

