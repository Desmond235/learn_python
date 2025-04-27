from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius **2


class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza('Pepperoni', 9)]

for shape in shapes:
    print(f'{shape.area()}cm²')