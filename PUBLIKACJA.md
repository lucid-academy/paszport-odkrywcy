# Publikacja gry pod lucidacademy.pl/projekty/paszport/

Stan na 13 października 2026.

## Co ustalono

- `lucidacademy.pl` stoi na **Netlify** (nagłówek `server: Netlify`, `cache-status: "Netlify Edge"`).
- `https://lucidacademy.pl/projekty/paszport/` zwraca **404** — gry tam jeszcze nie ma.
- `https://lucidacademy.pl/projekty/swietochp/` działa, więc sam wzorzec `/projekty/<nazwa>/` jest poprawny.
- **Strona NIE jest budowana z repozytorium `pirytos25-creator/lucid`.** Serwowany
  `index.html` ma 41 922 znaki i zawiera odnośniki do `projekty/`; plik w repozytorium
  ma 35 483 znaki i nie zawiera ich wcale. Repozytorium jest nieaktualne wobec tego,
  co stoi pod domeną, i nie ma w nim katalogu `projekty/`, pliku `CNAME` ani
  konfiguracji Netlify.

Wniosek: publikacja idzie inną drogą niż push do tego repozytorium — najpewniej
ręcznym wgraniem folderu na Netlify. Żeby cokolwiek opublikować pod `/projekty/`,
trzeba dotrzeć do źródła tamtego deploya (panel Netlify → Site configuration →
Build & deploy powie, czy site jest podpięty do repozytorium, czy przyjmuje
wgrywane ręcznie foldery).

## Dwa sposoby wrzucenia gry

### A. Kopia w folderze wgrywanym na Netlify

Rozpakować `paszport/` (katalog z `index.html` i `img/`) obok `swietochp/`
i `swietoBP/` w folderze, który trafia na Netlify, i wgrać folder ponownie.

Prosto, ale każda późniejsza poprawka wymaga powtórzenia całej operacji, a wersja
pod domeną zaczyna się rozjeżdżać z repozytorium gry.

### B. Przekierowanie Netlify do tego repozytorium (zalecane)

W korzeniu folderu wgrywanego na Netlify założyć plik `_redirects` (bez rozszerzenia)
i wpisać w nim jedną linię:

```
/projekty/paszport/*  https://lucid-academy.github.io/paszport-odkrywcy/:splat  200
```

Status `200` oznacza proxy, nie przekierowanie: w pasku adresu zostaje
`lucidacademy.pl/projekty/paszport/`, a treść leci prosto z GitHub Pages.
Odnośniki w grze są względne (`img/…`), więc `:splat` przenosi je poprawnie.

Zaleta: każda zmiana w tym repozytorium pojawia się pod domeną sama, bez dotykania
Netlify. Kod QR wydrukowany raz zostaje aktualny na zawsze.

Jeśli plik `_redirects` już istnieje, dopisać linię — kolejność ma znaczenie,
pierwsza pasująca reguła wygrywa.

## Po publikacji

1. Sprawdzić, że `https://lucidacademy.pl/projekty/paszport/` otwiera grę i że
   ładują się zdjęcia (one idą przez tę samą ścieżkę).
2. Zeskanować telefonem kod z `qr/` i potwierdzić, że ląduje we właściwym miejscu.
3. Dopiero wtedy oddawać kod do druku.
