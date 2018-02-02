import csv
from collections import Counter
states = {}
with open('uk.txt', encoding='utf-8') as file:
	lines = file.readlines()
	for line in lines:
		if line[:6] == 'Статья':
			dot = line.find('.')
			state_num = line[7:dot]
			state_title = line[dot + 1:].strip()
			states[state_num] = state_title
#crime_stat = Counter()
region = {}
with open('crime.csv') as file:
	reader = csv.DictReader(file, delimiter=';', quotechar='"')
	for row in reader:
		city_code = row['city_code']
		if city_code in region:
			pass
		else:
			region[city_code] = Counter()
		crime_code = str(int(row['crime_code'])//10)
		counter = region[city_code]
		counter[crime_code] += 1
		#region[city_code][crime_code] +=1

for city_code in region:
	crime_stat = region[city_code]
	l = crime_stat.most_common(3)
	for item in l:
		title = states[item[0]]
		cnt = item[1]
		print("%s\t%s\t%d" % (city_code, title, cnt))