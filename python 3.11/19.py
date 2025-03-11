import math

def rysuj_i_oblicz_pole(typ_figury, wymiar):
    if typ_figury == "kolo":
        pole = math.pi * wymiar ** 2
        print("Rysuję koło z promieniem", wymiar)
        print("Pole koła:", pole)
    elif typ_figury == "kwadrat":
        pole = wymiar ** 2
        print("Rysuję kwadrat o boku", wymiar)
        print("Pole kwadratu:", pole)
    else:
        raise ValueError("Nieznany typ figury")

rysuj_i_oblicz_pole("kolo", 5)
rysuj_i_oblicz_pole("kwadrat", 4)
