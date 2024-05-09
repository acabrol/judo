# Judo Techniques Catalog

{% for main_cat, sub_cats in data.items() -%}
## {{ main_cat }}

{% for sub_cat, items in sub_cats.items() -%}
### {{ sub_cat }}

| {% for header in items[0].keys() if header not in exclude -%}{{ header }} |{% endfor %} Picture | Video |
| {% for header in items[0].keys() if header not in exclude -%}---|{% endfor %}---|---|
{% for item in items -%}
| {% for key, value in item.items() if key not in exclude -%}{{ value }} |{% endfor %}<a href="{{ item.tutorial }}"><img src="{{ item.picture }}" alt="Picture" style="width: 150px; height: auto;"></a>|<a href="https://youtu.be/{{ item.video_id }}"><img src="https://img.youtube.com/vi/{{ item.video_id }}/0.jpg" alt="Video Thumbnail" style="width: 150px; height: auto;"></a>|
{% endfor %}
{% endfor %}
{% endfor %}
