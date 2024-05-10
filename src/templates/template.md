# Judo Techniques Catalog

{% for main_cat, sub_cats in data.items() -%}
## {{ main_cat }}

{% for sub_cat, items in sub_cats.items() -%}
### {{ sub_cat }}

| {%- for header in items[0].keys() if header not in exclude -%}{{ header }} |{% endfor %} Picture | Video |
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
    {{ value }}
  {%- endif -%}
| {% endfor %} <a href="{{ item.tutorial }}"><img src="{{ item.picture }}" alt="Picture" style="width: 300px; height: auto;"></a>|<a href="https://youtu.be/{{ item.video_id }}"><img src="https://img.youtube.com/vi/{{ item.video_id }}/0.jpg" alt="Video Thumbnail" style="width: 300px; height: auto;"></a>|
{% endfor %}
{%- endfor %}
{%- endfor %}
