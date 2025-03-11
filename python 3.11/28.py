class User:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password
        print(f"Użytkownik {username} został zarejestrowany.")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Zalogowano jako {username}.")
        else:
            print("Nieprawidłowy login lub hasło.")


user_system = User()
user_system.register("janek", "haslo123")
user_system.login("janek", "haslo123")
user_system.login("janek", "zlehaslo")
