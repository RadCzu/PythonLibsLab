# 🎯 Zadania na Dziś - Python & Wizualizacja

---

## 🧠 Szybka Teoria: Czym jest `lambda`?

`lambda` to po prostu skrócona, jednolinijkowa wersja zwykłej funkcji (`def`). Zamiast pisać pełną definicję, używamy jej wtedy, gdy potrzebujemy prostej reguły "na raz". Bardziej praktycznym zastosowaniem lambdy jest wykorzystanie jej jako wskaźnik na konkretną funkcję.

### Porównanie:

**Standardowa funkcja:**
```python
def kwadrat(x):
    return x ** 2
```
To samo za pomocą lambda:
```python
kwadrat = lambda x: x ** 2
```
Oba zapisy robią dokładnie to samo: przyjmują x i zwracają x do kwadratu

### Zadanie 1: Inżynieria Wsteczna (Debugowanie)
W folderze znajduje się plik something.py.
aimportuj funkcję z tego pliku do swojego głównego programu.
Przetestuj jej działanie dla kilku różnych podanych wartości za pomocą printów i logicznego myślenia.
Przeanalizuj kod w pliku something.py (zignoruj złośliwe nazwy zmiennych i komentarze!).

Cel: Wyjaśnij prowadzącemu co dokładnie robi ta funkcja i jaki jest jej rzeczywisty algorytm.

### Zadanie 2: Uniwersalny Plotter Funkcji Matematycznych
Napisz program, który wygeneruje i wyświetli wykres dla dowolnej przekazanej mu funkcji matematycznej $y = f(x)$ w zadanym przedziale.

📖 Dokumentacja biblioteki Matplotlib: matplotlib.org/stable/contents.html

Wymagania:Zaimportuj moduł matplotlib.pyplot as plt.
Stwórz główną funkcja rysującą o nazwie generuj_wykres.
Parametry wejściowe funkcji:
$f_x$ – przekazywana funkcja matematyczna (np. zadeklarowana wcześniej za pomocą def lub lambda)
$x_start$ – początek przedziału osi X
$x_end$ – koniec przedziału osi X
$step$ – krok (odległość między punktami na wykresie)

Program ma obliczyć wartości $y$ dla każdego $x$ z podanego zakresu, wygenerować estetyczny wykres i wyświetlić go na ekranie.


### 🏆 Zadanie Domowe (Dla Chętnego): Analizator Częstotliwości Liter
Napisz program, który przeprowadzi analizę statystyczną tekstu i przedstawi jej wynik graficznie.
Wymagania:Program przyjmuje na wejściu dowolny fragment tekstu (np. zdanie lub akapit).
Zlicza wystąpienia każdej poszczególnej litery (zignoruj spacje, znaki interpunkcyjne oraz wielkość liter).
Tworzy wykres słupkowy (plt.bar), gdzie:
Oś X przedstawia poszczególne litery
Oś Y przedstawia liczbę wystąpień danej litery w tekście
Zapisuje wygenerowany wykres do pliku graficznego .png.