# extend-point-to-vector.py
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector to Vector")

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print(p1)
    print(p2)
    print("Distance:", p1.distance(p2))

    v1 = Vector(3, 4)
    v2 = Vector(1, 1)
    print(v1)
    print(v2)
    v3 = v1 + v2
    print("Sum of vectors:", v3)
