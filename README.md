# (Pastel) Colors Generator

This program generates pastel colors and creates an image using the generated colors.

## Prerequisites

- Python 3.x
- Python libraries:
  - `colorsys`
  - `random`
  - `PIL` (Python Imaging Library)

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:

   ```shell
   pip install pillow
   ```

## Usage

1. Clone or download the program files to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the program files.
3. Run the following command to execute the program:

   ```shell
   python pastel_colors_generator.py
   ```

4. The program will generate three pastel colors and save the resulting image as `pastel_colors.png` in the same directory.

## How it works

The program follows these steps to generate and display the pastel colors:

1. It imports the required libraries: `colorsys` for color manipulation and `PIL` for image creation.
2. The `generate_pastel_colors()` function generates three pastel colors using random values for hue, saturation, and value. Hue represents the color tone, saturation controls the intensity of the color, and value determines the brightness.
3. The program creates a new image using the `Image.new()` function from the `PIL` library. The image dimensions are set to 300 pixels wide and 100 pixels high.
4. The `pixels` object is obtained from the image using the `load()` method. This allows direct access to the pixel data.
5. The program fills the image with the generated colors using nested loops. Each color is applied to a 100x100 pixel block in the image.
6. The resulting image is saved as `pastel_colors.png` using the `save()` method of the `Image` object.

## Customization

- You can modify the number of colors generated by changing the range in the `generate_pastel_colors()` function.
- Adjust the saturation and value ranges to control the intensity and brightness of the colors.
- Modify the image dimensions by changing the parameters in the `Image.new()` function.
- Change the output file name by modifying the argument in the `save()` method.

## License

This program is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and use this program according to your needs.

## Author

This program was created by [DinoSat].
