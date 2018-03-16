from PIL import Image, ImageDraw
im = Image.open("cat.png")
size = im.size
new_im = im.convert('L').resize((size[0]//4, size[1]//4))
size = new_im.size
for y in range(0, size[1]):
	for x in range(0, size[0]):
		g = new_im.getpixel((x, y))
		print("%d" % g, end = '\t')
	print()

for y in range(0, size[1]):
	for x in range(0, size[0]):
		g = new_im.getpixel((x, y))
		if g < 200:
			print("@", end = '')
		else:
			print(" ", end = '')
	print()