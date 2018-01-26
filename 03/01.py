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

crime_stat = Counter()
with open('crime_almaty.csv', encoding='utf-8') as file:
	reader = csv.DictReader(file, delimiter=',', quotechar='"')
	for row in reader:
		crime_code = str(int(row['crime_code'])//10)
		crime_stat[crime_code] +=1

l = crime_stat.most_common(10)
for item in l:
	title = states[item[0]]
	cnt = item[1]
	print("%s\t%d" % (title, cnt))