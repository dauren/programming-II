alpha = {} #dictionary
#key -> value
alpha['a'] = '.-'
alpha['b'] = '--.'
alpha['c'] = '-.-.'

def text_to_morse(text):
	r = []
	for letter in text:
		if letter in alpha: #if key exists
			r.append(alpha[letter]) # get value by key
	return r

t = text_to_morse('abc')
print(t)
