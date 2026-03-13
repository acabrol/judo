---
layout: page
title: Judo Techniques
permalink: /docs/techniques.html
---

<style>
  @page {
    size: A4 landscape;
    margin: 10mm;
  }

  .revision-guide {
    max-width: 100%;
    font-size: 0.95rem;
  }

  .revision-guide h1 {
    margin-bottom: 0.4rem;
  }

  .revision-intro {
    margin: 0 0 1rem;
    color: #444;
  }

  .screen-note {
    margin: 0 0 1rem;
    padding: 0.75rem 1rem;
    border-left: 4px solid #b22222;
    background: #fff5f2;
    color: #6b2b1a;
  }

  .category-sheet {
    margin: 0 0 1.4rem;
    padding: 0;
    break-before: page;
    page-break-before: always;
  }

  .category-sheet:first-of-type {
    break-before: auto;
    page-break-before: auto;
  }

  .category-header {
    margin: 0 0 0.8rem;
    padding-bottom: 0.35rem;
    border-bottom: 2px solid #111;
  }

  .category-header h2 {
    margin: 0;
    font-size: 1.35rem;
  }

  .category-meta {
    margin-top: 0.2rem;
    color: #444;
    font-size: 0.95rem;
  }

  .subcategory-block {
    margin: 0 0 1rem;
    break-inside: avoid-page;
    page-break-inside: avoid;
  }

  .subcategory-title {
    margin: 0 0 0.35rem;
    font-size: 1rem;
  }

  .subcategory-meta {
    margin: 0 0 0.45rem;
    color: #555;
    font-size: 0.9rem;
  }

  .revision-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
    font-size: 0.82rem;
    line-height: 1.2;
  }

  .revision-table th,
  .revision-table td {
    border: 1px solid #bbb;
    padding: 0.3rem 0.35rem;
    vertical-align: top;
  }

  .revision-table th {
    background: #f3f0ea;
    font-size: 0.74rem;
    letter-spacing: 0.02em;
    text-transform: uppercase;
  }

  .revision-table th.col-dan,
  .revision-table td.col-dan {
    width: 4.5%;
    text-align: center;
  }

  .revision-table th.col-technique,
  .revision-table td.col-technique {
    width: 18%;
  }

  .revision-table th.col-kanji,
  .revision-table td.col-kanji {
    width: 16%;
    text-align: center;
  }

  .revision-table th.col-french,
  .revision-table td.col-french {
    width: 28%;
  }

  .revision-table th.col-translation,
  .revision-table td.col-translation {
    width: 20%;
  }

  .revision-table th.col-links,
  .revision-table td.col-links {
    width: 8%;
    text-align: center;
  }

  .technique-name {
    font-weight: 700;
  }

  .technique-kanji ruby {
    ruby-position: over;
  }

  .technique-kanji rt {
    font-size: 0.68rem;
    color: #555;
  }

  .dan-hit {
    font-weight: 700;
    color: #111;
  }

  .dan-miss {
    color: #bbb;
  }

  .media-links {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
    align-items: center;
  }

  .media-links a {
    display: inline-block;
    min-width: 3.4rem;
    padding: 0.12rem 0.3rem;
    border: 1px solid #bbb;
    border-radius: 999px;
    color: #222;
    text-decoration: none;
    font-size: 0.72rem;
    background: #fff;
  }

  .sources {
    margin-top: 1.5rem;
    font-size: 0.9rem;
  }

  .sources ul {
    margin: 0.4rem 0 0;
  }

  @media print {
    .screen-note,
    .media-links {
      display: none;
    }

    .revision-guide {
      font-size: 11px;
    }

    .revision-table {
      font-size: 9px;
    }

    .revision-table th,
    .revision-table td {
      padding: 2.2mm 2.4mm;
    }

    .revision-table th.col-links,
    .revision-table td.col-links {
      display: none;
    }
  }
</style>

