from PIL import Image, ImageDraw, ImageFont
text = "S"
color = (100, 100, 100)
img = Image.new('RGB', (10, 10), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((2, -1), text)
img.save('img1.png')
