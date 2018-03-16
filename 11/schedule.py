import time
from onay import get_balance
import telegram
bot = telegram.Bot(token='271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU')
user_id = 129767043
while True:
	balance = get_balance('9643908503307746820')
	bot.sendMessage(chat_id=user_id, text='Баланс %f' % balance)
	time.sleep(5)