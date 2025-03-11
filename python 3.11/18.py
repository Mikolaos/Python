def konwertuj_temperature(temperatura, skala="CtoF"):
    if skala == "CtoF":
        return (temperatura * 9/5) + 32
    elif skala == "FtoC":
        return (temperatura - 32) * 5/9
    elif skala == "CtoK":
        return temperatura + 273.15
    elif skala == "KtoC":
        return temperatura - 273.15
    else:
        raise ValueError("Nieznana skala")

# Testowanie funkcji
print(konwertuj_temperature(0, "CtoF"))  # 32.0
print(konwertuj_temperature(32, "FtoC"))  # 0.0
