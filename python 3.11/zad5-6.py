def szukajWLiscie(lista: list, a):
    # Obsługuje przypadek int i float
    if isinstance(a, (int, float)):
        liczba_powtorzenia = lista.count(a)

    # Obsługuje przypadek str
    elif isinstance(a, str):
        try:
            a = float(a)
            liczba_powtorzenia = lista.count(a)
        except ValueError:
            suma_ascii = sum(ord(char) for char in a)
            liczba_powtorzenia = lista.count(suma_ascii)

    elif isinstance(a, bool):
        liczba_powtorzenia = lista.count(int(a))

    else:
        raise TypeError("Nieobsługiwany typ danych")

    print(liczba_powtorzenia)
    return liczba_powtorzenia


# Przykładowe testy:
szukajWLiscie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 611, 12, 13, 14, 15], 6)
szukajWLiscie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 611, 12, 13, 14, 15], 6.0)
szukajWLiscie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 611, 12, 13, 14, 15], "6")
szukajWLiscie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 611, 12, 13, 14, 15], "abc")
szukajWLiscie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 611, 12, 13, 14, 15], True)
szukajWLiscie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 611, 12, 13, 14, 15], False)
