from PIL import Image, ImageDraw
im = Image.open("cat.png")
size = im.size
new_im = im.convert('L').resize((size[0]//4, size[1]//4))