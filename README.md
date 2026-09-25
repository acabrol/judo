# judo

Judo knowledge base and printable technique cards published on GitHub Pages.

## Content

[Vocabulary](docs/vocabulary.md)

[Techniques](docs/techniques.md)

[Cards](docs/cards.html) (print with "flip on long edge")

[Techniques CSV](data/techniques/techniques.csv)

[Évolutions du référentiel 2026-2027](docs/changements_referentiel_2026-2027.md)

## Référentiel 2026-2027

Les fiches présentent les nouvelles épreuves judo du 1er au 4e dan (kata, UV2,
efficacité sportive ou combinée, engagement et transition jusqu'au 31 décembre
2028). La saison, les sources et ces exigences sont centralisées dans
[`data/referential.json`](data/referential.json).

L'[annexe officielle 2026-2027](data/GRADES%20-%20ANNEXES%202026-2027.pdf#page=1)
conserve les listes de projections et de techniques au sol de 2025-2026 ainsi
que leur répartition par dan. Le CSV et les repères de dan restent donc inchangés.
Les colonnes 1D/2D/3D et les mentions « UV2 DAN » correspondent aux lignes de
l'annexe 1 ; elles ne résument pas l'ensemble des épreuves du grade.

## Regenerate the site

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 src/generate_markdown.py
python3 src/generate_cards.py
```

The generators read `data/techniques/techniques.csv` and `data/referential.json`
and update `docs/techniques.md`, `docs/techniques.html`, `docs/cards.html`, and
`data/techniques/techniques.json`. The JSON technique export stays unchanged
when the CSV technique data is unchanged.

To also regenerate the two printable PDFs in `data/`, install Chromium or Google
Chrome, then run (network access loads the illustrations and QR codes):

```bash
python3 src/generate_pdfs.py
```

This command first runs both site generators, then prints the revision sheets
in A4 landscape and the cards in A4 portrait. Print cards double-sided with
"flip on long edge".

## Sources

[France Judo — Référentiel technique 2026-2027](https://www.ffjudo.com/resource-file/document/1790067237_8e4fbc1c45259d99e5f5.pdf)

[France Judo — Grades, annexes 2026-2027](https://www.ffjudo.com/resource-file/document/1789035361_068de2d2976847c37f5a.pdf)

[Kodokan dictionary Japanese - English](https://archive.org/details/kodokan-new-japanese-english-dictionary-of-judo-etc./)
