"""Regenerate the site and print its two HTML documents with Chromium."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from generate_cards import main as generate_cards
from generate_markdown import main as generate_markdown


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS = (
    ("techniques.html", "Judo Techniques Revision Sheets.pdf"),
    ("cards.html", "Detailed Judo Techniques Cards.pdf"),
)


def main() -> None:
    browser = next(
        (path for name in ("chromium-browser", "chromium", "google-chrome")
         if (path := shutil.which(name))),
        None,
    )
    if browser is None:
        raise SystemExit("Install Chromium or Google Chrome to generate the PDFs.")

    generate_markdown()
    generate_cards()
    # A directory in the project also works with Snap Chromium's private /tmp.
    with TemporaryDirectory(prefix=".judo-pdf-", dir=PROJECT_ROOT) as directory:
        temporary = Path(directory)
        for html_name, pdf_name in DOCUMENTS:
            output = temporary / pdf_name
            result = subprocess.run(
                [
                    browser,
                    "--headless",
                    "--disable-gpu",
                    "--no-pdf-header-footer",
                    "--run-all-compositor-stages-before-draw",
                    "--virtual-time-budget=15000",
                    f"--user-data-dir={temporary / 'profile'}",
                    f"--print-to-pdf={output}",
                    (PROJECT_ROOT / "docs" / html_name).as_uri(),
                ],
                capture_output=True, text=True, timeout=180,
            )
            if result.returncode or not output.exists():
                raise SystemExit(f"PDF generation failed for {html_name}:\n{result.stderr}")
            with output.open("rb") as handle:
                if handle.read(5) != b"%PDF-":
                    raise SystemExit(f"Invalid PDF generated for {html_name}")
        # Only replace existing PDFs once both documents have been generated.
        for _, pdf_name in DOCUMENTS:
            (temporary / pdf_name).replace(PROJECT_ROOT / "data" / pdf_name)
            print(f"Generated data/{pdf_name}")


if __name__ == "__main__":
    main()
