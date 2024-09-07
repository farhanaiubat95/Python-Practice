from PIL import Image

img = Image.open("Pillow folder/3.image crop/Sadman.jpg")
img.show()
print("First image size : ", img.size)

area = (200, 60, 650, 700)
image_crop = img.crop(area)
image_crop.save('Croped image.jpg')
print("After cropping : ", image_crop.size)
image_crop.show()
