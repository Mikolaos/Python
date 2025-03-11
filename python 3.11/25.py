class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Wpłacono {amount}. Nowe saldo: {self.balance}")
        else:
            print("Kwota musi być większa niż 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Wypłacono {amount}. Nowe saldo: {self.balance}")
        elif amount > self.balance:
            print("Niewystarczające środki.")
        else:
            print("Kwota musi być większa niż 0.")


konto = BankAccount(1000)
konto.deposit(500)
konto.withdraw(200)
konto.withdraw(1500)
