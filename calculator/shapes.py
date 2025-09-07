import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """базовый класс для всех геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """вычислить площадь фигуры."""
        pass

    def is_right(self) -> bool:
        """
        по дефолту фигура не может быть прямоугольной
        """
        return False


class Circle(Shape):
    """круг задаётся радиусом"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """треугольник задаётся тремя сторонами"""

    def __init__(self, a: float, b: float, c: float):
        # стороны должны быть положительными
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Все стороны должны быть положительными числами")

        # неравенство треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник с такими сторонами не существует")

        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        """вычисляем площадь"""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """проверка на прямоугольность"""
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)
