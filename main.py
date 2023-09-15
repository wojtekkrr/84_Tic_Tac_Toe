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


def linia_pozioma():
    a = "-------"
    return 3 * a


def generuj(a,b):
    for i in range(len(a)):
        d = (a[i] + b[i])
        print(d)


def generuj_advanced(tablica):
    for i in range(3):
        row = ["", "", "", "", "", ""]
        for j in range(3):
            if tablica[i][j] == 0:
                for k in range(len(linia_pionowa())):
                    row[k] = row[k] + puste_pole()[k] + linia_pionowa()[k]
        for l in row:
            print(l)
        print(linia_pozioma())


tablica = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



generuj_advanced(tablica)

