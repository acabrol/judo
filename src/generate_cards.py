import pandas as pd
import json
import qrcode
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from jinja2 import Environment, FileSystemLoader, select_autoescape
def extract_video_id(url):
    if 'youtu.be' in url:
        return url.split('/')[-1]
    elif 'youtube.com' in url:
        return url.split('v=')[-1].split('&')[0]
    return None

def generate_qrcode(url,keyword):
    # Generate the QR code image
    qr = qrcode.QRCode(
        version=2,  # Increase the version for larger QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Create a blank image with the same size as the QR code image
    overlay_img = Image.new('RGBA', qr_img.size, (255, 255, 255, 0))

    # Load a font
    font = ImageFont.truetype("arial.ttf", 20)

    # Get the size of the keyword text
    text_width, text_height = font.getmask(keyword).getbbox()[2:]

    # Calculate the position to center the keyword
    position = ((qr_img.size[0] - text_width) // 2, (qr_img.size[1] - text_height) // 2)

    # Draw the keyword text onto the overlay image
    draw = ImageDraw.Draw(overlay_img)
    draw.text(position, keyword, fill="black", font=font)

    # Combine the QR code and overlay images
    qr_img = Image.alpha_composite(qr_img.convert('RGBA'), overlay_img)

    # Convert the combined image to a base64 string
    img_buffer = BytesIO()
    qr_img.save(img_buffer, format="PNG")
    img_buffer.seek(0)
    base64_image = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    return base64_image

file_path = '../data/techniques/techniques.csv'
data = pd.read_csv(file_path)
data['video_id'] = data['video'].apply(lambda x: extract_video_id(x) if pd.notna(x) else None)
data['video_qrcode'] = data['video'].apply(lambda x: generate_qrcode(x,'video') if pd.notna(x) else None)
data['tutorial_qrcode'] = data['tutorial'].apply(lambda x: generate_qrcode(x,'tutorial') if pd.notna(x) else None)

organized_data = {}
for (main_cat, sub_cat), group in data.groupby(['main_category-name', 'subcategory-name']):
    if main_cat not in organized_data:
        organized_data[main_cat] = {}
    organized_data[main_cat][sub_cat] = group.to_dict('records')

exclusion_list = ['root_category-name','root_category-kanji','root_category-furigana','en-root_category_translation','fr-root_category_translation','main_category-name','main_category-kanji','main_category-furigana','en-main_category-translation','fr-main_category-translation','subcategory-name','subcategory-kanji','subcategory-furigana','en-subcategory-translation','fr-subcategory-translation','furigana','en-description','en-translation','steps','video_id','video','picture','tutorial']  # Update your exclusion list

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/cards.html')
# env = Environment(
#     loader=FileSystemLoader('templates/template.md'),
#     autoescape=select_autoescape(['html', 'xml']),
# )


markdown_file_content = template.render(data=organized_data, exclude=exclusion_list)

with open('../docs/cards.html', 'w') as file:
    file.write(markdown_file_content)

print("HTML file generated successfully using Jinja2 template!")
