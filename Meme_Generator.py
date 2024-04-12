from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")

print(top_text, bottom_text)

print("Список картинок:")
print("1.negr")
print("2.Младенец")
print("3.negr2")
print("4.Сигма")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
    image_file = "mem.jpg"
elif image_number == 2:
    image_file = "mem1.jpg"
elif image_number == 3:
    image_file = "memes.jpg"
elif image_number == 4:
    image_file = "memes2.jpeg"
else:
    print("Ошибка ввода")
    exit()

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)


font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="white")

text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill="white")

image.save("memes.jpg")