import pandas as pd
from jinja2 import Environment, FileSystemLoader

def extract_video_id(url):
    if 'youtu.be' in url:
        return url.split('/')[-1]
    elif 'youtube.com' in url:
        return url.split('v=')[-1].split('&')[0]
    return None

file_path = '../data/techniques/techniques.csv'
data = pd.read_csv(file_path)
data['video_id'] = data['video'].apply(lambda x: extract_video_id(x) if pd.notna(x) else None)

organized_data = {}
for (main_cat, sub_cat), group in data.groupby(['main_category-name', 'subcategory-name']):
    if main_cat not in organized_data:
        organized_data[main_cat] = {}
    organized_data[main_cat][sub_cat] = group.to_dict('records')

exclusion_list = ['root_category-name','root_category-kanji','root_category-furigana','en-root_category_translation','fr-root_category_translation','main_category-name','main_category-kanji','main_category-furigana','en-main_category_translation','fr-main_category_translation','subcategory-name','subcategory-kanji','subcategory-furigana','en-subcategory-translation','fr-subcategory-translation','en-description','en-translation','steps','video_id','video','picture','tutorial']  # Update your exclusion list

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/template.md')

markdown_file_content = template.render(data=organized_data, exclude=exclusion_list)

with open('../docs/techniques.md', 'w') as file:
    file.write(markdown_file_content)

print("Markdown file generated successfully using Jinja2 template!")
