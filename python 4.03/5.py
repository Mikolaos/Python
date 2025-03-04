
def transposition_cipher(text: str, key: int) -> str:
    if key >= len(text):
        return text
    text_list = list(text)
    text_list[key], text_list[-key-1] = text_list[-key-1], text_list[key]
    return ''.join(text_list)

print(transposition_cipher(input("Podaj tekst do zaszyfrowania: "), 10))