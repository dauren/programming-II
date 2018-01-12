file = open('morse.txt', 'r') #open file for read
lines = file.readlines() # read all lines
alpha = {}
for line in lines:
	l = line.lower().split()
	if len(l) == 2:
		key, value = l
		alpha[key] = value

print(alpha)
