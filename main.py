from PIL import Image, ImageFont, ImageDraw


def z1():
    im = "111.jpeg"
    with Image.open(im) as img:
        img.load()

    cropped_img=img.crop((300,210,600,470))
    cropped_img.save("222.jpg")

z1()

def z2():

    holidays = {"день рождения": "denirojj.jpeg", "новый год": "nov god.jpeg", "8 марта": "8 marta.jpeg"}
    holiday = input("какой праздник вам нужен?")
    for day in holidays:
        if day.lower() == holiday.lower():
            image = Image.open(holidays[day])
            image.show()

#z2()


def z3():
    n = input("Введите имя получателя: ")
    ph = "8 marta.jpg"

    with Image.open(ph) as img:
        img.load()

    font = ImageFont.truetype("1.ttf", 24)

    write_name = ImageDraw.Draw(img)

    write_name.text((img.width // 2 - 50, img.height - 30), n + ", поздравляю!", fill = ('blue'), font = font, stroke_width = 1)

    img.show()
    img.save("otk name.png")

z3()