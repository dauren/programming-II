import requests
url = "https://api.vk.com/method/database.getUniversities?q=%D0%9A%D0%91%D0%A2%D0%A3&v=5.52"

r = requests.get(url)
data = r.json()
universities = data['response']['items']
for university in universities:
	university_id = university['id']
	title = university['title']
	url = "https://api.vk.com/method/users.search?university=%d&access_token=c99469df531d0b44d7edff926c507b300f13f1a553d2f1120678f2c1c32eb93722393e0e05085f0d82b23&v=5.52" % university_id
	r = requests.get(url)
	data = r.json()
	print(data)

