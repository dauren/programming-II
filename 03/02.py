states = {}
with open('uk.txt', encoding='utf-8') as file:
	lines = file.readlines()
	for line in lines:
		if line[:6] == 'Статья':
			dot = line.find('.')
			state_num = line[7:dot]
			state_title = line[dot + 1:].strip()
			states[state_num] = state_title	