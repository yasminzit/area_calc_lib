from .shapes import Shape, Circle, Triangle


def get_area(shape: Shape) -> float:
    """
    универсальная функция для вычисления площади - работает с любой фигурой, наследующей Shape
    """
    return shape.area()


def make_circle(radius: float) -> Circle:
    return Circle(radius)


def make_triangle(a: float, b: float, c: float) -> Triangle:
    return Triangle(a, b, c)
