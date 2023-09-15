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


def puste_pole_rysuj(i, j, row):
    for k in range(len(linia_pionowa())):
        if j == 2:
            row[k] = row[k] + puste_pole()[k]
        else:
            row[k] = row[k] + puste_pole()[k] + linia_pionowa()[k]


def x_pole_rysuj(i, j, row):
    for k in range(len(linia_pionowa())):
        if j == 2:
            row[k] = row[k] + x_pole()[k]
        else:
            row[k] = row[k] + x_pole()[k] + linia_pionowa()[k]


def o_pole_rysuj(i, j, row):
    for k in range(len(linia_pionowa())):
        if j == 2:
            row[k] = row[k] + o_pole()[k]
        else:
            row[k] = row[k] + o_pole()[k] + linia_pionowa()[k]


def generuj(tablica):
    for i in range(3):
        row = ["", "", "", "", ""]
        for j in range(3):
            if tablica[i][j] == 0:
                puste_pole_rysuj(i, j, row)

            elif tablica[i][j] == 1:
                x_pole_rysuj(i, j, row)

            elif tablica[i][j] == 2:
                o_pole_rysuj(i, j, row)
        for l in row:
            print(l)
        if i != 2:
            print(linia_pozioma())


tablica = [[0, 2, 0], [0, 1, 0], [2, 0, 1]]


generuj(tablica)

