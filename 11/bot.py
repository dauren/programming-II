from telegram.ext import Updater
import logging
import requests
from onay import get_balance
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU')
dispatcher = updater.dispatcher

def start_reply(bot, update):
	text = get_balance('9643908503307746820')
	print(update)
	bot.send_message(chat_id=update.message.chat_id, text=text)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start_reply)
dispatcher.add_handler(start_handler)

def echo_reply(bot, update):
	text = update.message.text.lower()

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo_reply)
dispatcher.add_handler(echo_handler)

updater.start_polling()