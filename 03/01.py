import csv

with open('crime_almaty.csv', encoding='utf-8') as file:
	reader = csv.DictReader(file, delimiter=',', quotechar='"')
	for row in reader:
		print(row)
		print(row['reg_code'])
		break
