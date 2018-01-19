a, b = 0, 0
with open('input.txt', 'r') as file:
	lines = file.readlines()
	a = int(lines[0])
	b = int(lines[1])
print(a + b)
print(lines)