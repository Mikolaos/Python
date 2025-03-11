import math


def odleglosc(P1, P2):
    if len(P1) != 2 or len(P2) != 2:
        raise ValueError("Punkty muszą być listami o dwóch elementach.")

    x1, y1 = P1
    x2, y2 = P2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def czy_wspolliniowe(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
        return True
    else:
        return False


def obwod_trojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Punkty są współliniowe, więc nie tworzą trójkąta.")
        return 0

    a = odleglosc(P1, P2)
    b = odleglosc(P2, P3)
    c = odleglosc(P3, P1)

    obwod = a + b + c
    return obwod



P1 = [3, 4]
P2 = [7, 1]
P3 = [5, 5]

obwod = obwod_trojkata(P1, P2, P3)
if obwod != 0:
    print(f"Obwód trójkąta wynosi: {obwod:.2f}")


P1 = [0, 0]
P2 = [1, 1]
P3 = [2, 2]


obwod = obwod_trojkata(P1, P2, P3)
if obwod != 0:
    print(f"Obwód trójkąta wynosi: {obwod:.2f}")
