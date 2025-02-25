
user_input = input("Wprowadź jakąś wartość: ")

if user_input.isdigit():
    print("Typ danych: int")
elif user_input.replace('.', '', 1).isdigit() and user_input.count('.') == 1:
    print("Typ danych: float")
elif user_input.lower() == "true" or user_input.lower() == "false":
    print("Typ danych: bool")
else:
    print("Typ danych: str")

