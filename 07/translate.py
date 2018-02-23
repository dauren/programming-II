import requests
from bs4 import BeautifulSoup
text = 'кошка'
url = 'https://sozdik.kz/translate/ru/kk/%s/' % text
r = requests.get(url)
data = r.json()
translation = data['translation']
from bs4 import BeautifulSoup
soup = BeautifulSoup(translation, 'html.parser')
text = soup.select('a')[0].text
print(text)