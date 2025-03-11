def pietro(znak):
    for i in range(3):
        if i == 1:
            print(" "+znak  + " " * 2 + "O" * 1 + " " * 2 + znak)
        else:
            print(" "+znak + " " * 5 + znak)

def dach(znak):
    szerokosc = 10
    for i in range(5):
        spacje = " " * (4 - i)
        dachowki = znak * (2 * i + 1)
        print(spacje + dachowki)

def rysuj_dom(liczba_pieter:int, znak_sciany, znak_dachu):
    if liczba_pieter <= 0:
        print("Liczba pięter musi być liczbą całkowitą większą od 0.")
        return
    if not isinstance(znak_sciany, str) or len(znak_sciany) != 1:
        print("Znak ściany musi być jednym znakiem.")
        return
    if not isinstance(znak_dachu, str) or len(znak_dachu) != 1:
        print("Znak dachu musi być jednym znakiem.")
        return
    dach(znak_dachu)
    for i in range(liczba_pieter):
        pietro(znak_sciany)

rysuj_dom(2,'|','#')
