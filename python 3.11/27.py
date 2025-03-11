class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        discount = (self.price * percent) / 100
        self.price -= discount
        print(f"Nowa cena produktu {self.name} po {percent}% zniżce: {self.price:.2f}")


produkt = Product("Laptop", 2000)
produkt.apply_discount(10) 
