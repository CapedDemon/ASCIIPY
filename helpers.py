from PIL import Image, ImageDraw, ImageFont
from math import ceil

# importnt variables
PIL_GRAYSCALE = 'L'
PIL_WIDTH_INDEX = 0
PIL_HEIGHT_INDEX = 1

# ascii chars
asciiChars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resizing the image
def imageResize(targetImage, newWidth):
    global newHeight
    width, height = targetImage.size
    ratio = height/width
    newHeight = ratio * newWidth
    newImage = targetImage.resize((newWidth, int(newHeight)))
    return newImage

# changing the image into gray scale
def graying(newImage):
    grayImage = newImage.convert("L")
    return grayImage

# replacing the pixels to ascii
def pixelAscii(grayImage):
    pixels = grayImage.getdata()
    characters = "".join([asciiChars[i//25] for i in pixels])
    return characters

# text to image
def text_to_img(textfile_path):
    with open(textfile_path) as f:
        lines = tuple(line.rstrip() for line in f.readlines())

    # taking the default font
    font = None
    
    if font is None:
        font = ImageFont.load_default()

    # make a sufficiently sized background image based on the combination of font and lines
    def font_points_to_pixels(pt): return round(pt * 96.0 / 72)
    margin_pixels = 20

    # height of the background image
    tallest_line = max(lines, key=lambda line: font.getsize(line)[
                       PIL_HEIGHT_INDEX])
    max_line_height = font_points_to_pixels(
        font.getsize(tallest_line)[PIL_HEIGHT_INDEX])
    # apparently it measures a lot of space above visible content
    realistic_line_height = max_line_height * 0.8
    image_height = int(ceil(realistic_line_height *
                       len(lines) + 2 * margin_pixels))

    # width of the background image
    widest_line = max(lines, key=lambda s: font.getsize(s)[PIL_WIDTH_INDEX])
    max_line_width = font_points_to_pixels(
        font.getsize(widest_line)[PIL_WIDTH_INDEX])
    image_width = int(ceil(max_line_width + (2 * margin_pixels)))

    # draw the background
    background_color = 255  # white
    image = Image.new(PIL_GRAYSCALE, (image_width,
                      image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # draw each line of text
    font_color = 0  # black
    horizontal_position = margin_pixels
    for i, line in enumerate(lines):
        vertical_position = int(
            round(margin_pixels + (i * realistic_line_height)))
        draw.text((horizontal_position, vertical_position),
                  line, fill=font_color, font=font)

    return image