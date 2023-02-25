from PIL import Image, ImageDraw, ImageFont
import io, textwrap

def generate_meme(image_bytes, top_text, bottom_text):
    # Load the image
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert('RGB')

    # Set up font and text properties
    scale = int(img.size[1]/10)
    font = ImageFont.truetype("Impact.ttf", scale)
    outline_width = int(scale/15)
    draw = ImageDraw.Draw(img)
    font_color = (255, 255, 255)

    # Draw the top text with an outline
    textwidth, textheight = draw.textsize(top_text, font=font)
    x = (img.width - textwidth) / 2
    y = 0
    draw.text((x, y), top_text, font=font, fill=font_color)
    draw.text((x, y), top_text, font=font, fill='white', stroke_width=outline_width, stroke_fill='black')

    # Wrap the bottom text based on the image width
    max_chars_per_line = int(img.width / (scale * 0.6))
    wrapped_text = textwrap.wrap(bottom_text, width=max_chars_per_line)

    # Draw the wrapped bottom text with an outline
    wrapped_text_size = []
    for line in wrapped_text:
        line_width, line_height = draw.textsize(line, font=font)
        wrapped_text_size.append((line_width, line_height))
    
    total_height = sum([size[1] for size in wrapped_text_size])
    y = img.height - (total_height + img.height/85)
    for index, line in enumerate(wrapped_text):
        line_width, line_height = wrapped_text_size[index]
        x = (img.width - line_width) / 2
        draw.text((x, y), line, font=font, fill='white', stroke_width=outline_width, stroke_fill='black')
        y += line_height

    # Save the modified image to a bytes object
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='JPEG')
    img_byte_array.seek(0)

    # Return the image as bytes
    return img_byte_array.getvalue()