def puste_pole():
    a = "      "
    b = "      "
    c = "      "
    d = "      "
    e = "      "
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


def generuj(tablica):
    for i in range(3):
        row = ["", "", "", "", ""]
        for j in range(3):
            if tablica[i][j] == 0:
                for k in range(len(linia_pionowa())):
                    if j ==2:
                        row[k] = row[k] + puste_pole()[k]
                    else:
                        row[k] = row[k] + puste_pole()[k] + linia_pionowa()[k]
        for l in row:
            print(l)
        if i != 2:
            print(linia_pozioma())


tablica = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


generuj(tablica)

