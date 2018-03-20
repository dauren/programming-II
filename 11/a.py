import json

def save_card(user_id, card_no):
	data = {}
	with open('cards.json', 'r') as file:
		data = json.load(file)
	if data.get(user_id):
		l = data[user_id]
		l.append(card_no)
		data[user_id] = l
	else:
		data[user_id] = [card_no]
	with open('cards.json', 'w') as file:
		json.dump(data, file)

def get_cards(user_id):
	data = {}
	with open('cards.json', 'r') as file:
		data = json.load(file)
	if data.get(user_id):
		return date[user_id]
	return []

save_card('asdas', 'asdsad')