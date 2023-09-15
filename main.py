def puste_pole():
    a = "      "
    b = "      "
    c = "      "
    d = "      "
    e = "      "
    f = "      "
    indeksy = [a, b, c, d, e, f]
    return indeksy

def linia_pionowa():
    a = "|"
    b = "|"
    c = "|"
    d = "|"
    e = "|"
    f = "|"
    indeksy = [a, b, c, d, e, f]
    return indeksy

def generuj(a,b):
    for i in range(len(a)):
        d = (a[i] + b[i])
        print(d)

def generuj_advanced(tablica):
    for i in range(3):
        for j in range(3):
            for k in range(6):
                if tablica[i][j] == 0:
                    generuj(puste_pole(), linia_pionowa())

tablica = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

generuj_advanced(tablica)

