url = "https://oauth.vk.com/authorize?client_id=6393777&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,status&response_type=token&v=5.52"
access_token = '4e3440897165e3c6088930c83afa60241dff17471021bf6ff9cb3fc644d2841623996f421cfc0ffc56952'
url = 'https://api.vk.com/method/status.set?text=hello&access_token=4e3440897165e3c6088930c83afa60241dff17471021bf6ff9cb3fc644d2841623996f421cfc0ffc56952&v=5.52'

url = "https://api.vk.com/method/status.set?text=hello&access_token=4e3440897165e3c6088930c83afa60241dff17471021bf6ff9cb3fc644d2841623996f421cfc0ffc56952&v=5.52"
import requests

url = "https://www.anekdot.ru/"
headers = {
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
r = requests.get(url, headers=headers)
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
items = soup.select('body div.text')
import random
item = random.choice(items)
text = item.text

url = "https://api.vk.com/method/status.set?text=%s&access_token=4e3440897165e3c6088930c83afa60241dff17471021bf6ff9cb3fc644d2841623996f421cfc0ffc56952&v=5.52" % text
r = requests.get(url)