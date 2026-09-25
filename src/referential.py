"""Shared season, sources and grade requirements for the generated documents."""

import json
from pathlib import Path


REFERENTIAL_FILE = Path(__file__).resolve().parent.parent / "data" / "referential.json"


def load_referential() -> dict:
    with REFERENTIAL_FILE.open(encoding="utf-8") as handle:
        return json.load(handle)
