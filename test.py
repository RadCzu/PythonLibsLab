import matplotlib.pyplot as plt

# --- 1. FUNKCJA POMOCNICZA: Generowanie krokowo listy punktów X ---
def wygeneruj_punkty_x(x_start, x_end, step):
    punkty_x = []
    aktualny_x = x_start
    
    while aktualny_x <= x_end:
        punkty_x.append(aktualny_x)
        aktualny_x += step
        
    return punkty_x


def generuj_wykres(f_x, x_start, x_end, step):
    x_val = wygeneruj_punkty_x(x_start, x_end, step)
    
    y_val = []
    for x in x_val:
        y_val.append(f_x(x))
        
    plt.figure(figsize=(9, 6))
    plt.plot(x_val, y_val, color='purple', linewidth=2)
    
    # Osie główne (0,0)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    
    # --- DYNAMICZNY KROK SIATKI ---
    min_x, max_x = min(x_val), max(x_val)
    min_y, max_y = min(y_val), max(y_val)
    
    # Wyznaczamy rozpiętość danych
    zakres_x = max_x - min_x
    zakres_y = max_y - min_y
    
    # Krok osi to ok. 1/10 całej rozpiętości wykresu (minimum 1)
    krok_x = max(1.0, round(zakres_x / 10, 1))
    krok_y = max(1.0, round(zakres_y / 10, 1))
    
    # Budujemy listę punktów podziałki osi X i Y
    ticks_x = []
    curr_x = int(min_x)
    while curr_x <= max_x + krok_x:
        ticks_x.append(curr_x)
        curr_x += krok_x

    ticks_y = []
    curr_y = int(min_y)
    while curr_y <= max_y + krok_y:
        ticks_y.append(curr_y)
        curr_y += krok_y

    plt.xticks(ticks_x)
    plt.yticks(ticks_y)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.title("Wykres z dynamicznie dopasowaną siatką")
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.legend()
    
    plt.show()


def parabola(x):
    return x**2 - 4

def f_wielomian(x):
    a = 1
    b = 0
    c = -3
    d = 0
    return a * (x**3) + b * (x**2) + c * x + d

generuj_wykres(f_wielomian, -5, 17, 0.315)