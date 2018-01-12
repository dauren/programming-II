alpha = {} #dictionary
def read_morse_table():
	file = open('morse.txt', 'r') #open file for read
	lines = file.readlines() # read all lines
	alpha = {}
	for line in lines:
		l = line.lower().split()
		if len(l) == 2:
			key, value = l
			alpha[key] = value
	return alpha

alpha = read_morse_table()
alpha[' '] = '.......'
alpha['.'] = '......'
alpha[','] = '.-.-.-'
def text_to_morse(text):
	r = []
	for letter in text.lower():
		if letter in alpha: #if key exists
			r.append(alpha[letter]) # get value by key
	return r

t = text_to_morse('Aliya')
print(t)
