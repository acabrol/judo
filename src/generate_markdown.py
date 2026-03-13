from __future__ import annotations

import csv
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from jinja2 import Environment, FileSystemLoader, select_autoescape


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
DATA_FILE = PROJECT_ROOT / "data" / "techniques" / "techniques.csv"
JSON_OUTPUT = PROJECT_ROOT / "data" / "techniques" / "techniques.json"
MARKDOWN_OUTPUT = PROJECT_ROOT / "docs" / "techniques.md"
HTML_OUTPUT = PROJECT_ROOT / "docs" / "techniques.html"
TEMPLATE_DIR = BASE_DIR / "templates"

EXCLUSION_LIST = [
    "root_category-name",
    "root_category-kanji",
    "root_category-furigana",
    "en-root_category_translation",
    "fr-root_category_translation",
    "main_category-name",
    "main_category-kanji",
    "main_category-furigana",
    "en-main_category-translation",
    "fr-main_category-translation",
    "subcategory-name",
    "subcategory-kanji",
    "subcategory-furigana",
    "en-subcategory-translation",
    "fr-subcategory-translation",
    "furigana",
    "en-description",
    "en-translation",
    "steps",
    "video_id",
    "video",
    "picture",
    "tutorial",
    "tutorial_url",
    "video_url",
    "video_thumbnail_url",
]


def normalize_value(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip()
    if not cleaned or cleaned.lower() == "nan":
        return None
    return cleaned


def extract_video_id(url: str | None) -> str | None:
    if not url:
        return None

    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")

    if host == "youtu.be":
        return path.split("/")[0] or None
    if host.endswith("youtube.com"):
        if path == "watch":
            return parse_qs(parsed.query).get("v", [None])[0]
        if path.startswith("shorts/"):
            return path.split("/", 1)[1].split("/")[0] or None
        if path.startswith("embed/"):
            return path.split("/", 1)[1].split("/")[0] or None

    return None


def load_techniques() -> list[dict[str, str | None]]:
    with DATA_FILE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for row in reader:
            normalized = {key: normalize_value(value) for key, value in row.items()}
            video_url = normalized.get("video")
            normalized["video_id"] = extract_video_id(video_url)
            normalized["video_url"] = video_url
            normalized["video_thumbnail_url"] = (
                f"https://img.youtube.com/vi/{normalized['video_id']}/0.jpg"
                if normalized["video_id"]
                else None
            )
            normalized["tutorial_url"] = normalized.get("tutorial")
            rows.append(normalized)
        return rows


def organize_techniques(rows: list[dict[str, str | None]]) -> dict[str, dict[str, list[dict[str, str | None]]]]:
    organized: dict[str, dict[str, list[dict[str, str | None]]]] = {}
    for row in rows:
        main_category = row["main_category-name"]
        subcategory = row["subcategory-name"]
        if not main_category or not subcategory:
            continue
        organized.setdefault(main_category, {}).setdefault(subcategory, []).append(row)
    return organized


def render_markdown(organized_data: dict[str, dict[str, list[dict[str, str | None]]]]) -> str:
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    template = env.get_template("template.md")
    return template.render(data=organized_data, exclude=EXCLUSION_LIST)


def render_html(organized_data: dict[str, dict[str, list[dict[str, str | None]]]]) -> str:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("techniques.html")
    return template.render(data=organized_data)


def main() -> None:
    rows = load_techniques()
    organized_data = organize_techniques(rows)

    with JSON_OUTPUT.open("w", encoding="utf-8") as handle:
        json.dump(organized_data, handle, ensure_ascii=False, indent=2)

    markdown = render_markdown(organized_data)
    with MARKDOWN_OUTPUT.open("w", encoding="utf-8") as handle:
        handle.write(markdown)

    html = render_html(organized_data)
    with HTML_OUTPUT.open("w", encoding="utf-8") as handle:
        handle.write(html)

    print(
        f"Generated {MARKDOWN_OUTPUT.relative_to(PROJECT_ROOT)}, "
        f"{HTML_OUTPUT.relative_to(PROJECT_ROOT)} and {JSON_OUTPUT.relative_to(PROJECT_ROOT)}"
    )


if __name__ == "__main__":
    main()
