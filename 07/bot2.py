from telegram.ext import Updater
import logging
import requests
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU')
dispatcher = updater.dispatcher

def start_reply(bot, update):
	first_name = update.message.from_user.first_name
	bot.send_message(chat_id=update.message.chat_id, text="Hello, %s" % first_name)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start_reply)
dispatcher.add_handler(start_handler)

def translate_reply(bot, update, args):
	text = ' '.join(args).lower()
	url = 'https://sozdik.kz/translate/ru/kk/%s/' % text
	r = requests.get(url)
	data = r.json()
	translation = data['translation']
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(translation, 'html.parser')
	text = soup.select('a')[0].text
	bot.send_message(chat_id=update.message.chat_id, text=text)

translate_handler = CommandHandler('translate', translate_reply,  pass_args=True)
dispatcher.add_handler(translate_handler)


def echo_reply(bot, update):
	text = update.message.text.lower()
	if "привет" in text:
		bot.send_message(chat_id=update.message.chat_id, text="Привет")
	elif "салам" in text:
		bot.send_message(chat_id=update.message.chat_id, text="Салам-пополам")
	elif "как дела" in text:
		bot.send_message(chat_id=update.message.chat_id, text="пока не родила")
	elif "что делаешь" in text:
		bot.send_message(chat_id=update.message.chat_id, text="ничего")
	elif "ладно" in text:
		bot.send_message(chat_id=update.message.chat_id, text="прохладно")
	else:
		bot.send_message(chat_id=update.message.chat_id, text="че?")



from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo_reply)
dispatcher.add_handler(echo_handler)


updater.start_polling()