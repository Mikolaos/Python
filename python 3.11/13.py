def sortuj_liste(lista, kierunek='rosnąco'):

    if kierunek not in ['rosnąco', 'malejąco']:
        raise ValueError("Kierunek sortowania musi być 'rosnąco' lub 'malejąco'")

    if kierunek == 'rosnąco':
        return sorted(lista)
    else:
        return sorted(lista, reverse=True)


lista_liczb = [8, 2, 5, 1, 9, 3, 7]


posortowana_rosnaco = sortuj_liste(lista_liczb, 'rosnąco')
print(f"Lista posortowana rosnąco: {posortowana_rosnaco}")


posortowana_malejąco = sortuj_liste(lista_liczb, 'malejąco')
print(f"Lista posortowana malejąco: {posortowana_malejąco}")
