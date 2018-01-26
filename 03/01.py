import csv
from collections import Counter
crime_stat = Counter()
with open('crime_almaty.csv', encoding='utf-8') as file:
	reader = csv.DictReader(file, delimiter=',', quotechar='"')
	for row in reader:
		crime_stat[row['stat']] +=1

print(crime_stat.most_common(10))
