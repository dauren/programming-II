import math
def is_prime(x):
	i = 2
	while i < math.sqrt(x):
		if x % i == 0:
			return False
		i = i + 1
	return True

x = 2
with open('prime.txt', 'r') as file:
	lines = file.readlines()
	x = int(lines[-1])
with open('prime.txt', 'a') as file:
	while True:
		if is_prime(x):
			s = str(x) + "\n"
			file.write(s)
		x = x + 1

