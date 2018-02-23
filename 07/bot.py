import requests
token = '271801612:AAF_3DZ-QhhFkmi7dAi_TOjkPw5Ok82eINU'
url = 'https://api.telegram.org/bot%s/'  % token 
r = requests.get(url + 'getMe')
data = r.json()
print(data)
r = requests.get(url + 'getUpdates')
data = r.json()
updates = data['result']
for update in updates:
	message = update['message']
	user_id = message['from']['id']
	send_data = {
		'chat_id': user_id,
		'text': 'Салам'
	}
	r = requests.post(url + 'sendMessage', send_data)
	print(r.json())




