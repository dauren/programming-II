import time
from onay import get_balance
import telegram
import json
bot = telegram.Bot(token='271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU')
data = {}
with open('cards.json', 'r') as file:
	data = json.load(file)

while True:
	for user_id, card_list in data.items():
		user_id = int(user_id)
		for card in card_list:
			balance = get_balance(card)
			if balance < 200:
				bot.sendMessage(chat_id=user_id, text='Внимание, баланс вашей карты ...%s ~ %d тг. Этого хватит меньше чем на %d поездок' % (card[-8:], balance, balance//80))
	time.sleep(60)