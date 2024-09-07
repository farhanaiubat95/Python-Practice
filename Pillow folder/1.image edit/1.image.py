from PIL import Image

img = Image.open("Pillow folder/1.image edit/elon musk.jpg")
img.show()  # image show
img.rotate(45).show()  # rotate 45

# image size print
print(img.height)
print(img.width)
print(img.size)
print(img.format)
