import random

def gra_kamien_papier_nozyce():
    opcje = ["kamień", "papier", "nożyce"]
    wybor_gracza = input("Wybierz kamień, papier, lub nożyce: ").lower()
    wybor_komputera = random.choice(opcje)

    print(f"Twój wybór: {wybor_gracza}")
    print(f"Wybór komputera: {wybor_komputera}")

    if wybor_gracza == wybor_komputera:
        return "Remis!"
    elif (wybor_gracza == "kamień" and wybor_komputera == "nożyce") or \
            (wybor_gracza == "papier" and wybor_komputera == "kamień") or \
            (wybor_gracza == "nożyce" and wybor_komputera == "papier"):
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"


print(gra_kamien_papier_nozyce())
