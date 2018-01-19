def compare_lines(s1, s2):
	s1 = s1.replace(' ', '')
	s2 = s2.replace(' ', '')
	v1 = 0
	for c in s1:
		v1 = v1 + ord(c)
	v2 = 0
	for c in s2:
		v2 = v2 + ord(c)
	return 1 - abs(v2-v1)/min(v1, v2)
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
x = 0
while i < len(a_lines) and i < len(b_lines):
	s1 = a_lines[i].replace(" ", "")
	s2 = b_lines[i].replace(" ", "")
	if compare_lines(s1, s2) > 0.7:
		x = x + compare_lines(s1, s2)
	i = i  + 1

p = x / (len(a_lines) + len(b_lines))
print(p)
