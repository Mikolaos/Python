class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


prostokat = Rectangle(5, 3)
print(prostokat.area())  
