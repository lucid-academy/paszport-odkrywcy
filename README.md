# Paszport Odkrywcy Bydgoskiego Przedmieścia

Cyfrowa wersja letniej gry terenowej po Bydgoskim Przedmieściu w Toruniu — 12 przystanków,
23 zadania, rys historyczny każdego budynku i certyfikat na koniec.

**Zagraj:** https://lucid-academy.github.io/paszport-odkrywcy/

Gra działa w przeglądarce telefonu, nie wymaga instalacji ani logowania. Odpowiedzi zapisujesz
w trakcie spaceru i pokazujesz w recepcji Kulturalnego hubu przy ul. Bydgoskiej 50.

## Trasa

Pętla zaczynająca się i kończąca przy Kulturalnym hubie (ul. Bydgoska 50-52):

1. ul. Bydgoska 50-52 — dom Konrada Schwartza, dziś Kulturalny hub
2. ul. Bydgoska 42 — kamienica piekarza Gustawa Sodtke
3. ul. Bydgoska 40 — willa szachulcowa
4. ul. Konopnickiej 18 — willa z wieżyczką
5. ul. Konopnickiej 24 — żółta kamienica czynszowa
6. ul. Mickiewicza 60 — szara kamienica z nereidami
7. róg Mickiewicza i Klonowica — kamienica w stylu renesansu niderlandzkiego
8. ul. Mickiewicza 61 — secesyjna kamienica Petera Gehrza
9. ul. Mickiewicza 92 — kamienica z odsłoniętymi napisami piekarni
10. ul. Sienkiewicza 15 — kamienica neogotycka
11. ul. Sienkiewicza 4 — willa Emila Dietricha
12. ul. Bydgoska 60 — kamienica projektu Solfa i Wichardsa

## Pliki

| Ścieżka | Co to |
| --- | --- |
| `docs/index.html` | gra (wersja serwowana przez GitHub Pages) |
| `docs/img/` | fotografie i materiał archiwalny |
| `docs/paszport-odkrywcy-offline.html` | ta sama gra w jednym pliku, ze zdjęciami wbudowanymi w HTML — do wysłania mailem albo wgrania na urządzenie bez internetu |
| `narzedzia/zbuduj-offline.py` | przebudowuje plik offline z `docs/index.html` |

Gra nie ma zależności ani procesu budowania — to zwykły plik HTML. Jedyny wyjątek to
wersja offline, którą trzeba przebudować po każdej zmianie w `docs/index.html`
albo w `docs/img/`:

```
python3 narzedzia/zbuduj-offline.py
```

## Źródła i prawa

Treść gry: **Toruńska Agenda Kulturalna** / Kulturalny hub Bydgoskiego Przedmieścia,
opracowanie **Zuzanna Falleńczyk**. Rysy historyczne opierają się na Białych Kartach
Zabytków (zabytek.pl).

Ikonografia: fotografie i pocztówki archiwalne — fotopolska.eu, toruntour.pl; portret Konrada
Schwartza — archiwum rodzinne Eda Grube za nowosci.com.pl; projekt elewacji kamienicy przy
ul. Konopnickiej 24 z 1903 r. — Archiwum Państwowe w Toruniu, sygn. G1726, k. 18.
Pełna lista źródeł znajduje się w samej grze, na ekranie końcowym.

Wersja cyfrowa (demo techniczne): **Fundacja Lucid Academy** — [lucidacademy.pl](https://lucidacademy.pl).
Robimy cyfrowe narzędzia dla miast, instytucji kultury i szkół.

## Kod QR

W katalogu `qr/` leżą gotowe kody prowadzące pod adres gry — w wersji czarno-białej
(uniwersalnej) i w kolorach paszportu. Każdy w dwóch formatach: `.svg` do druku
w dowolnym rozmiarze i `.png` 2000 px do wklejenia w Wordzie albo Canvie.
Korekcja błędów Q (25%), więc kod zadziała nawet częściowo zabrudzony lub zasłonięty.
