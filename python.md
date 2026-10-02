# 🐍 Szybka Powtórka z Pythona

Krótkie przypomnienie podstawowych konstrukcji języka, które poznaliśmy na poprzednich zajęciach.

---

## 1. Zmienne
Zmienna to wskaźnik na kontener danych. W Pythonie nie podajemy typu – system sam go rozpoznaje.

```python
wiek = 17 # liczba
imie = "Radek" # tekst
litera = 'a' # znak
wynik = 9.5 # zmienno przecinkowa liczba
czy_aktywny = True # warunek (boolean)
tablica = [1, 2, 3] # typ złożony - tablica, kilka elementów
tablica[2] = tablica[2]/2 # dzielimy przez 2; trzeci element tablicy (element pierwszy to indeks [0])
```

# 1.1 Operacje
Na liczbach można wykonywać operacje matematyczne
/+ - dodawanie
/- - odejmowanie
/* - mnożenie
// - dzielenie
/% - dzielenie modulo (reszta z dzielenia,  3 % 2 == 1)

## 2. Instrukcje Warunkowe (if / elif / else)
Program wykonuje sekcję kodu w zależności od spełnienia warunku logicznego.

punkty = 85

```python
if punkty >= 90:
    print("Ocena: 5")
elif punkty >= 75:
    print("Ocena: 4")
else:
    print("Ocena: 3 lub niższa")
```

## 3. Pętle (for oraz while)
Służą do wielokrotnego wykonywania bloku kodu.

# Pętla for (dla każdego elementu):
```python
for i in range(5):  # Liczy od 0 do 4, range(5) to funkcja zwracająca tablicę liczb [0, 1, 2, 3, 4]
    print(f"Krok numer: {i}")
```
# Pętla while (działa dopóki warunek jest prawdziwy):

```python
licznik = 3
while licznik > 0:
    print(f"Odliczanie: {licznik}")
    licznik -= 1
```

## 4. Funkcje (def)
Funkcja to wydzielony blok kodu, który przyjmuje argumenty i zwraca wynik.

```python
def pomnoz(a, b):
    iloczyn = a * b
    return iloczyn

# Wywołanie funkcji:
wynik_mnozenia = pomnoz(4, 5)
print(f"Wynik: {wynik_mnozenia}")
```

## 5. Importowanie Modułów (import)
Pozwala na używanie kodu z zewnętrznych plików lub bibliotek systemowych.

```python
import math
import os

# Użycie funkcji z zaimportowanego modułu:
pierwiastek = math.sqrt(16)
obecny_katalog = os.getcwd()

print(f"Pierwiastek: {pierwiastek}")
print(f"Katalog: {obecny_katalog}")
```