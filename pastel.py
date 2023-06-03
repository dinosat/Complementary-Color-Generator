import colorsys
import random
from PIL import Image

def generate_pastel_colors():
    colors = []
    for _ in range(3):
        # Generate random values for hue, saturation, and value
        hue = random.random()
        saturation = random.uniform(0.1, 0.3)  # Low saturation for pastels
        value = random.uniform(0.7, 0.9)  # High value for pastels

        # Convert the HSV color to RGB
        rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue, saturation, value))
        colors.append(rgb)

    return colors

# Generate pastel colors
colors = generate_pastel_colors()

# Create a new image with the colors
image = Image.new("RGB", (300, 100))
pixels = image.load()

# Fill the image with the colors
for i, color in enumerate(colors):
    for x in range(i * 100, (i + 1) * 100):
        for y in range(100):
            pixels[x, y] = color

# Save the image
image.save("pastel_colors.png")
