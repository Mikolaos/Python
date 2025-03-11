def szyfr_cezara(tekst, klucz):
    szyfrowany_tekst = ""
    for char in tekst:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            szyfrowany_tekst += chr((ord(char) - shift + klucz) % 26 + shift)
        else:
            szyfrowany_tekst += char
    return szyfrowany_tekst


print(szyfr_cezara("Hello, World!", 3))  # "Khoor, Zruog!"
