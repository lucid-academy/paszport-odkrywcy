#!/usr/bin/env python3
"""Buduje docs/paszport-odkrywcy-offline.html z docs/index.html.

Wersja offline to ta sama gra w jednym pliku: ścieżki img/… zamienione na
obrazy wklejone w HTML (data URI). Dzięki temu plik działa bez internetu —
z maila, pendrive'a albo z dysku.

Uruchom po każdej zmianie w docs/index.html albo w docs/img/:

    python3 narzedzia/zbuduj-offline.py
"""
import base64
import mimetypes
import pathlib
import re
import sys

KORZEN = pathlib.Path(__file__).resolve().parent.parent
ZRODLO = KORZEN / "docs" / "index.html"
CEL = KORZEN / "docs" / "paszport-odkrywcy-offline.html"

html = ZRODLO.read_text(encoding="utf-8")
brakujace = []
wklejone = set()


def wklej(m):
    sciezka = m.group(0)
    plik = KORZEN / "docs" / sciezka
    if not plik.exists():
        brakujace.append(sciezka)
        return m.group(0)
    typ = mimetypes.guess_type(plik.name)[0] or "application/octet-stream"
    dane = base64.b64encode(plik.read_bytes()).decode("ascii")
    wklejone.add(sciezka)
    return f"data:{typ};base64,{dane}"


wynik = re.sub(r"img/([A-Za-z0-9._-]+)", wklej, html)

if brakujace:
    print("Brakuje plików: " + ", ".join(sorted(set(brakujace))), file=sys.stderr)
    sys.exit(1)

if "img/" in wynik:
    print("Zostały niezamienione ścieżki img/ — sprawdź plik.", file=sys.stderr)
    sys.exit(1)

CEL.write_text(wynik, encoding="utf-8")
print(f"{CEL.relative_to(KORZEN)}: {len(wklejone)} obrazów, "
      f"{CEL.stat().st_size / 1_048_576:.1f} MB")
