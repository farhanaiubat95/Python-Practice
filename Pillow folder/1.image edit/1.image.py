from PIL import Image

img = Image.open("Pillow folder/1.image edit/elon musk.jpg")
img.show()
img.rotate(45).show()  # rotate 45

print(img.height)
print(img.width)
print(img.size)
print(img.format)
