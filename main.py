# Graficzne przedstawienie pół
def puste_pole():
    a = "      "
    b = "      "
    c = "      "
    d = "      "
    e = "      "
    indeksy = [a, b, c, d, e]
    return indeksy


def x_pole():
    a = "\    /"
    b = " \  / "
    c = "  x   "
    d = " /  \ "
    e = "/    \\"
    indeksy = [a, b, c, d, e]
    return indeksy


def o_pole():
    a = "  __  "
    b = "/    \\"
    c = "|    |"
    d = " \  / "
    e = "  --  "
    indeksy = [a, b, c, d, e]
    return indeksy


def linia_pionowa():
    a = "|"
    b = "|"
    c = "|"
    d = "|"
    e = "|"
    indeksy = [a, b, c, d, e]
    return indeksy


def linia_pozioma():
    a = "-------"
    return 3 * a


# Rozrysowanie pól
def puste_pole_rysuj(j, row):
    for k in range(len(linia_pionowa())):
        if j == 2:
            row[k] = row[k] + puste_pole()[k]
        else:
            row[k] = row[k] + puste_pole()[k] + linia_pionowa()[k]


def x_pole_rysuj(j, row):
    for k in range(len(linia_pionowa())):
        if j == 2:
            row[k] = row[k] + x_pole()[k]
        else:
            row[k] = row[k] + x_pole()[k] + linia_pionowa()[k]


def o_pole_rysuj(j, row):
    for k in range(len(linia_pionowa())):
        if j == 2:
            row[k] = row[k] + o_pole()[k]
        else:
            row[k] = row[k] + o_pole()[k] + linia_pionowa()[k]


# Rozrysowanie szachownicy
def generuj(tablica):
    print("\n")
    for i in range(3):
        row = ["", "", "", "", ""]
        for j in range(3):
            if tablica[i][j] == 0:
                puste_pole_rysuj(j, row)
            elif tablica[i][j] == 1:
                x_pole_rysuj(j, row)
            elif tablica[i][j] == 2:
                o_pole_rysuj(j, row)
        for l in row:
            print(l)
        if i != 2:
            print(linia_pozioma())


# Wybór pola przez gracza
def wybor_pola():
    wiersz = int(input(f"\nPodaj numer wiersza, w którym chcesz umieścić znak {gracz}:\n")) - 1
    while wiersz < 0 or wiersz > 2:
        wiersz = int(input("\nPodaj liczbę z zakresu od 1 do 3.:\n")) - 1

    kolumna = int(input(f"\nPodaj numer kolumny, w którym chcesz umieścić znak {gracz}:\n")) - 1
    while kolumna < 0 or kolumna > 2:
        kolumna = int(input("\nPodaj liczbę z zakresu od 1 do 3:\n")) - 1

    return [wiersz, kolumna]


# Sprawdzenie czy ruch doprowadził do wygranej
def sprawdzenie_czy_wygrana(gracz):
    global game_on
    wygrana = 0
    # Czy wygrana w poziomie
    for i in range(3):
        licznik = 0
        for j in range(3):
            if tablica[i][j] == gracz:
                licznik += 1
                if licznik == 3:
                    wygrana = 1
    # Czy wygrana w pionie
    for i in range(3):
        licznik = 0
        for j in range(3):
            if tablica[j][i] == gracz:
                licznik += 1
                if licznik == 3:
                    wygrana = 1
    # Czy wygrana na skos \
    licznik = 0
    for i in range(3):
        if tablica[i][i] == gracz:
            licznik += 1
            if licznik == 3:
                wygrana = 1
    # Czy wygrana na skos /
    licznik = 0
    for i in range(3):
        if tablica[-(i + 1)][i] == gracz:
            licznik += 1
            if licznik == 3:
                wygrana = 1
    # Komunikat i koniec gry jeśli wygrana
    if wygrana == 1:
        game_on = False
        if gracz == 1:
            return print("\nWygrał gracz X")
        if gracz == 2:
            return print("\nWygrał gracz O")


# Sprawdzenie czy ruch doprowadził do remisu
def czy_remis():
    global game_on
    # Czy gra nie została przerwana przez wygraną?
    if game_on:
        licznik = 0
        for i in range(3):
            for j in range(3):
                if tablica[i][j] == 0:
                    licznik = + 1
        # Komunikat i koniec gry jeśli remis
        if licznik == 0:
            game_on = False
            return print("\nRemis")


# Macierz definiująca ustawienie
tablica = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

game_on = True
gracz = "X"
print("Kółko i Krzyżyk")
generuj(tablica)

# Pętla generująca kolejne ruchy i zmieniająca graczy
while game_on:
    print(f"\nRuch gracza {gracz}.")
    wynik = wybor_pola()

    while tablica[wynik[0]][wynik[1]] != 0:
        print("\nTo zajęte pole, proszę wybrać inne.")
        wynik = wybor_pola()

    if gracz == "X":
        tablica[wynik[0]][wynik[1]] = 1
        generuj(tablica)
        sprawdzenie_czy_wygrana(1)
        gracz = "O"
    elif gracz == "O":
        tablica[wynik[0]][wynik[1]] = 2
        generuj(tablica)
        sprawdzenie_czy_wygrana(2)
        gracz = "X"

    czy_remis()

input("\nWciśnij ENTER, aby zakończyć...\n")
