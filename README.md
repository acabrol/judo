# judo

Judo knowledge base and printable technique cards published on GitHub Pages.

## Content

[Vocabulary](docs/vocabulary.md)

[Techniques](docs/techniques.md)

[Cards](docs/cards.html) (print with "flip on long edge")

[Techniques CSV](data/techniques/techniques.csv)

## Regenerate the site

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 src/generate_markdown.py
python3 src/generate_cards.py
```

The generators read `data/techniques/techniques.csv` and update `docs/techniques.md`, `docs/cards.html`, and `data/techniques/techniques.json`.

## Sources

[Technical Referential French Federation of Judo](https://www.ffjudo.com/resource-file/document/1762434499_e99cb17966bb166426a2.pdf)

[Kodokan dictionary Japanese - English](https://archive.org/details/kodokan-new-japanese-english-dictionary-of-judo-etc./)
