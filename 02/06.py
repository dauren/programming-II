import csv
high_schools = []
with open('high_schools.csv', encoding='utf-8') as file:
	reader = csv.reader(file, delimiter=',', quotechar='"')
	i = 0
	for row in reader:
		i = i + 1
		if i > 1 and len(row) > 0:
			high_schools.append(row[3])
stat = {}
stat['university'] = 0
stat['institute'] = 0
stat['academy'] = 0
for item in high_schools:
	item = item.lower()
	if "университет" in item:
		stat['university'] = stat['university'] + 1
	if "институт" in item:
		stat['institute'] = stat['institute'] + 1
	if "академия" in item:
		stat['academy'] = stat['academy'] + 1

print(stat)