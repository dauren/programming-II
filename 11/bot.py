from telegram.ext import Updater
import logging
import requests
from onay import get_balance
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU')
dispatcher = updater.dispatcher

def start_reply(bot, update):
	text = 'Введите 19 цифр вашей Онай карты'
	bot.send_message(chat_id=update.message.chat_id, text=text)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start_reply)
dispatcher.add_handler(start_handler)

def echo_reply(bot, update):
	text = update.message.text.lower()
	import re
	p = re.compile('^(96431085033|96439085033)\d{8}$')
	if p.match(text):
		card_no = text
		balance = get_balance(card_no)
		if balance is not None:
			text = 'Баланс карты: %d' % balance
			bot.send_message(chat_id=update.message.chat_id, text=text)
		else:
			text = 'Карта не найдена'
			bot.send_message(chat_id=update.message.chat_id, text=text)
	else:
		text = 'Введите 19 цифр вашей Онай карты'
		bot.send_message(chat_id=update.message.chat_id, text=text)


from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo_reply)
dispatcher.add_handler(echo_handler)

updater.start_polling()