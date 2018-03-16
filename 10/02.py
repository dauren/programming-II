from PIL import Image, ImageDraw
im = Image.open("img1.png")
rgb_im = im.convert('RGB')
size = rgb_im.size
w, h = size
for y in range(0, w):
	for x in range(0, h):
		r, g, b = rgb_im.getpixel((x, y))
		print("%d,%d,%d" % (r,g, b), end = '\t')
	print()

for y in range(0, size[1]):
 for x in range(0, size[0]):
  r, g, b = rgb_im.getpixel((x, y))
  if (r, g, b) == (0, 0, 120):
   print("*", end = '')
  else:
   print(" ", end = '')
 print()