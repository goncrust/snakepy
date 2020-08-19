from PIL import Image, ImageDraw, ImageFont
import sys


def image_from_text(text, img_size, bg_color, text_place, text_size, text_color, save):

    img = Image.new('RGB', img_size, color=bg_color)

    fnt = ImageFont.truetype("/Library/Fonts/Arial.ttf", text_size)

    d_img = ImageDraw.Draw(img)
    d_img.text(text_place, text, fill=text_color, font=fnt)

    img.save(save)


image_from_text("SOUND", (150, 100), (0, 0, 0), (0, 0), 40,
                (255, 0, 0), "images/sound_off.png")

image_from_text("SOUND", (150, 100), (0, 0, 0), (0, 0), 40,
                (0, 255, 0), "images/sound_on.png")

image_from_text("BACK", (115, 100), (0, 0, 0), (0, 0), 40,
                (255, 255, 255), "images/back.png")

args = sys.argv


def help():
    print("  python ift.py text img_size bg_color text_place text_size text_color save")


if not(len(args) > 1):
    help()
elif args[1] == "-h" or len(args) != 7:
    help()
elif len(args) == 7:
    text = args[1]
    img_size = (int(args[2].split(",")[0]), int(args[2].split(",")[1]))
    bg_color = (int(args[3].split(",")[0]), int(
        args[3].split(",")[1]), int(args[3].split(",")[2]))
    text_place = (int(args[4].split(",")[0]), int(args[4].split(",")[1]))
    text_size = int(args[5])
    text_color = (int(args[6].split(",")[0]), int(
        args[6].split(",")[1]), int(args[6].split(",")[2]))
    save = args[7]

    image_from_text(text, img_size, bg_color, text_place,
                    text_size, text_color, save)
