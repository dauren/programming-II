import csv
stat = {}
with open('high_schools.csv', encoding='utf-8') as file:
	reader = csv.reader(file, delimiter=',', quotechar='"')
	i = 0
	for row in reader:
		i = i + 1
		if i > 1 and len(row) > 0:
			city = row[0]
			current = stat.get(city, 0) #0 default
			stat[city] = current +  1
print(stat['Астана'])
print(stat)


