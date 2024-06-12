# Judo Techniques Catalog

{% for main_cat, sub_cats in data.items() -%}
<div class="print-section">

## {{ main_cat }}
{%- set first_key = sub_cats.keys() | list | first %}
<ruby>{{sub_cats[first_key][0]['main_category-kanji']}}<rt>{{sub_cats[first_key][0]['main_category-furigana']}}</rt></ruby>

english: {{sub_cats[first_key][0]['en-main_category-translation']}}

french: {{sub_cats[first_key][0]['fr-main_category-translation']}}

{% for sub_cat, items in sub_cats.items() -%}
{%- if sub_cat != main_cat%}
### {{ sub_cat }}

<ruby>{{items[0]['subcategory-kanji']}}<rt>{{items[0]['subcategory-furigana']}}</rt></ruby>

english: {{items[0]['en-subcategory-translation']}}

french: {{items[0]['fr-subcategory-translation']}}
{%- endif %}
| {%- for header in items[0].keys() if header not in exclude -%}{{ header }} |{% endfor %} Tutorial | Video |
| {%- for header in items[0].keys() if header not in exclude %}---|{% endfor %}---|---|
{% for item in items -%}
| {% for key, value in item.items() if key not in exclude -%}
  {%- if 'dan' in key -%}
    {%- if value == item.technique -%}
      &#10004;
    {%- elif value!=item.technique and value|string!='nan' -%}
      &#10008;
    {%- else -%}
      &nbsp;  {# Empty cell for better table formatting #}
    {%- endif -%}
  {%- else -%}
    {%- if key=='kanji' -%}
    <ruby>{{ value }}<rt>{{item['furigana']}}</rt></ruby>
    {%- elif key=='furigana' -%}
    {%- else -%}
    {{ value }}
    {%- endif -%}
  {%- endif -%}
| {% endfor %} <a href="{{ item.tutorial }}"><img src="{{ item.picture }}" alt="Tutorial" style="width: 300px; height: auto;"></a>|<a href="https://youtu.be/{{ item.video_id }}"><img src="https://img.youtube.com/vi/{{ item.video_id }}/0.jpg" alt="Video Thumbnail" style="width: 300px; height: auto;"></a>|
{% endfor %}
{%- endfor %}

</div>

{%- endfor %}

## Sources

[FFJDA Technical Referential](https://www.ffjudo.com/uploads/elfinder/CULTURE/GRADES%20CSDGE/REFERENTIEL%20TECHNIQUE%202023-2024%20%20(1).pdf)
[Judo Channel](https://www.judo-ch.jp)
[Youtube KODOKAN JUDO](https://www.youtube.com/@KODOKANJUDO)