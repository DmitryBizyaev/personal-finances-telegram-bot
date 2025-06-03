import os
import telebot
# import secrets
from telebot import types

def main():

    # DATABASE_NAME = 'schedule.db'

    bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


    @bot.message_handler(commands = ['start'])
    def start_message(message):

        tg_user_id = str(message.from_user.id)

        bot.send_message(message.chat.id, message.from_user.id)

    bot.infinity_polling()
        

if __name__ == "__main__":
    main()