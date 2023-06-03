import colorsys
import random
from PIL import Image


def generate_complementary_color():
    base_hue = random.random()

    complementary_hue1 = (base_hue + 0.5) % 1
    complementary_hue2 = (base_hue + 0.5 + 0.33) % 1
    saturation = random.uniform(0.4, 0.6)
    value = random.uniform(0.7, 0.9)

    rgb_base = colorsys.hsv_to_rgb(base_hue, saturation, value)
    rgb_complementary1 = colorsys.hsv_to_rgb(complementary_hue1, saturation, value)
    rgb_complementary2 = colorsys.hsv_to_rgb(complementary_hue2, saturation, value)

    base_color = tuple(int(value * 255) for value in rgb_base)
    complementary_color1 = tuple(int(value * 255) for value in rgb_complementary1)
    complementary_color2 = tuple(int(value * 255) for value in rgb_complementary2)
    return base_color, complementary_color1, complementary_color2


base_color, complementary_color1, complementary_color2 = generate_complementary_color()

image = Image.new("RGB", (300, 100))
pixels = image.load()
for x in range(100):
    for y in range(100):
        pixels[x, y] = base_color
for x in range(100, 200):
    for y in range(100):
        pixels[x, y] = complementary_color1
for x in range(200, 300):
    for y in range(100):
        pixels[x, y] = complementary_color2
image.save("complementary_colors.png")
print("Base color:", base_color)
print("Complementary color 1:", complementary_color1)
print("Complementary color 2:", complementary_color2)
