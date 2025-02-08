from PIL import Image, ImageDraw, ImageFont

# Characters for 3-tone shading:
#  - ' ' (space) for black (background)
#  - '#' for mid-gray
#  - '@' for bright white
ASCII_CHARS = " #@"

def resize_image(image, new_width=80, scale_factor=1.0):
    """
    Resize the image while maintaining its aspect ratio.
    'scale_factor' can help fix vertical stretching:
      - <1.0 to compress vertically if output is too tall,
      - >1.0 to stretch if output is too short.
    """
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * scale_factor)
    return image.resize((new_width, new_height))

def pixels_to_ascii(image):
    """
    Converts each grayscale pixel to an ASCII character from ASCII_CHARS.
    - 0 (black)    -> ' ' (space)
    - ~128 (gray)  -> '#'
    - 255 (white)  -> '@'
    """
    pixels = image.getdata()
    ascii_str_list = []
    length = len(ASCII_CHARS)  # Here, it's 3

    for pixel in pixels:
        # Map pixel [0..255] -> index [0..(length-1)]
        # 0..85   -> 0 -> ' '
        # 86..170 -> 1 -> '#'
        # 171..255-> 2 -> '@'
        idx = (pixel * length) // 256
        ascii_str_list.append(ASCII_CHARS[idx])

    return "".join(ascii_str_list)

def image_to_ascii(image_path, new_width=80, scale_factor=1.0):
    """
    1) Open and convert the image to 8-bit grayscale.
    2) Resize according to new_width and scale_factor.
    3) Convert pixels to ASCII characters.
    4) Split into lines based on the new image width.
    Returns the multi-line ASCII string.
    """
    try:
        image = Image.open(image_path).convert("L")
        image = resize_image(image, new_width=new_width, scale_factor=scale_factor)
        
        ascii_str = pixels_to_ascii(image)
        
        # Break the single ASCII string into rows
        img_width = image.width
        ascii_img = "\n".join(
            ascii_str[i : i + img_width] for i in range(0, len(ascii_str), img_width)
        )
        return ascii_img
    except Exception as e:
        print(f"Error: {e}")
        return None

def ascii_to_png(ascii_str, output_path="ascii_art.png", font_path=None, font_size=16):
    """
    Renders the ASCII art onto a *transparent* PNG.
    Uses 'getbbox' to calculate character width/height, 
    avoiding 'getsize' issues in newer Pillow versions.
    """
    lines = ascii_str.split("\n")

    # Load default font if no custom font is given
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)

    # For both default and custom fonts, use 'getbbox' to measure 'X'
    left, top, right, bottom = font.getbbox("X")
    char_width = right - left
    char_height = bottom - top

    # Determine the required image size
    max_line_width = max(len(line) for line in lines)
    img_width = char_width * max_line_width
    img_height = char_height * len(lines)

    # Create a transparent RGBA image
    img = Image.new("RGBA", (img_width, img_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Draw each line of ASCII text
    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill=(0, 0, 0), font=font)
        y_offset += char_height

    # Save the result
    img.save(output_path)
    print(f"PNG saved to: {output_path}")

if __name__ == "__main__":
    # Replace with your actual image path
    image_path = r"C:\Users\Roshaan Ali Mehar\Downloads\roshaan-removebg-preview.png"

    # Generate ASCII art (tweak width and scale_factor as needed)
    ascii_art = image_to_ascii(image_path, new_width=80, scale_factor=0.5)

    if ascii_art:
        # Print the ASCII art in the console
        print(ascii_art)

        # Save to a text file
        with open("ascii_art.txt", "w") as f:
            f.write(ascii_art)
        print("ASCII art saved to ascii_art.txt")

        # Convert the ASCII art into a transparent PNG
        ascii_to_png(ascii_art, output_path="ascii_art.png", font_path=None, font_size=16)
