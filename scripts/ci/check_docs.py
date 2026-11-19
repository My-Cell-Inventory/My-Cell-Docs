"""Validate UTF-8 Markdown and relative inline links in tracked documents."""

import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


INLINE_LINK = re.compile(r"\]\(\s*(?:<([^>\n]+)>|([^\s)]+))")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"(`+)(.+?)\1")


def check_document(path):
    try:
        content = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        print(f"{path}: el archivo debe estar en UTF-8.")
        return 1

    if not content.strip():
        print(f"{path}: el archivo está vacío.")
        return 1

    errors = 0
    fence = ""
    for number, line in enumerate(content.splitlines(), 1):
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = ""
            continue
        if marker:
            fence = marker[1]
            continue

        for match in INLINE_LINK.finditer(INLINE_CODE.sub("", line)):
            destination = match[1] or match[2]
            try:
                url = urlsplit(destination)
            except ValueError:
                print(f"{path}:{number}: enlace inválido: {destination}")
                errors += 1
                continue

            if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
                continue
            if not (path.parent / unquote(url.path)).exists():
                print(f"{path}:{number}: enlace local sin destino: {destination}")
                errors += 1
    return errors


def main():
    tracked = subprocess.check_output(["git", "ls-files", "-z"], encoding="utf-8")
    documents = [Path(name) for name in tracked.split("\0") if name.lower().endswith(".md")]
    errors = sum(check_document(path) for path in documents)
    print(f"{len(documents)} archivos Markdown revisados. {errors} errores.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
