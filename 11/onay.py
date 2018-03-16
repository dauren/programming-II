
import requests
def get_balance(card_no):
	headers =  {
		  "Content-Type": "application/json",
		  "X-Application-Token": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MDIwOTQxOTcsImp0aSI6IlJNODJoVlhYeWtwYk55WkJFM2RlU0UyOGdKVkxlaFB2IiwiaXNzIjoiQ2Vuc3VzIEFQSSBhdXRob3JpemF0aW9uIHNlcnZpY2UiLCJhdWQiOiJJT1NfTVAiLCJuYmYiOjE1MDIwOTQyMjcsImV4cCI6MTgxNzQ1NDE5NywiZGF0YSI6eyJyb3V0ZXMiOnsidjFcL2V4dGVybmFsXC8qIjpbIkdFVCIsIlBPU1QiLCJQVVQiLCJERUxFVEUiLCJPUFRJT05TIl19LCJob3N0cyI6WyJwdWIuY2Vuc3VzIl19fQ.t7esNI740ZjnDsa2P54ilUZ3HC_TOYLtebhiII4p-iA",
		  "Accept": "*/*", 
		  "User-Agent": "Onay/1.3.3 (kz.onay.Onay; build:1.3.3.0; iOS 11.0.1) Alamofire/4.4.0",
		  "Accept-Language": "ru_RU"
	}
	r = requests.get("https://nwqsr0rz5earuiy2t8z8.census.kz/v1/external/card/%s" % card_no, headers=headers)
	data = r.json()
	if data.get('success'):
		balance = float(data['result']['data']['balance'])
		return balance
	return None


b = get_balance('9643908503307746820')
print(b)