# Fibonaci
Ciąg Fibonacciego to ciąg spełniający warunek
- każda kolejna liczba jest sumą dwuch poprzednich
- pierwsze dwa wyrazy to 0 i 1

## zadanie 1
Napisz program wypisujący n-tą liczbę z ciągu Fibonacciego w dwuch wersjach
1. Korzystając z rekurencji
2. Korzystając z pętli

# Sortowanie
Na poprzednich zajęciach mieliśmy doczynienia z sortowaniem bąbelkowym.
Algorytmy sortujące stawiają sobie jeden cel. Segregują nieouporządkowene dane na podstawie konkretnego parametru.

## zadanie 2
Napisz program generujący tablicę liczb losowych w przedziale.
Wejście:
- n (długość tablicy)
- min (najmniejsza możliwa wartość)
- max (największa możliwa wartość)
Wyjście:
- tablica liczb w przedziale (min, max) o długości n

## zadanie 3
Napisz program implementujący sortowanie bąbelkowe z poniższego pseudokodu. (Bubble sort)

Dla każdego elementu "e1" sprawdzamy jego oraz następny element "e2", jeśli "e1" jest większe od "e2", zamieniamy je miejscami
Następnie wykonujemy jeden z dwuch wariantów:
- Po dotarciu do końca, sprawdzamy czy zbiór jest posortowany, jeśli nie, wykonujemy pokownie
lub
- Wykonujemy tyle razy ile jest elementów
(Gwarantowane posortowanie! Zauważ że najwyższy element zawsze "wyniesie" się na najwyższą pozycję jak bąbelek unosi się w wodzie)

## zadanie 4
Napisz program implementujący sortowanie poprzez scalenie z poniższego pseudokodu. (Merge sort)

### merge_sort(t[]):
1. Jeśli długość tablicy "t" wynosi 1 lub 0, zwróć "t" (warunek stopu)
2. Podziel tablicę "t" na dwie równe części "t1" i "t2"
3. Wykonaj rekurencyjnie:
   t1 = merge_sort(t1)
   t2 = merge_sort(t2)

4. Scal tablice w następujący sposób:
   Stwórz nową, pustą tablicę wynikową (np. "wynik")
   Śledź indeks t1 jako i1 (zaczynając od 0, i1 = 0)
   Śledź indeks t2 jako i2 (zaczynając od 0, i2 = 0)
   
   Dopóki i1 jest mniejsze od rozmiaru tablicy t1 ORAZ i2 jest mniejsze od rozmiaru tablicy t2:
   - Jeśli t1[i1] < t2[i2]:
     Dopisz t1[i1] do tablicy wynikowej
     Zwiększ i1 o 1
   - W przeciwnym wypadku (gdy t2[i2] jest mniejsze lub równe):
     Dopisz t2[i2] do tablicy wynikowej
     Zwiększ i2 o 1
     
   Dopisz do tablicy wynikowej wszystko, co zostało w t1 (jeśli coś zostało)
   Dopisz do tablicy wynikowej wszystko, co zostało w t2 (jeśli coś zostało)
   
   Zwróć tablicę wynikową

Dlaczego ten algorytm działa statystycznie lepiej? 
- W sortowaniu bąbelkowym:
- - Każdy dodatkowy element wymaga przejścia całej tablicy w nowej iteracji na każdym elemencie. Z tąd złożoność tak zwana $O(n^2)$
- - Jeden element wymaga 1 operacji
- - 2 elementy wymahają 4
- - 3 wymagają 9
- W sortowaniu przez scalenie:
- - Każdy dodatkowy element wymaga tylko tyle dodatkowych operacji, ile jest pięter. $O(n*log(n))$
- - Dopiero podwojenie ilości elementów dodaje nam piętro.
- - 2 elementy - 1 piętro
- - 4 elementy - 2 piętra
- - 8 elementy - 3 piętra
- - 16 elementów - 4 piętra
- - 17 elementów - 5 pięter
- - 32 elementy - też 5 pięter