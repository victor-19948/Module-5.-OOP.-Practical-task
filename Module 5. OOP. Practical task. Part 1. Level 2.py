class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def increase(self, coordinate, value):
        if coordinate == 'x':
            self.x += value
        if coordinate == 'y':
            self.y += value

    def decrease(self, coordinate, value):
        if coordinate == 'x':
            self.x -= value
        if coordinate == 'y':
            self.y -= value

    def multiply(self, coordinate, value):
        if coordinate == 'x':
            self.x *= value
        if coordinate == 'y':
            self.y *= value

    def division(self, coordinate, value):
        if coordinate == 'x':
            self.x //= value
        if coordinate == 'y':
            self.y //= value

    def reverse(self, coordinate):
        if coordinate == 'x':
            self.x *= -1
        if coordinate == 'y':
            self.y *= -1

    def zeroing(self, coordinate):
        if coordinate == 'x':
            self.x = 0
        if coordinate == 'y':
            self.y = 0

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)


a = Point(2, 2)
print(a.x, a.y)
a.increase('x', 5)
print(a.x, a.y)
a.increase('y', 5)
print(a.x, a.y)
a.division('x', 2)
print(a.x, a.y)
a.reverse('x')
print(a.x, a.y)
a.reverse('x')
print(a.x, a.y)

b = Point(2, 2)
c = a + b
print(c.x, c.y)
