class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'it is {self.color} and {'filled' if self.is_filled else 'not filled'}')

class Circle(Shape):
    def __init__(self, color, radius, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f'The area of the circle is {3.14 * self.radius * self.radius}')

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color, is_filled, width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=4)
triangle = Triangle(color='blue', is_filled=False, width=3, height=5)
square = Square(color='green', is_filled=True, width=6)

circle.describe()