<div class="revision-guide">
  <h1>Judo Techniques Revision Sheets</h1>
  <p class="revision-intro">
    Fiches compactes pour réviser les techniques, les kanji, les lectures japonaises et les attendus de grade.
  </p>
  <p class="screen-note">
    À l'écran, les colonnes <strong>Tuto</strong> et <strong>Vidéo</strong> restent disponibles.
    À l'impression, elles sont masquées pour conserver une vraie mise en page A4 paysage.
  </p>

{% for main_cat, sub_cats in data.items() -%}
{%- set first_key = sub_cats.keys() | list | first %}
{%- set category_item = sub_cats[first_key][0] %}
<section class="category-sheet">
  <header class="category-header">
    <h2>{{ main_cat }}</h2>
    <div class="category-meta">
      <ruby>{{ category_item['main_category-kanji'] }}<rt>{{ category_item['main_category-furigana'] }}</rt></ruby>
      · {{ category_item['en-main_category-translation'] }}
      · {{ category_item['fr-main_category-translation'] }}
    </div>
  </header>

{% for sub_cat, items in sub_cats.items() -%}
  <section class="subcategory-block">
    <h3 class="subcategory-title">{{ sub_cat }}</h3>
    <div class="subcategory-meta">
      <ruby>{{ items[0]['subcategory-kanji'] }}<rt>{{ items[0]['subcategory-furigana'] }}</rt></ruby>
      · {{ items[0]['en-subcategory-translation'] }}
      · {{ items[0]['fr-subcategory-translation'] }}
    </div>

    <table class="revision-table">
      <thead>
        <tr>
          <th class="col-technique">Technique</th>
          <th class="col-kanji">Kanji</th>
          <th class="col-french">Description FR</th>
          <th class="col-translation">Traduction FR</th>
          <th class="col-dan">1D</th>
          <th class="col-dan">2D</th>
          <th class="col-dan">3D</th>
          <th class="col-links">Liens</th>
        </tr>
      </thead>
      <tbody>
{% for item in items -%}
        <tr>
          <td class="col-technique">
            <div class="technique-name">{{ item.technique }}</div>
          </td>
          <td class="col-kanji technique-kanji">
            {%- if item.furigana -%}
            <ruby>{{ item.kanji }}<rt>{{ item.furigana }}</rt></ruby>
            {%- else -%}
            {{ item.kanji }}
            {%- endif -%}
          </td>
          <td class="col-french">{{ item['fr-description'] or '&nbsp;' }}</td>
          <td class="col-translation">{{ item['fr-translation'] or '&nbsp;' }}</td>
          <td class="col-dan">
            {%- if item['fr-1-dan'] == item.technique -%}
            <span class="dan-hit">●</span>
            {%- else -%}
            <span class="dan-miss">·</span>
            {%- endif -%}
          </td>
          <td class="col-dan">
            {%- if item['fr-2-dan'] == item.technique -%}
            <span class="dan-hit">●</span>
            {%- else -%}
            <span class="dan-miss">·</span>
            {%- endif -%}
          </td>
          <td class="col-dan">
            {%- if item['fr-3-dan'] == item.technique -%}
            <span class="dan-hit">●</span>
            {%- else -%}
            <span class="dan-miss">·</span>
            {%- endif -%}
          </td>
          <td class="col-links">
            <div class="media-links">
              {%- if item.tutorial_url -%}<a href="{{ item.tutorial_url }}">Tuto</a>{%- endif -%}
              {%- if item.video_url -%}<a href="{{ item.video_url }}">Vidéo</a>{%- endif -%}
            </div>
          </td>
        </tr>
{% endfor %}
      </tbody>
    </table>
  </section>
{% endfor %}
</section>
{% endfor %}

  <section class="sources">
    <h2>Sources</h2>
    <ul>
      <li><a href="https://www.ffjudo.com/uploads/elfinder/CULTURE/GRADES%20CSDGE/REFERENTIEL%20TECHNIQUE%202024-2025%20GL.pdf">FFJDA Technical Referential</a></li>
      <li><a href="https://www.judo-ch.jp">Judo Channel</a></li>
      <li><a href="https://www.youtube.com/@KODOKANJUDO">YouTube KODOKAN JUDO</a></li>
    </ul>
  </section>
</div>
