import math


def statystyki(lista):
    if not lista:
        raise ValueError("Lista nie może być pusta")

    lista_posortowana = sorted(lista)

    suma = sum(lista)
    srednia = suma / len(lista)

    n = len(lista)
    if n % 2 == 1:
        mediana = lista_posortowana[n // 2]
    else:
        mediana = (lista_posortowana[n // 2 - 1] + lista_posortowana[n // 2]) / 2

    min_val = min(lista)
    max_val = max(lista)

    wariancja = sum((x - srednia) ** 2 for x in lista) / len(lista)
    odchylenie_standardowe = math.sqrt(wariancja)

    return {
        'średnia': srednia,
        'mediana': mediana,
        'min': min_val,
        'max': max_val,
        'odchylenie_standardowe': odchylenie_standardowe
    }

lista = [3, 5, 7, 9, 2, 8, 4, 6]

statystyki_result = statystyki(lista)

print("Podstawowe statystyki:")
for key, value in statystyki_result.items():
    print(f"{key}: {value:.2f}")
