a_lines = []
b_lines = []
with open('a.txt', 'r') as file:
	lines = file.readlines()
	for line in lines:
		line = line.strip()
		if len(line) > 1:
			a_lines.append(line)

with open('b.txt', 'r') as file:
	lines = file.readlines()
	for line in lines:
		line = line.strip()
		if len(line) > 1:
			b_lines.append(line)

i = 0
while i < len(a_lines) and i < len(b_lines):
	s1 = a_lines[i]
	s2 = b_lines[i]